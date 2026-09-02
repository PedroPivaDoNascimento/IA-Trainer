"""
Configuração de modelos de regressão, escaladores e grade de parâmetros.
"""
from typing import List, Dict, Any
from sklearn.preprocessing import (
    StandardScaler, RobustScaler, MinMaxScaler, MaxAbsScaler,
    QuantileTransformer, Normalizer, PowerTransformer
)
from sklearn.svm import SVR, LinearSVR
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
            RobustScaler(),
            MinMaxScaler(),
            MaxAbsScaler(),
            QuantileTransformer(output_distribution="uniform", random_state=42),
            #QuantileTransformer(output_distribution="normal", random_state=42),
            PowerTransformer(method="yeo-johnson"),
            Normalizer(norm="l2"),
            None,

            #RobustScaler(),
            ##RobustScaler(quantile_range=(20, 80)),
            ##RobustScaler(quantile_range=(10, 90)),
            ##RobustScaler(quantile_range=(30, 70)),
            #StandardScaler(),
        ]   

    @staticmethod
    def get_reducoes() -> List[Any]:
        """Retorna lista de reduções disponíveis para o pipeline."""
        return [
            "passthrough",
            PCA(n_components=0.95, random_state=31),
            PCA(n_components=0.99, random_state=31),
            SelectKBest(score_func=f_regression, k="all")
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
            #    "clf__C": [0.1, 1, 5, 10, 50, 100],
            #    "clf__kernel": ["rbf", "poly"],
            #    "clf__gamma": ["scale", "auto"],
            #    "scaler": scalers,
            #    "reducao": reducoes,
            #},
            #{
            #    "clf": [LinearSVR(random_state=42)],
            #    "clf__max_iter": [1000, 2000],
            #    "clf__C": [0.1, 1, 5, 10, 50, 100],
            #    "scaler": scalers,
            #    "reducao": reducoes,
            #},
            #{
            #    "clf": [RandomForestRegressor(random_state=42)],
            #    "clf__n_estimators": [100, 300, 500],
            #    "clf__max_depth": [None, 10, 20],
            #    "clf__criterion": ["squared_error", "absolute_error"],
            #    "scaler": [None],
            #    "reducao": ["passthrough"],
            #},
            #{
            #    "clf": [ExtraTreesRegressor(random_state=42)],
            #    "clf__n_estimators": [100, 300],
            #    "clf__max_depth": [None, 10, 20],
            #    "clf__criterion": ["squared_error", "absolute_error"],
            #    "scaler": [None],
            #    "reducao": ["passthrough"],
            #},
            #{
            #    "clf": [GradientBoostingRegressor(random_state=42)],
            #    "clf__n_estimators": [100, 200],
            #    "clf__learning_rate": [0.05, 0.1, 0.2],
            #    "clf__max_depth": [3, 5],
            #    "scaler": [None],
            #    "reducao": ["passthrough"],
            #},
            #{
            #     "clf": [KNeighborsRegressor()],
            #     "clf__n_neighbors": [3, 5, 7, 9, 11, 13, 15, 17, 19],
            #     "clf__weights": ["uniform", "distance"],
            #     "clf__metric": ["euclidean", "manhattan"],
            #     "scaler": scalers,
            #     "reducao": reducoes,
            #},
            {
                "clf": [LinearRegression()],
                "scaler": scalers,
                "reducao": reducoes,
            },
            #{
            #    "clf": [Ridge()],
            #    "clf__alpha": [0.01, 0.1],
            #    "scaler": scalers,
            #    "reducao": reducoes,
            #},
            #{
            #    "clf": [Lasso(random_state=42)],
            #    "clf__alpha": [0.01, 0.1, 1.0, 10.0],
            #    "scaler": scalers,
            #    "reducao": ["passthrough"],
            #},
        ]