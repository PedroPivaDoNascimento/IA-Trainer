"""
Configuração de modelos, escaladores e grade de parâmetros.
"""
from typing import List, Dict, Any
from sklearn.preprocessing import (
    StandardScaler, RobustScaler, MinMaxScaler, MaxAbsScaler,
    QuantileTransformer, Normalizer, PowerTransformer
)
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import (
    RandomForestClassifier, GradientBoostingClassifier, ExtraTreesClassifier
)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression, Perceptron, RidgeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.decomposition import PCA


class ModelConfig:
    """Gerencia a configuração dos classificadores e pré-processadores."""

    @staticmethod
    def get_scalers() -> List[Any]:
        """Retorna lista de escaladores disponíveis para o pipeline."""
        return [
            #StandardScaler(),
            #RobustScaler(),
            #MinMaxScaler(),
            #MaxAbsScaler(),
            #QuantileTransformer(output_distribution="uniform", random_state=42),
            #QuantileTransformer(output_distribution="normal", random_state=42),
            #PowerTransformer(method="yeo-johnson"),
            #Normalizer(norm="l2"),
            #None,

            RobustScaler(),
            RobustScaler(quantile_range=(20, 80)),
            #RobustScaler(quantile_range=(10, 90)),
            #RobustScaler(quantile_range=(30, 70)),
            StandardScaler(),
        ]   

    @staticmethod
    def get_reducoes() -> List[Any]:
        """Retorna lista de reduções disponíveis para o pipeline."""
        return [
            "passthrough",
            #PCA(n_components=0.95, random_state=31),
            PCA(n_components=0.99, random_state=31),
            SelectKBest(score_func=f_classif, k="all")
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
            #    "clf": [Perceptron(random_state=42, class_weight="balanced")],
            #    "clf__eta0": [0.1, 0.01, 1.0],
            #    "clf__penalty": ["l2", "l1", "elasticnet"],
            #    "scaler": scalers,
            #    "reducao": ["passthrough"],
            #},
            {
                "scaler": scalers,
                "reducao": reducoes,
                "clf": [MLPClassifier(random_state=31)],
                "clf__activation": [
                    "tanh",
                    "relu"
                ],


                "clf__hidden_layer_sizes": [
                    (24,),
                    (32,),
                    (40,),
                    #(48,),
                    #(24, 12),
                    #(32, 16)
                ],

                "clf__alpha": [
                    0.00005,
                    0.0001,
                    0.0002,
                    #0.0005,
                    #0.01
                ],

                "clf__learning_rate_init": [
                    #0.005,
                    0.0075,
                    0.01,
                    0.015,
                    #0.1
                ],

                "clf__early_stopping": [True],
                "clf__validation_fraction": [
                    0.08, 
                    0.10, 
                    0.12, 
                    #0.15
                ],

                "clf__max_iter": [
                    500,
                    1000,
                    1500
                ],

                "clf__n_iter_no_change": [
                    10, 
                    15, 
                    20
                ],

                "clf__tol": [
                    0.0001, 
                    0.00005
                ]
            },

            #{
            #    "clf": [SVC(random_state=42, class_weight="balanced")],
            #    "clf__C": [0.1, 1, 5, 10, 50, 100],
            #    "clf__kernel": ["rbf", "poly"],
            #    "clf__gamma": ["scale", "auto"],
            #    "scaler": scalers,
            #    "reducao": reducoes,
            #},
            #{
            #    "clf": [LinearSVC(random_state=42, class_weight="balanced")],
            #    "clf__max_iter": [1000, 2000],
            #    "clf__C": [0.1, 1, 5, 10, 50, 100],
            #    "clf__dual": [False],
            #    "scaler": scalers,
            #    "reducao": reducoes,
            #},
            #{
            #    "clf": [RandomForestClassifier(random_state=42, class_weight="balanced")],
            #    "clf__n_estimators": [100, 300, 500],
            #    "clf__max_depth": [None, 10, 20],
            #    "clf__criterion": ["gini", "entropy"],
            #    "scaler": [None],
            #    "reducao": ["passthrough"],
            #},
            #{
            #    "clf": [ExtraTreesClassifier(random_state=42, class_weight="balanced")],
            #    "clf__n_estimators": [100, 300],
            #    "clf__max_depth": [None, 10, 20],
            #    "clf__criterion": ["gini", "entropy"],
            #    "scaler": [None],
            #    "reducao": ["passthrough"],
            #},
            #{
            #    "clf": [GradientBoostingClassifier(random_state=42)],
            #    "clf__n_estimators": [100, 200],
            #    "clf__learning_rate": [0.05, 0.1, 0.2],
            #    "clf__max_depth": [3, 5],
            #    "scaler": [None],
            #    "reducao": ["passthrough"],
            #},
            #{
            #    "clf": [KNeighborsClassifier()],
            #    "clf__n_neighbors": [1, 3, 5, 7, 9, 11],
            #    "clf__weights": ["uniform", "distance"],
            #    "clf__metric": ["euclidean", "manhattan"],
            #    "scaler": scalers,
            #    "reducao": reducoes,
            #},
            #{
            #    "clf": [LogisticRegression(random_state=42, class_weight="balanced", max_iter=1000)],
            #    "clf__C": [0.01, 0.1, 1, 5, 10, 50, 100],
            #    "clf__solver": ["liblinear", "lbfgs"],
            #    "scaler": scalers,
            #    "reducao": reducoes,
            #},
            #{
            #    "clf": [RidgeClassifier(class_weight="balanced")],
            #    "clf__alpha": [0.1, 1.0, 10.0, 100.0],
            #    "scaler": scalers,
            #    "reducao": ["passthrough"],
            #},
        ]