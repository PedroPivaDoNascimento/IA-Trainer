"""
Manipulação de dados: carregamento, preparação e divisão treino/teste.
"""
from typing import Tuple
import numpy as np
from sklearn.model_selection import train_test_split
from .excel_geter import preparar_dados_para_treino
import pandas as pd
from typing import Any
from sklearn.inspection import permutation_importance


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
        self, test_size: float = 0.2, random_state: int = 67, X: np.ndarray = None, y: np.ndarray = None
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Carrega os dados do Excel e realiza a divisão estratificada.

        Args:
            test_size: Proporção do conjunto de teste.
            random_state: Semente para reprodutibilidade.

        Returns:
            Tupla contendo (X_train, X_test, y_train, y_test).
        """
        return train_test_split(
            X, y, test_size=test_size, random_state=random_state, stratify=y
        )
    
    def load_and_split_analysis(
        self, test_size: float = 0.2, random_state: int = 67, X: pd.DataFrame = None, y: np.ndarray = None
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
    
    
    def __calcular_ratio_variancia(X_data, y_data):
        """
        Calcula a razão de variância (Interclasse / Intraclasse).

        Valores muito baixos indicam alta variação interna sem separabilidade de labels
        e valores muito altos é alta variação externa.
        """
        ratios = {}
        for col in X_data.columns:
            # Agrupando por label para calcular as métricas por classe
            grouped = X_data[col].groupby(y_data)
            means = grouped.mean()
            variances = grouped.var()
            
            var_inter = np.var(means)       # Variância entre as médias das classes
            mean_var_intra = np.mean(variances)  # Média das variâncias internas das classes
            
            # Evita divisão por zero se a variância intraclasse for nula
            ratios[col] = var_inter / (mean_var_intra + 1e-9)
            
        return ratios
    
    def __classificar_feature(row):
        # Threshold estatístico: Se a variância interclasse for menor que 1% da intraclasse
        if row['Variance_Ratio'] < 0.01:
            return "Prejudicial (Ruído Intraclasse)"
        elif row['Importance_Drop'] > 0.01:
            return "Importante (Mantém)"
        else:
            return "Neutra (Pode remover)"
    
    def make_permutation_importance(self, model: Any, X_val: np.ndarray, y_val: np.ndarray, feature_names: list) -> pd.DataFrame:
        """
        Aplica Permutation Importance para avaliar a importância das features.

        Args:
            model: Modelo treinado.
            X_val: Conjunto de validação (features).
            y_val: Conjunto de validação (labels).

        Returns:
            DataFrame com a importância das features.
        """

        # Calculamos o ratio com base nos dados de treino
        variance_ratios = self.__calcular_ratio_variancia(X_val, y_val)

        result = permutation_importance(model, X_val, y_val, n_repeats=10, random_state=42)

        # Organizando os resultados iniciais
        importance_df = pd.DataFrame({
            'Feature': feature_names,
            'Importance_Drop': result.importances_mean,
            'Variance_Ratio': [variance_ratios[f] for f in feature_names]
        })

        importance_df['Classificacao'] = importance_df.apply(self.__classificar_feature, axis=1)
        importance_df = importance_df.sort_values(by='Importance_Drop', ascending=False)

        return importance_df