"""
Módulo adaptado para treinamento de ML com configuração dinâmica via Django.
Recebe parâmetros de validação cruzada e random_state para reprodutibilidade.
"""
from typing import Any, Dict, List
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.feature_selection import SelectKBest, f_classif
import joblib
import os
from django.conf import settings


class DynamicTrainer:
    """
    Treinador dinâmico que constrói pipelines baseados em configuração JSON.
    Aceita cv (folds) e random_state para controle total da validação cruzada.
    """
    
    # Mapeamento de nomes de classes para imports do scikit-learn
    SCALERS = {
        'StandardScaler': StandardScaler,
        'RobustScaler': lambda **kwargs: __import__('sklearn.preprocessing', fromlist=['RobustScaler']).RobustScaler(**kwargs),
        'MinMaxScaler': lambda **kwargs: __import__('sklearn.preprocessing', fromlist=['MinMaxScaler']).MinMaxScaler(**kwargs),
        'MaxAbsScaler': lambda **kwargs: __import__('sklearn.preprocessing', fromlist=['MaxAbsScaler']).MaxAbsScaler(**kwargs),
        'QuantileTransformer': lambda **kwargs: __import__('sklearn.preprocessing', fromlist=['QuantileTransformer']).QuantileTransformer(**kwargs),
        'PowerTransformer': lambda **kwargs: __import__('sklearn.preprocessing', fromlist=['PowerTransformer']).PowerTransformer(**kwargs),
        'Normalizer': lambda **kwargs: __import__('sklearn.preprocessing', fromlist=['Normalizer']).Normalizer(**kwargs),
    }
    
    REDUCERS = {
        'PCA': PCA,
        'SelectKBest': lambda **kwargs: __import__('sklearn.feature_selection', fromlist=['SelectKBest', 'f_classif']).SelectKBest(score_func=f_classif, **kwargs),
    }
    
    CLASSIFIERS = {
        'MLPClassifier': lambda **kwargs: __import__('sklearn.neural_network', fromlist=['MLPClassifier']).MLPClassifier(**kwargs),
        'RandomForestClassifier': lambda **kwargs: __import__('sklearn.ensemble', fromlist=['RandomForestClassifier']).RandomForestClassifier(**kwargs),
        'SVC': lambda **kwargs: __import__('sklearn.svm', fromlist=['SVC']).SVC(**kwargs),
        'LinearSVC': lambda **kwargs: __import__('sklearn.svm', fromlist=['LinearSVC']).LinearSVC(**kwargs),
        'KNeighborsClassifier': lambda **kwargs: __import__('sklearn.neighbors', fromlist=['KNeighborsClassifier']).KNeighborsClassifier(**kwargs),
        'LogisticRegression': lambda **kwargs: __import__('sklearn.linear_model', fromlist=['LogisticRegression']).LogisticRegression(**kwargs),
        'GradientBoostingClassifier': lambda **kwargs: __import__('sklearn.ensemble', fromlist=['GradientBoostingClassifier']).GradientBoostingClassifier(**kwargs),
        'ExtraTreesClassifier': lambda **kwargs: __import__('sklearn.ensemble', fromlist=['ExtraTreesClassifier']).ExtraTreesClassifier(**kwargs),
        'RidgeClassifier': lambda **kwargs: __import__('sklearn.linear_model', fromlist=['RidgeClassifier']).RidgeClassifier(**kwargs),
        'Perceptron': lambda **kwargs: __import__('sklearn.linear_model', fromlist=['Perceptron']).Perceptron(**kwargs),
    }
    
    def __init__(self, metric_focus: str = 'f1_score'):
        """
        Inicializa o treinador.
        
        Args:
            metric_focus: Métrica alvo para otimização no GridSearchCV.
        """
        self.metric_focus = metric_focus
        self.scoring = {
            'accuracy': 'accuracy',
            'precision': 'precision',
            'recall': 'recall',
            'f1_score': 'f1',
            'roc_auc': 'roc_auc'
        }
        self.refit_metric = self.scoring.get(metric_focus, 'f1')
    
    def _create_instance(self, class_name: str, params: Dict = None):
        """Cria uma instância de uma classe scikit-learn."""
        params = params or {}
        
        # Tenta encontrar nas mappings
        all_mappings = {**self.SCALERS, **self.REDUCERS, **self.CLASSIFIERS}
        
        if class_name in all_mappings:
            factory = all_mappings[class_name]
            try:
                return factory(**params)
            except Exception as e:
                print(f"Erro ao criar instância de {class_name}: {e}")
                raise
        
        # Fallback: tenta importar diretamente
        raise ValueError(f"Classe não encontrada: {class_name}")
    
    def build_pipeline_and_grid(self, config: Dict, random_state: int):
        """
        Constrói o Pipeline e o param_grid dinamicamente a partir da configuração JSON.
        
        Args:
            config: Dicionário com configuração do scaler, pca e classifier.
            random_state: Semente aleatória para reprodutibilidade.
            
        Returns:
            Tuple (pipeline, param_grid)
        """
        # Extrai configurações
        scaler_config = config.get('scaler', {'class': 'StandardScaler', 'params': {}})
        pca_config = config.get('pca', {'enabled': False})
        classifier_config = config.get('classifier')
        
        if not classifier_config:
            raise ValueError("Configuração do classifier é obrigatória.")
        
        # Cria steps do pipeline
        steps = []
        param_grid = {}
        
        # Step 1: Scaler
        scaler_class = scaler_config.get('class', 'StandardScaler')
        scaler_params = scaler_config.get('params', {})
        scaler_instance = self._create_instance(scaler_class, scaler_params)
        steps.append(('scaler', scaler_instance))
        
        # Adiciona parâmetros do scaler ao grid (se houver params_grid)
        scaler_grid = scaler_config.get('params_grid', {})
        for param_name, values in scaler_grid.items():
            param_grid[f'scaler__{param_name}'] = values
        
        # Step 2: PCA (opcional)
        if pca_config.get('enabled', False):
            pca_class = pca_config.get('class', 'PCA')
            pca_params = pca_config.get('params', {})
            # Garante random_state no PCA se aplicável
            if 'random_state' not in pca_params and pca_class == 'PCA':
                pca_params['random_state'] = random_state
            pca_instance = self._create_instance(pca_class, pca_params)
            steps.append(('pca', pca_instance))
            
            # Adiciona parâmetros do PCA ao grid
            pca_grid = pca_config.get('params_grid', {})
            for param_name, values in pca_grid.items():
                param_grid[f'pca__{param_name}'] = values
        else:
            # Passthrough - não faz redução
            steps.append(('pca', 'passthrough'))
        
        # Step 3: Classifier
        classifier_class = classifier_config.get('class')
        classifier_params = classifier_config.get('params', {})
        # Garante random_state no classifier se aplicável
        if 'random_state' not in classifier_params and classifier_class in ['MLPClassifier', 'RandomForestClassifier', 'SVC', 'LinearSVC', 'ExtraTreesClassifier', 'GradientBoostingClassifier', 'LogisticRegression', 'RidgeClassifier', 'Perceptron']:
            classifier_params['random_state'] = random_state
        classifier_instance = self._create_instance(classifier_class, classifier_params)
        steps.append(('classifier', classifier_instance))
        
        # Adiciona parâmetros do classifier ao grid
        classifier_grid = classifier_config.get('params_grid', {})
        for param_name, values in classifier_grid.items():
            param_grid[f'classifier__{param_name}'] = values
        
        # Cria o pipeline
        pipeline = Pipeline(steps)
        
        return pipeline, param_grid
    
    def train(
        self, 
        X_train: np.ndarray, 
        y_train: np.ndarray, 
        config: Dict, 
        cv_folds: int = 5, 
        random_state: int = 42
    ):
        """
        Executa o GridSearchCV com configuração dinâmica.
        
        Args:
            X_train: Features de treino.
            y_train: Labels de treino.
            config: Configuração JSON do pipeline.
            cv_folds: Número de folds para validação cruzada.
            random_state: Semente aleatória para StratifiedKFold e reprodutibilidade.
            
        Returns:
            Objeto GridSearchCV treinado.
        """
        # Constrói pipeline e grid dinamicamente
        pipeline, param_grid = self.build_pipeline_and_grid(config, random_state)
        
        # Cria StratifiedKFold com random_state controlado
        cv = StratifiedKFold(
            n_splits=cv_folds,
            shuffle=True,
            random_state=random_state
        )
        
        # Cria GridSearchCV
        grid = GridSearchCV(
            estimator=pipeline,
            param_grid=param_grid,
            cv=cv,
            n_jobs=-1,  # Usa todos os cores disponíveis
            scoring=self.scoring,
            refit=self.refit_metric,
            verbose=1,
            error_score='raise'  # Falha rápido se houver erro
        )
        
        # Executa o fit
        grid.fit(X_train, y_train)
        
        return grid
    
    def save_model(self, grid_search: Any, model_name: str):
        """
        Salva o melhor modelo encontrado.
        
        Args:
            grid_search: GridSearchCV treinado.
            model_name: Nome do arquivo .pkl.
        """
        modelos_dir = os.path.join(settings.MEDIA_ROOT, 'modelos_treinados')
        os.makedirs(modelos_dir, exist_ok=True)
        
        file_path = os.path.join(modelos_dir, model_name)
        joblib.dump(grid_search.best_estimator_, file_path)
        
        return file_path
