"""
Interface de visualização e salvar o modelo.
"""
import joblib
import pandas as pd
from typing import Dict, List


class ReportView:
    """Responsável por toda interação de saída com o usuário e disco."""

    def display_cv_metrics(self, metrics: Dict[str, float], focus: str) -> None:
        """
        Exibe as métricas de validação cruzada no console.

        Args:
            metrics: Dicionário com as médias do CV.
            focus: Métrica foco utilizada no treinamento.
        """
        header = f"\n{'='*60}\nMELHOR MODELO — OTIMIZADO POR: {focus.upper()}\n{'='*60}"
        print(header)
        print(f"{'Acuracia(CV - accuracy)':<28} {metrics['accuracy']:.2f}%")
        print(f"{'Acuracia(CV - f1_score)':<28} {metrics['f1_score']:.2f}%")
        print(f"{'Acuracia(CV - precision)':<28} {metrics['precision']:.2f}%")
        print(f"{'Acuracia(CV - recall)':<28} {metrics['recall']:.2f}%")
        print(f"{'Desvio Padrão (CV - ' + focus + ')':<28} {metrics['std']:.4f}%")
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
        Exibe o resumo final do treinamento e a média dos relatórios.

        Args:
            all_metrics: Lista de dicionários de métricas por execução.
            all_reports: Lista de strings de classificação.
            all_params: Lista de melhores hiperparâmetros.
            random_states: Sementes utilizadas.
            total_minutes: Tempo total de execução.
        """
        print("\n Melhores modelos:")
        for i in range(len(all_metrics)):
            print(f"\n\t====== MODELO {i+1} ======")
            self.display_cv_metrics(all_metrics[i], metric_focus)
            print(all_reports[i])
            print(f"Parâmetros: {all_params[i]}")
            print(f"Random State usado: {random_states[i]}")