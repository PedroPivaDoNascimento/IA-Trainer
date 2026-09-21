"""
Configuração de modelos de regressão, escaladores e grade de parâmetros.
"""
from typing import List, Dict, Any
from sklearn.preprocessing import (
    StandardScaler, RobustScaler, MinMaxScaler, MaxAbsScaler,
    QuantileTransformer, Normalizer, PowerTransformer
)
from sklearn.svm import SVR, LinearSVR, NuSVR
from sklearn.ensemble import (
    RandomForestRegressor, GradientBoostingRegressor, ExtraTreesRegressor
)
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import (
    LinearRegression, Ridge, Lasso, ElasticNet, SGDRegressor
)
from sklearn.neural_network import MLPRegressor
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.decomposition import PCA


class ModelConfig:
    """Gerencia a configuração dos regressores e pré-processadores."""

    @staticmethod
    def get_scalers() -> List[Any]:
        """Retorna lista de escaladores disponíveis para o pipeline."""
        return [
            StandardScaler(),
            #StandardScaler(with_mean=False, with_std=True),
            #StandardScaler(with_mean=True, with_std=False),
            #StandardScaler(with_mean=False, with_std=False),
            #StandardScaler(with_mean=True, with_std=True),
            #RobustScaler(),
            #RobustScaler(quantile_range=(20, 80)),
            #RobustScaler(quantile_range=(10, 90)),
            #RobustScaler(quantile_range=(30, 70)),
            #MinMaxScaler(),
            #MaxAbsScaler(),
            #QuantileTransformer(output_distribution="uniform", random_state=42),
            #QuantileTransformer(output_distribution="normal", random_state=42),
            #PowerTransformer(method="yeo-johnson"),
            #Normalizer(norm="l2"),
            #None,
        
        ]   

    @staticmethod
    def get_reducoes() -> List[Any]:
        """Retorna lista de reduções disponíveis para o pipeline."""
        return [
            "passthrough",
            #PCA(n_components=0.90, random_state=31),
            #PCA(n_components=0.95, random_state=31),
            #PCA(n_components=0.97, random_state=31),
            #PCA(n_components=0.98, random_state=31),
            #PCA(n_components=0.99, random_state=31),
            #SelectKBest(score_func=f_regression, k="all")
        ]

    @staticmethod
    def get_param_grid() -> List[Dict[str, Any]]:
        """
        Define a grade de parâmetros para o GridSearchCV.

        Returns:
            Lista de dicionários compatíveis com `param_grid` do scikit-learn.
        """
        scalers = ModelConfig.get_scalers()
        reducoes = ModelConfig.get_reducoes()

        return [
            #{
            #    "clf": [SVR()],
            #    "clf__C": [105, 110],
            #    "clf__kernel": ["rbf", "poly", "sigmoid", "linear"],
            #    "clf__gamma": ["scale", "auto"],
            #    "scaler": scalers,
            #    "reducao": reducoes,
            #},
            #{
            #    "clf": [RandomForestRegressor(random_state=42)],
            #    "clf__n_estimators": [145],
            #    "clf__max_depth": [None],
            #    "clf__min_samples_split": [5],
            #    "clf__criterion": ["squared_error"],
            #    "clf__ccp_alpha": [0.01],
            #    "scaler": [None],
            #    "reducao": ["passthrough"],
            #},
            #{
            #    "clf": [ExtraTreesRegressor(random_state=42)],
            #    "clf__n_estimators": [300],
            #    "clf__max_depth": [10],
            #    "clf__criterion": ["absolute_error"],
            #    "clf__min_samples_split": [7],
            #    "scaler": [None],
            #    "reducao": ["passthrough"],
            #},
            #{
            #    "clf": [GradientBoostingRegressor(random_state=42)],
            #    "clf__n_estimators": [125],
            #    "clf__learning_rate": [0.125],
            #    "clf__max_depth": [4],
            #    "clf__loss": ["absolute_error"],
            #    "scaler": [None],
            #    "reducao": ["passthrough"],
            #},
            #{
            #     "clf": [KNeighborsRegressor()],
            #     "clf__n_neighbors": [7],
            #     "clf__weights": ["distance"],
            #     "clf__metric": ["manhattan"],
            #     "scaler": scalers,
            #     "reducao": reducoes,
            #},
            #{
            #    "clf": [LinearRegression()],
            #    #"clf__fit_intercept": [True, False],
            #    #"clf__positive": [False, True],
            #    "scaler": scalers,
            #    "reducao": reducoes,
            #},
            #{
            #    "clf": [Ridge()],
            #    "clf__alpha": [0.3],
            #    #"clf__solver": ["auto", "svd", "cholesky", "lsqr", "saga"],
            #    #"clf__tol": [5.5e-4, 6e-4, 7e-4, 8e-4, 9e-4],
            #    #"clf__fit_intercept": [True, False],
            #    "scaler": scalers,
            #    "reducao": reducoes,
            #},
            #{
            #    "clf": [Lasso(random_state=42)],
            #    "clf__alpha": [0.01, 0.1, 0.2, 1.0, 10.0],
            #    "scaler": scalers,
            #    "reducao": ["passthrough"],
            #},
            #{
            #    "clf": [ElasticNet(random_state=42)],
            #    # Força total da penalidade (escala logarítmica recomendada)
            #    "clf__alpha": [0.001, 0.01, 0.1, 0.5 ,1.0, 10.0],
            #    # Proporção entre L1 (Lasso) e L2 (Ridge)
            #    "clf__l1_ratio": [0.1, 0.3, 0.5, 0.65, 0.7, 0.9],
            #    # Algoritmo de otimização (assim como no Lasso)
            #    "clf__selection": ["cyclic", "random"],
            #    # Tolerância de convergência e máximo de iterações
            #    "clf__tol": [1e-4, 1e-3],
            #    "clf__max_iter": [2000, 5000],
            #    # Cálculo do intercepto
            #    "clf__fit_intercept": [True, False],
            #    # Pré-processadores do seu pipeline
            #    "scaler": scalers,
            #    "reducao": reducoes,
            #},
        ]