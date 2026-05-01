"""
Processamento de métricas e relatórios.
"""
import re
from typing import Dict, List, Tuple
import numpy as np
from sklearn.metrics import classification_report
from config.settings import STD_MAP, CLASS_NAMES


class MetricsHandler:
    """Calcula e agrega métricas de desempenho do modelo."""

    def __init__(self, metric_focus: str) -> None:
        self.metric_focus = metric_focus
        self.std_key = STD_MAP[metric_focus]

    def evaluate(self, grid: any, X_test: np.ndarray, y_test: np.ndarray) -> Tuple[Dict[str, float], str]:
        """
        Avalia o melhor modelo encontrado no GridSearch.

        Args:
            grid: GridSearchCV treinado.
            X_test: Features de teste.
            y_test: Labels de teste.

        Returns:
            Tupla com (dicionário de métricas CV, string do classification_report).
        """
        best_model = grid.best_estimator_
        y_pred = best_model.predict(X_test)
        report = classification_report(
            y_test, y_pred, target_names=CLASS_NAMES, zero_division=0
        )

        idx = grid.best_index_
        cv_metrics = {
            "accuracy": grid.cv_results_["mean_test_accuracy"][idx] * 100,
            "f1_score": grid.cv_results_["mean_test_f1"][idx] * 100,
            "precision": grid.cv_results_["mean_test_precision"][idx] * 100,
            "recall": grid.cv_results_["mean_test_recall"][idx] * 100,
            "std": grid.cv_results_[self.std_key][idx] * 100,
        }
        return cv_metrics, report

    @staticmethod
    def extract_last_numbers(line: str, count: int) -> List[float]:
        """
        Extrai os últimos `count` números de uma string.

        Args:
            line: Linha do relatório de classificação.
            count: Quantidade de números a retornar.

        Returns:
            Lista de floats encontrados.
        """

        #\d+: Procura um ou mais dígitos (ex: 1, 50, 123).
        #\.: Procura um ponto literal (o separador decimal).
        #\d+\.\d+: Procura números com casas decimais (ex: 0.85, 10.5).
        #|: Significa "OU".
        #\d+: Procura números inteiros (ex: 50, 100).
        nums = [float(x) if "." in x else int(x) for x in re.findall(r"\d+\.\d+|\d+", line)]

        # Retornmas os ultimos count numeros da linha se tivermos mais de count numeros
        return nums[-count:] if len(nums) >= count else []

    def compute_average_report(self, reports: List[str]) -> str:
        """
        Calcula a média ponderada das métricas de múltiplos relatórios.

        Args:
            reports: Lista de strings `classification_report`.

        Returns:
            String formatada com a média das métricas.
        """
        if not reports:
            return "Nenhum relatório encontrado para calcular a média."

        # Criando um dicíonario que guarda o precision, recall, f1 e support de cada classe
        accumulator = {
            cls: {"p": [], "r": [], "f": [], "s": []} for cls in CLASS_NAMES
        }

        # Adicionando os valores de accuracy, macro avg e weighted avg para cada métrica
        accumulator.update({
            "accuracy": {"acc": [], "s": []},
            "macro avg": {"p": [], "r": [], "f": [], "s": []},
            "weighted avg": {"p": [], "r": [], "f": [], "s": []},
        })

        # Pegando cada report na lista de todos os reports
        for report in reports:
            for line in report.splitlines(): # Esse splitlines transforma cada quebra de linha em uma lista de strings
                for cls in CLASS_NAMES:
                    if cls in line: # Se a classe estiver na linha
                        # Extrai os últimos 4 números da linha (Precision, Recall, F1, Support).
                        nums = self.extract_last_numbers(line, 4)
                        if len(nums) == 4:
                            # zip associa as chaves ['p','r','f','s'] aos valores encontrados [num1, num2, num3, num4]
                            for k, v in zip(["p", "r", "f", "s"], nums):
                                accumulator[cls][k].append(v)

                # Verificando se estamos na linha de accuracy
                if "accuracy" in line:
                    nums = self.extract_last_numbers(line, 2)
                    if len(nums) == 2:
                        accumulator["accuracy"]["acc"].append(nums[0])
                        accumulator["accuracy"]["s"].append(nums[1])

                # Percorrendo as linhas da média
                for avg in ["macro avg", "weighted avg"]:
                    if avg in line:
                        nums = self.extract_last_numbers(line, 4)
                        if len(nums) == 4:
                            for k, v in zip(["p", "r", "f", "s"], nums):
                                accumulator[avg][k].append(v)

        def safe_mean(lst: list) -> float:
            return sum(lst) / len(lst) if lst else 0.0

        output = [f"{'':>12} {'precision':>9} {'recall':>9} {'f1-score':>9} {'support':>9}"]
        for cls in CLASS_NAMES:
            output.append(
                f"{cls:>12} {safe_mean(accumulator[cls]['p']):>9.2f} "
                f"{safe_mean(accumulator[cls]['r']):>9.2f} "
                f"{safe_mean(accumulator[cls]['f']):>9.2f} "
                f"{round(safe_mean(accumulator[cls]['s'])):>9}"
            )

        output.append("")
        output.append(
            f"{'accuracy':>12} {safe_mean(accumulator['accuracy']['acc']):>30.2f} "
            f"{round(safe_mean(accumulator['accuracy']['s'])):>9}"
        )

        for avg in ["macro avg", "weighted avg"]:
            output.append(
                f"{avg:>12} {safe_mean(accumulator[avg]['p']):>9.2f} "
                f"{safe_mean(accumulator[avg]['r']):>9.2f} "
                f"{safe_mean(accumulator[avg]['f']):>9.2f} "
                f"{round(safe_mean(accumulator[avg]['s'])):>9}"
            )

        return "\n".join(output)