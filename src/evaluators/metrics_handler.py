"""
Processamento de métricas e relatórios para Regressão.
"""
import re
from typing import Dict, List, Tuple
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from config.settings import STD_MAP


class MetricsHandler:
    """Calcula e agrega métricas de desempenho para modelos de regressão."""

    def __init__(self, metric_focus: str) -> None:
        self.metric_focus = metric_focus
        self.std_key = STD_MAP[metric_focus]

    def evaluate(self, grid: any, X_test: np.ndarray, y_test: np.ndarray) -> Tuple[Dict[str, float], str]:
        """
        Avalia o melhor modelo encontrado no GridSearch usando métricas de regressão.

        Args:
            grid: GridSearchCV treinado.
            X_test: Features de teste.
            y_test: Target de teste.

        Returns:
            Tupla com (dicionário de métricas CV, string do relatório de regressão).
        """
        best_model = grid.best_estimator_
        y_pred = best_model.predict(X_test)

        # Cálculo das métricas diretas no conjunto de teste
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)

        report = (
            "=== Relatório de Avaliação no Teste ===\n"
            f"R2 Score : {r2:.4f}\n"
            f"MAE      : {mae:.4f}\n"
            f"MSE      : {mse:.4f}\n"
            f"RMSE     : {rmse:.4f}\n"
        )

        idx = grid.best_index_
        
        # Leitura das métricas médias da Validação Cruzada do GridSearch
        # Nota: O scikit-learn usa valores negativos para MAE e MSE/RMSE no scoring (neg_*)
        # Usamos abs() para salvar com sinal positivo nos relatórios.
        cv_metrics = {
            "r2": grid.cv_results_["mean_test_r2"][idx],
            "mae": abs(grid.cv_results_["mean_test_mae"][idx]),
            "mse": abs(grid.cv_results_["mean_test_mse"][idx]),
            "rmse": abs(grid.cv_results_["mean_test_rmse"][idx]),
            "std": grid.cv_results_[self.std_key][idx],
        }
        return cv_metrics, report

    @staticmethod
    def extract_last_numbers(line: str, count: int) -> List[float]:
        """
        Extrai os últimos `count` números de uma string (incluindo suporte a números negativos e decimais).

        Args:
            line: Linha do relatório.
            count: Quantidade de números a retornar.

        Returns:
            Lista de floats encontrados.
        """
        nums = [float(x) for x in re.findall(r"[-+]?\d*\.\d+|\d+", line)]
        return nums[-count:] if len(nums) >= count else []

    def compute_average_report(self, reports: List[str]) -> str:
        """
        Calcula a média das métricas de regressão a partir de múltiplos relatórios.

        Args:
            reports: Lista de strings de relatórios gerados por `evaluate`.

        Returns:
            String formatada com a média das métricas entre as iterações.
        """
        if not reports:
            return "Nenhum relatório encontrado para calcular a média."

        accumulator = {
            "r2": [],
            "mae": [],
            "mse": [],
            "rmse": []
        }

        for report in reports:
            for line in report.splitlines():
                if "R2 Score" in line:
                    nums = self.extract_last_numbers(line, 1)
                    if nums: accumulator["r2"].append(nums[0])
                elif "MAE" in line:
                    nums = self.extract_last_numbers(line, 1)
                    if nums: accumulator["mae"].append(nums[0])
                elif "MSE" in line:
                    nums = self.extract_last_numbers(line, 1)
                    if nums: accumulator["mse"].append(nums[0])
                elif "RMSE" in line:
                    nums = self.extract_last_numbers(line, 1)
                    if nums: accumulator["rmse"].append(nums[0])

        def safe_mean(lst: list) -> float:
            return sum(lst) / len(lst) if lst else 0.0

        output = [
            "=== Média Métrica Final (Múltiplas Rodadas) ===",
            f"R2 Score Médio : {safe_mean(accumulator['r2']):.4f}",
            f"MAE Médio      : {safe_mean(accumulator['mae']):.4f}",
            f"MSE Médio      : {safe_mean(accumulator['mse']):.4f}",
            f"RMSE Médio     : {safe_mean(accumulator['rmse']):.4f}",
        ]

        return "\n".join(output)