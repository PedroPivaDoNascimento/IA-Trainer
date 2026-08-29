"""
Interface de visualização e salvamento do modelo (Regressão).
"""
import joblib
import pandas as pd
from typing import Dict, List


class ReportView:
    """Responsável por toda interação de saída com o usuário e disco."""

    def display_cv_metrics(self, metrics: Dict[str, float], focus: str) -> None:
        """
        Exibe as métricas de validação cruzada para regressão no console.

        Args:
            metrics: Dicionário com as médias do CV (r2, mae, mse, rmse, std).
            focus: Métrica foco utilizada no treinamento.
        """
        header = f"\n{'='*60}\nMELHOR MODELO — OTIMIZADO POR: {focus.upper()}\n{'='*60}"
        print(header)
        print(f"{'Métrica (CV - R2 Score)':<28} {metrics['r2']:.4f}")
        print(f"{'Métrica (CV - MAE)':<28} {metrics['mae']:.4f}")
        print(f"{'Métrica (CV - MSE)':<28} {metrics['mse']:.4f}")
        print(f"{'Métrica (CV - RMSE)':<28} {metrics['rmse']:.4f}")
        print(f"{'Desvio Padrão (CV - ' + focus + ')':<28} {metrics['std']:.4f}")
        print(f"{'-'*60}")

    def save_model(self, grid: any, filename: str) -> None:
        """
        Serializa o melhor pipeline encontrado.

        Args:
            grid: GridSearchCV com o modelo ajustado.
            filename: Nome do arquivo de saída.
        """
        joblib.dump(grid.best_estimator_, filename)
        print(f"\n💾 Modelo exportado com sucesso para: '{filename}'")

    def print_training_summary(
        self,
        all_metrics: List[Dict[str, float]],
        all_reports: List[str],
        all_params: List[dict],
        random_states: List[int],
        metric_focus: str
    ) -> None:
        """
        Exibe o resumo final do treinamento e os relatórios de regressão.

        Args:
            all_metrics: Lista de dicionários de métricas por execução.
            all_reports: Lista de relatórios em texto.
            all_params: Lista de melhores hiperparâmetros.
            random_states: Sementes utilizadas.
            metric_focus: Métrica principal da otimização.
        """
        print("\n Melhores modelos:")
        for i in range(len(all_metrics)):
            print(f"\n\t====== MODELO {i+1} ======")
            self.display_cv_metrics(all_metrics[i], metric_focus)
            print(all_reports[i])
            print(f"Parâmetros: {all_params[i]}")
            print(f"Random State usado: {random_states[i]}")