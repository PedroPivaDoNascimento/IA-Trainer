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


class ModelConfig:
    """Gerencia a configuração dos classificadores e pré-processadores."""

    @staticmethod
    def get_scalers() -> List[Any]:
        """Retorna lista de escaladores disponíveis para o pipeline."""
        return [
            StandardScaler(),
            RobustScaler(),
            MinMaxScaler(),
            MaxAbsScaler(),
            QuantileTransformer(output_distribution="uniform", random_state=42),
            QuantileTransformer(output_distribution="normal", random_state=42),
            PowerTransformer(method="yeo-johnson"),
            Normalizer(norm="l2"),
            None, 
        ]

    @staticmethod
    def get_param_grid() -> List[Dict[str, Any]]:
        """
        Define a grade de parâmetros para o GridSearchCV.

        Returns:
            Lista de dicionários compatíveis com `param_grid` do scikit-learn.
        """
        scalers = ModelConfig.get_scalers()
        reducoes = ["passthrough"]
        # Exemplo de redução: PCA(n_components=n)

        return [
            {
                "clf": [Perceptron(random_state=42, class_weight="balanced")],
                "clf__eta0": [0.1, 0.01, 1.0],
                "clf__penalty": ["l2", "l1", "elasticnet"],
                "scaler": scalers,
                "reducao": ["passthrough"],
            },
            {
                "scaler": [StandardScaler(), MinMaxScaler(), RobustScaler()],
                "reducao": reducoes,
                "clf": [MLPClassifier(random_state=31, solver="adam")],
                "clf__hidden_layer_sizes": [(32,), (64,), (128,)],
                "clf__activation": ["relu", "tanh"],
                "clf__alpha": [0.0001, 0.001, 0.01],
                "clf__learning_rate_init": [0.001, 0.01],
                "clf__early_stopping": [True],
                "clf__validation_fraction": [0.1],
                "clf__max_iter": [1000],
            },
            {
                "clf": [SVC(random_state=42, class_weight="balanced")],
                "clf__C": [0.1, 1, 5, 10, 50, 100],
                "clf__kernel": ["rbf", "poly"],
                "clf__gamma": ["scale", "auto"],
                "scaler": scalers,
                "reducao": reducoes,
            },
            {
                "clf": [LinearSVC(random_state=42, class_weight="balanced")],
                "clf__max_iter": [1000, 2000],
                "clf__C": [0.1, 1, 5, 10, 50, 100],
                "clf__dual": [False],
                "scaler": scalers,
                "reducao": reducoes,
            },
            {
                "clf": [RandomForestClassifier(random_state=42, class_weight="balanced")],
                "clf__n_estimators": [100, 300, 500],
                "clf__max_depth": [None, 10, 20],
                "clf__criterion": ["gini", "entropy"],
                "scaler": [None],
                "reducao": ["passthrough"],
            },
            {
                "clf": [ExtraTreesClassifier(random_state=42, class_weight="balanced")],
                "clf__n_estimators": [100, 300],
                "clf__max_depth": [None, 10, 20],
                "clf__criterion": ["gini", "entropy"],
                "scaler": [None],
                "reducao": ["passthrough"],
            },
            {
                "clf": [GradientBoostingClassifier(random_state=42)],
                "clf__n_estimators": [100, 200],
                "clf__learning_rate": [0.05, 0.1, 0.2],
                "clf__max_depth": [3, 5],
                "scaler": [None],
                "reducao": ["passthrough"],
            },
            {
                "clf": [KNeighborsClassifier()],
                "clf__n_neighbors": [1, 3, 5, 7, 9, 11],
                "clf__weights": ["uniform", "distance"],
                "clf__metric": ["euclidean", "manhattan"],
                "scaler": scalers,
                "reducao": reducoes,
            },
            {
                "clf": [LogisticRegression(random_state=42, class_weight="balanced", max_iter=1000)],
                "clf__C": [0.01, 0.1, 1, 5, 10, 50, 100],
                "clf__solver": ["liblinear", "lbfgs"],
                "scaler": scalers,
                "reducao": reducoes,
            },
            {
                "clf": [RidgeClassifier(class_weight="balanced")],
                "clf__alpha": [0.1, 1.0, 10.0, 100.0],
                "scaler": scalers,
                "reducao": ["passthrough"],
            },
        ]