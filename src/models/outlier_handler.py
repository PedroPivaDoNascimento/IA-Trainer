"""
Pré-processamento para remoção de outliers nas colunas numéricas dos dados de treino.

Implementação do Método de Tukey (regra do IQR):
    1. IQR = Q³ - Q¹
    2. margem = 1.5 * IQR
    3. limite inferior = Q¹ - margem | limite superior = Q³ + margem
    4. São outliers os valores fora do intervalo [limite inferior, limite superior]

Regra de aplicação: o cálculo é feito coluna a coluna; se uma linha apresentar
valor outlier em qualquer coluna aplicável, a linha inteira é removida da base
destinada ao treinamento.
"""
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd


class TukeyOutlierRemover:
    """
    Estratégia de remoção de outliers baseada no Método de Tukey (regra do IQR).

    Responsabilidade única (SRP): apenas calcular limites por IQR e identificar
    linhas outlier. Não conhece o fluxo de treinamento nem a origem dos dados,
    podendo ser substituída por outra estratégia que respeite a mesma interface
    (Open/Closed e Liskov, via Duck Typing/Protocol).
    """

    def __init__(self, factor: float = 1.5) -> None:
        """
        Args:
            factor: Multiplicador da regra do IQR (1.5 = padrão de Tukey).
        """
        self.factor = factor

    def compute_bounds(self, serie: pd.Series) -> Tuple[float, float]:
        """
        Calcula os limites inferior e superior pelo método de Tukey para uma coluna.

        Args:
            serie: Série numérica correspondente a uma coluna do DataFrame.

        Returns:
            Tupla (limite_inferior, limite_superior).
        """
        q1 = serie.quantile(0.25)
        q3 = serie.quantile(0.75)
        iqr = q3 - q1
        margem = self.factor * iqr
        return q1 - margem, q3 + margem

    def get_numeric_columns(self, X: pd.DataFrame) -> List[str]:
        """Retorna apenas as colunas numéricas (colunas aplicáveis à regra de Tukey)."""
        return list(X.select_dtypes(include=np.number).columns)

    def find_outliers(self, X: pd.DataFrame) -> pd.Series:
        """
        Identifica as linhas que contêm ao menos um valor outlier em qualquer
        coluna numérica aplicável.

        Args:
            X: DataFrame de features.

        Returns:
            Série booleana (índice alinhado a X): True para linhas com outlier.
        """
        outlier_mask = pd.Series(False, index=X.index)
        for col in self.get_numeric_columns(X):
            limite_inferior, limite_superior = self.compute_bounds(X[col])
            values = X[col]
            # NaN não é considerado outlier: a regra se aplica apenas a valores
            # efetivamente fora dos limites.
            is_outlier = (values < limite_inferior) | (values > limite_superior)
            outlier_mask |= is_outlier.fillna(False)
        return outlier_mask

    def summarize_columns(self, X: pd.DataFrame) -> pd.DataFrame:
        """
        Gera um resumo por coluna numérica com Q1, Q3, IQR, margem, limites
        inferior/superior e a contagem de outliers detectados.

        Args:
            X: DataFrame de features.

        Returns:
            DataFrame de resumo (uma linha por coluna numérica).
        """
        bounds_info: Dict[str, Dict[str, float]] = {}
        for col in self.get_numeric_columns(X):
            q1 = X[col].quantile(0.25)
            q3 = X[col].quantile(0.75)
            iqr = q3 - q1
            margem = self.factor * iqr
            limite_inferior = q1 - margem
            limite_superior = q3 + margem
            is_outlier = ((X[col] < limite_inferior) | (X[col] > limite_superior)).fillna(False)

            bounds_info[col] = {
                "Q1": q1,
                "Q3": q3,
                "IQR": iqr,
                "Margem": margem,
                "Limite_Inferior": limite_inferior,
                "Limite_Superior": limite_superior,
                "Outliers": int(is_outlier.sum()),
            }

        info_df = pd.DataFrame.from_dict(bounds_info, orient="index")
        info_df.index.name = "Coluna"
        return info_df

    def remove_outliers(self, X: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series, pd.DataFrame]:
        """
        Remove do DataFrame as linhas que possuam outlier em qualquer coluna numérica.

        Args:
            X: DataFrame de features.

        Returns:
            Tupla (X_limpo, mascara_outlier, resumo_por_coluna).
        """
        outlier_mask = self.find_outliers(X)
        resumo = self.summarize_columns(X)
        return X.loc[~outlier_mask], outlier_mask, resumo


def remove_outliers_tukey(
    X: pd.DataFrame,
    y: Optional[np.ndarray] = None,
    factor: float = 1.5,
    verbose: bool = True,
) -> Tuple[pd.DataFrame, Optional[np.ndarray]]:
    """
    Função de alto nível (facade) para a etapa de pré-processamento: aplica o
    Método de Tukey às colunas numéricas e remove inteiramente as linhas que
    apresentarem outlier em qualquer coluna, mantendo X e y alinhados.

    Args:
        X: DataFrame de features destinado ao treinamento.
        y: Vetor de labels correspondente (opcional); filtrado com as mesmas linhas.
        factor: Multiplicador da regra do IQR (padrão 1.5, conforme Tukey).
        verbose: Se True, imprime um resumo da remoção realizada.

    Returns:
        Tupla (X_filtrado, y_filtrado).
    """
    remover = TukeyOutlierRemover(factor=factor)
    total_antes = len(X)
    X_limpo, outlier_mask, info_df = remover.remove_outliers(X)

    # Mantém X e y alinhados: remove as mesmas linhas do vetor de labels.
    y_limpo = y
    if y is not None:
        y_limpo = np.asarray(y)[~outlier_mask.to_numpy()]

    if verbose:
        removidas = total_antes - len(X_limpo)
        percentual = (removidas / total_antes * 100) if total_antes else 0.0
        print(f"[Outliers/Tukey] Linhas removidas: {removidas} de {total_antes} ({percentual:.2f}%)")
        if removidas > 0:
            print(info_df.to_string())

    return X_limpo, y_limpo
