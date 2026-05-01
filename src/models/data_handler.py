"""
Manipulação de dados: carregamento, preparação e divisão treino/teste.
"""
from typing import Tuple
import numpy as np
from sklearn.model_selection import train_test_split
from .excel_geter import preparar_dados_para_treino


class DataHandler:
    """Gerencia o carregamento e a divisão estratificada dos dados."""

    def __init__(self, data_path: str, results_path: str) -> None:
        """
        Inicializa o manipulador de dados.

        Args:
            data_path: Caminho para o arquivo Excel com features.
            results_path: Caminho para o arquivo Excel com labels.
        """
        self.data_path = data_path
        self.results_path = results_path

    def load_and_split(
        self, test_size: float = 0.2, random_state: int = 67
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Carrega os dados do Excel e realiza a divisão estratificada.

        Args:
            test_size: Proporção do conjunto de teste.
            random_state: Semente para reprodutibilidade.

        Returns:
            Tupla contendo (X_train, X_test, y_train, y_test).
        """
        X, y = preparar_dados_para_treino(self.data_path, self.results_path)
        return train_test_split(
            X, y, test_size=test_size, random_state=random_state, stratify=y
        )