import numpy as np
from models.data_handler import DataHandler
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import pandas as pd

class DataReport:
    def __init__(self, X: np.ndarray, y: np.ndarray, data_handler: DataHandler) -> None:
        self.data_handler = data_handler
        self.X = X
        self.y = y
    def generate_report_balenceamento(self) -> None:
        """Gera um relatório de balanceamento das classes."""
        unique, counts = np.unique(self.y, return_counts=True)
        plt.bar(unique, counts)
        plt.xlabel('Classes')
        plt.ylabel('Contagem')
        plt.title('Balanceamento das Classes')
        plt.xticks(unique)
        plt.show()

    def generate_report_importance(self, importance_df: pd.DataFrame) -> None:
        plt.figure(figsize=(10, 6))
        # Mapeamento de cores baseado na nova classificação
        color_map = {
            "Importante (Mantém)": "green",
            "Neutra (Pode remover)": "gray",
            "Prejudicial (Remove)": "red"
        }
        colors = [color_map[crit] for crit in importance_df['Classificacao']]
        bars = plt.barh(importance_df['Feature'], importance_df['Importance_Drop'], color=colors)
        plt.axvline(x=0, color='black', linestyle='--')

        # Adicionando legenda
        legend_elements = [Patch(facecolor=color, label=label) for label, color in color_map.items()]
        plt.legend(handles=legend_elements, loc='lower right')

        plt.title('Impacto da Feature vs. Comportamento Estatístico')
        plt.xlabel('Queda na Acurácia se a Feature for Removida (Permutation Importance)')
        plt.ylabel('Features')
        plt.gca().invert_yaxis()  # Mantém a maior queda (mais importante) no topo
        plt.grid(axis='x', linestyle=':', alpha=0.6)
        plt.tight_layout()
        plt.show()

