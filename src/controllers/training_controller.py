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
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd


class TrainingController:
    """Coordena o ciclo de vida do treinamento e avaliação."""

    def __init__(
        self,
        data_path: str,
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
        self.data_handler = DataHandler(data_path)
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
        #random_states = [647] # Random State para o melhor KNNcf
        
        all_metrics = []
        all_reports = []
        all_params = []

        for i, rs in enumerate(random_states):
            X, y = preparar_dados_para_treino(self.data_handler.data_path)
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

        rs = random.randint(1, 1000)

        X, y = preparar_dados_para_treino(self.data_handler.data_path)
        #X = self.data_handler.remove_feature(X, removed_features_knn)

        #DataReport.generate_report_balenceamento(y)

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

        #X_val_scaled = PowerTransformer().fit_transform(X_val)
        importance_df = self.data_handler.make_permutation_importance(model, X_val, y_val, feature_names)
        print("\n--- Resultado da Análise de Features ---")
        print(importance_df.to_string(index=False))

        # Relatório de Importância de Features
        DataReport.generate_report_importance(importance_df)

        total_minutes = (time.time() - start_time) / 60
        print(f"Tempo gasto em minutos: {total_minutes:.2f}")




            



