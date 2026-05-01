"""
Controlador principal da aplicação.
"""
import time
import random
from models.data_handler import DataHandler
from models.trainer import Trainer
from evaluators.metrics_handler import MetricsHandler
from views.report_view import ReportView


class TrainingController:
    """Coordena o ciclo de vida do treinamento e avaliação."""

    def __init__(
        self,
        data_path: str,
        results_path: str,
        metric_focus: str = "recall",
        iterations: int = 10,
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
        self.trainer = Trainer(metric_focus)
        self.metrics_handler = MetricsHandler(metric_focus)
        self.view = ReportView()
        self.metric_focus = metric_focus
        self.iterations = iterations

    def run(self) -> None:
        """Executa o loop principal de treinamento, avaliação e relatório."""
        start_time = time.time()
        random_states = [random.randint(1, 1000) for _ in range(self.iterations)]

        all_metrics = []
        all_reports = []
        all_params = []

        for i, rs in enumerate(random_states):
            X_train, X_test, y_train, y_test = self.data_handler.load_and_split(
                random_state=rs
            )
            grid = self.trainer.train(X_train, y_train)
            cv_metrics, report = self.metrics_handler.evaluate(grid, X_test, y_test)

            model_name = f"modelo_pe_frontal_esquerdo_{i+1}.pkl"
            self.view.save_model(grid, model_name)

            all_metrics.append(cv_metrics)
            all_reports.append(report)
            all_params.append(grid.best_params_)


        total_minutes = (time.time() - start_time) / 60
        self.view.print_training_summary(
            all_metrics, all_reports, all_params, random_states, total_minutes, self.metric_focus
        )

        avg_report = self.metrics_handler.compute_average_report(all_reports)
        print(f"\n{'='*60}\nCLASSIFICATION REPORT (MÉDIA GERAL)\n{'='*60}")
        print(avg_report)
        print("=" * 60)