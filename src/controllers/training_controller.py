"""
Controlador principal da aplicação.
"""
import time
import random
from models.data_handler import DataHandler
from models.trainer import Trainer
from evaluators.metrics_handler import MetricsHandler
from views.report_view import ReportView
from models.excel_geter import preparar_dados_para_treino, pegar_nomes_das_features
from views.data_report import DataReport
from views.advanced_visualizations import AdvancedVisualizations, TrainingDiagnostic
from sklearn.preprocessing import RobustScaler, PowerTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd


class TrainingController:
    """Coordena o ciclo de vida do treinamento e avaliação."""

    def __init__(
        self,
        data_path: str,
        results_path: str,
        metric_focus: str = "recall",
        iterations: int = 10,
        dict_params: dict = None

    ) -> None:
        """
        Inicializa as dependências do controlador.

        Args:
            data_path: Caminho para features.
            results_path: Caminho para labels.
            metric_focus: Métrica alvo.
            iterations: Número de execuções com random states diferentes.
        """
        self.data_handler = DataHandler(data_path, results_path)
        self.trainer = Trainer(metric_focus, dict_params=dict_params)
        self.metrics_handler = MetricsHandler(metric_focus)
        self.view = ReportView()
        self.metric_focus = metric_focus
        self.iterations = iterations



    def run(self) -> None:
        """Executa o loop principal de treinamento, avaliação e relatório."""
        start_time = time.time()
        random_states = [random.randint(1, 1000) for _ in range(self.iterations)]
        #removed_features_mlp = ["big_toe_x_iqr", "heel_y_iqr"]
        #removed_features_mlp = ["ankle_y_std", "ankle_x_iqr", "heel_x_std", "big_toe_y_std", "heel_x_iqr", "big_toe_x_iqr", "heel_y_iqr"]
        #removed_features_knn = ["heel_x_iqr", "heel_y_std"]
        #random_states = [777]    # Random State para o melhor MLP 
        #random_states = [647] # Random State para o melhor KNN
        
        all_metrics = []
        all_reports = []
        all_params = []

        for i, rs in enumerate(random_states):
            X, y = preparar_dados_para_treino(self.data_handler.data_path, self.data_handler.results_path)
            #X = self.data_handler.remove_feature(X, removed_features_mlp)
            X_train, X_test, y_train, y_test = self.data_handler.load_and_split(
                random_state=rs, X=X, y=y
            )
            grid = self.trainer.train(X_train, y_train, random_state=rs)
            cv_metrics, report = self.metrics_handler.evaluate(grid, X_test, y_test)

            model_name = f"modelo_pe_frontal_esquerdo_{i+1}.pkl"
            self.view.save_model(grid, model_name)

            all_metrics.append(cv_metrics)
            all_reports.append(report)
            all_params.append(grid.best_params_)


        total_minutes = (time.time() - start_time) / 60
        self.view.print_training_summary(
            all_metrics, all_reports, all_params, random_states, self.metric_focus
        )

        avg_report = self.metrics_handler.compute_average_report(all_reports)
        print(f"\n{'='*60}\nCLASSIFICATION REPORT (MÉDIA GERAL)\n{'='*60}")
        print(avg_report)
        print("=" * 60)
        print(f"Tempo gasto em minutos: {total_minutes:.2f}")

        return   
    
    def run_data_analysis(self) -> None:
        """Executa análises exploratórias nos dados."""
        start_time = time.time()

        rs = 777 # random_state do melhor modelo encontrado para o MLP
        #rs = 647 # random_state do melhor modelo encontrado para o KNN
        #removed_features_knn = ["heel_x_iqr"]
        #removed_features_mlp = ["big_toe_x_iqr"]

        X, y = preparar_dados_para_treino(self.data_handler.data_path, self.data_handler.results_path)
        #X = self.data_handler.remove_feature(X, removed_features_knn)

        DataReport.generate_report_balenceamento(y)

        feature_names = pegar_nomes_das_features(self.data_handler.data_path)
       
        X_train, X_val, y_train, y_val = self.data_handler.load_and_split_analysis(
            random_state=rs, X=X, y=y
        )
    
        model = self.trainer.train(X_train, y_train, random_state=rs)
        baseline_score = model.score(X_val, y_val)
        print(f"Acurácia inicial do modelo: {baseline_score:.4f}")

        # Diagnóstico de aprendizado (Overfitting/Underfitting)
        print("\n--- Diagnóstico de Aprendizado ---")
        TrainingDiagnostic.analisar_aprendizado(
            modelo=model.best_estimator_,
            X_treino=X_train,
            y_treino=y_train,
            X_teste=X_val,
            y_teste=y_val
        )

        X_val_scaled = PowerTransformer().fit_transform(X_val)
        importance_df = self.data_handler.make_permutation_importance(model, X_val_scaled, y_val, feature_names)
        print("\n--- Resultado da Análise de Features ---")
        print(importance_df.to_string(index=False))

        # Relatório de Importância de Features
        DataReport.generate_report_importance(importance_df)
        
        # Matriz de Confusão
        AdvancedVisualizations.plot_confusion_matrix(y_val, model.predict(X_val_scaled), class_names=["Classe 0", "Classe 1"], dataset_name="Pé frontal esquerdo - 150 amostras - 2 classes")
        
  
        print("\n--- Gerando Visualizações Detalhadas ---")
        
        # Preparar dados completos para visualizações (sem split)
        X_full, y_full = preparar_dados_para_treino(self.data_handler.data_path, self.data_handler.results_path)
        X_full_scaled = RobustScaler().fit_transform(X_full)
        X_full_df = pd.DataFrame(X_full_scaled, columns=feature_names)
        
        # Treinar modelos adicionais para comparação de importância
        rf_model = RandomForestClassifier(n_estimators=100, random_state=rs, n_jobs=-1)
        rf_model.fit(X_full_scaled, y_full)
        
        lr_model = LogisticRegression(max_iter=1000, random_state=rs)
        lr_model.fit(X_full_scaled, y_full)
        
        # Extrair importâncias da árcore
        rf_feature_importances = rf_model.feature_importances_
        
        # Para Regressão Logística eu peguei a média dos valores absolutos dos coeficientes
        if len(lr_model.coef_.shape) == 2 and lr_model.coef_.shape[0] > 1:
            lr_coefficients = np.mean(np.abs(lr_model.coef_), axis=0)
        else:
            lr_coefficients = np.abs(lr_model.coef_.flatten())
        
        # Comparação de Importância de Features com Gráficos
        print("\n Gerando comparação de importância de features...")
        AdvancedVisualizations.plot_feature_importance_comparison(
            permutation_importance_df=importance_df,
            rf_feature_importances=rf_feature_importances,
            lr_coefficients=lr_coefficients,
            feature_names=feature_names,
            dataset_name="Pé frontal esquerdo - 150 amostras - 2 classes"
        )
        
        # Identificar Top 2 features de cada método
        top_features_dict = AdvancedVisualizations.get_top_2_features(
            permutation_importance_df=importance_df,
            rf_feature_importances=rf_feature_importances,
            lr_coefficients=lr_coefficients,
            feature_names=feature_names
        )
        
        print(f"\nTop 2 Features - Permutation Importance: {top_features_dict['permutation']}")
        print(f"Top 2 Features - Random Forest: {top_features_dict['random_forest']}")
        print(f"Top 2 Features - Logistic Regression: {top_features_dict['logistic_regression']}")
        
        # Plots 2D com as Duas Melhores Features de Cada Método
        print("\nGerando plots 2D das top features...")
        AdvancedVisualizations.plot_2d_scatter_top_features(
            X=X_full_df,
            y=y_full,
            top_features_dict=top_features_dict,
            class_names=["Classe 0", "Classe 1"],
            dataset_name="Pé frontal esquerdo - 150 amostras - 2 classes"
        )
        
        total_minutes = (time.time() - start_time) / 60
        print(f"Tempo gasto em minutos: {total_minutes:.2f}")




            



