"""
Módulo responsável pelo treinamento dinâmico de modelos de ML.
Constrói Pipelines e Param Grids baseados em configuração JSON.
"""
import os
import joblib
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import make_scorer, f1_score, accuracy_score, precision_score, recall_score

class DynamicTrainer:
    """
    Classe que gerencia a construção dinâmica do Pipeline e treinamento com GridSearchCV.
    """
    
    def __init__(self, metric_focus='f1_score'):
        self.metric_focus = metric_focus
        self.save_dir = os.path.join('media', 'modelos_treinados')
        os.makedirs(self.save_dir, exist_ok=True)
        
        # Mapeamento de Scalers
        self.scalers_map = {
            'StandardScaler': StandardScaler,
            'MinMaxScaler': MinMaxScaler,
            'RobustScaler': RobustScaler
        }
        
        # Mapeamento de Redutores (PCA e SelectKBest)
        self.reducers_map = {
            'PCA': PCA,
            'SelectKBest': SelectKBest
        }
        
        # Mapeamento de Classificadores
        self.classifiers_map = {
            'RandomForestClassifier': RandomForestClassifier,
            'MLPClassifier': MLPClassifier,
            'SVC': SVC,
            'LogisticRegression': LogisticRegression,
            'GradientBoostingClassifier': GradientBoostingClassifier
        }

    def build_pipeline(self, config):
        """
        Constrói o Pipeline do scikit-learn baseado na configuração JSON.
        """
        steps = []
        
        # 1. Adicionar Scaler (Sempre presente)
        scaler_config = config.get('scaler', {})
        scaler_name = scaler_config.get('class', 'StandardScaler')
        scaler_params = scaler_config.get('params', {})
        
        if scaler_name in self.scalers_map:
            steps.append(('scaler', self.scalers_map[scaler_name](**scaler_params)))
        else:
            # Fallback para StandardScaler se nome inválido
            steps.append(('scaler', StandardScaler()))
            
        # 2. Adicionar Redutor de Dimensionalidade (Opcional)
        pca_config = config.get('pca', {})
        if pca_config.get('enabled', False):
            reducer_name = pca_config.get('class', 'PCA')
            reducer_params = pca_config.get('params', {})
            
            if reducer_name in self.reducers_map:
                steps.append(('pca', self.reducers_map[reducer_name](**reducer_params)))
            else:
                steps.append(('pca', PCA(**reducer_params)))
        
        # 3. Adicionar Classificador
        clf_config = config.get('classifier', {})
        clf_name = clf_config.get('class', 'RandomForestClassifier')
        # Params vazios aqui, pois serão injetados pelo GridSearch
        
        if clf_name in self.classifiers_map:
            steps.append(('classifier', self.classifiers_map[clf_name]()))
        else:
            steps.append(('classifier', RandomForestClassifier()))
            
        return Pipeline(steps)

    def build_param_grid(self, config):
        """
        Constrói o dicionário param_grid para o GridSearchCV.
        Usa a notação de prefixos (ex: scaler__param).
        """
        param_grid = {}
        
        # Scaler Params
        scaler_config = config.get('scaler', {})
        scaler_params_grid = scaler_config.get('params_grid', {})
        for param, values in scaler_params_grid.items():
            param_grid[f'scaler__{param}'] = values
            
        # PCA Params (se enabled)
        pca_config = config.get('pca', {})
        if pca_config.get('enabled', False):
            pca_params_grid = pca_config.get('params_grid', {})
            for param, values in pca_params_grid.items():
                param_grid[f'pca__{param}'] = values
        else:
            # Se não estiver habilitado mas houver params no grid, podemos ignorar ou forçar None
            # Aqui vamos ignorar para simplificar
            pass
            
        # Classifier Params
        clf_config = config.get('classifier', {})
        clf_params_grid = clf_config.get('params_grid', {})
        for param, values in clf_params_grid.items():
            param_grid[f'classifier__{param}'] = values
            
        return param_grid

    def train(self, X_train, y_train, config, cv_folds=5, random_state=42):
        """
        Executa o treinamento com GridSearchCV.
        """
        pipeline = self.build_pipeline(config)
        param_grid = self.build_param_grid(config)
        
        # Configuração de Métricas Múltiplas
        scoring = {
            'accuracy': make_scorer(accuracy_score),
            'precision': make_scorer(precision_score, average='weighted'),
            'recall': make_scorer(recall_score, average='weighted'),
            'f1': make_scorer(f1_score, average='weighted')
        }
        
        # Validação Cruzada Estratificada com Random State Controlado
        cv_strategy = StratifiedKFold(n_splits=cv_folds, shuffle=True, random_state=random_state)
        
        # Instanciação do GridSearchCV
        # CORREÇÃO AQUI: refit='f1' é obrigatório quando scoring é um dict
        grid_search = GridSearchCV(
            estimator=pipeline,
            param_grid=param_grid,
            scoring=scoring,
            cv=cv_strategy,
            refit='f1',  # Define qual métrica usar para escolher o best_estimator_
            n_jobs=-1,   # Usa todos os núcleos da CPU
            verbose=1,
            error_score='raise' # Falha rápido se houver erro nos params
        )
        
        print("Iniciando GridSearchCV...")
        grid_search.fit(X_train, y_train)
        print("Treinamento concluído.")
        
        return grid_search

    def save_model(self, model_object, filename):
        """
        Salva o modelo treinado em disco.
        """
        filepath = os.path.join(self.save_dir, filename)
        joblib.dump(model_object, filepath)
        print(f"Modelo salvo em: {filepath}")
        return filepath