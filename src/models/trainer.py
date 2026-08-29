"""
Treinamento de modelos com validação cruzada para REGRESSÃO.
"""
from typing import Any
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV, KFold  # 1. Trocado StratifiedKFold por KFold
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVR  # 2. Trocado SVC por SVR (Regressor)
from config.settings import METRIC_SCORING_MAP, SCORING_PIPELINE_MAP
from models.model_config import ModelConfig


class Trainer:
    """Orquestra o treinamento e a busca de hiperparâmetros para modelos de regressão."""

    def __init__(self, metric_focus: str, dict_params: dict = None) -> None:
        """
        Inicializa o treinador.

        Args:
            metric_focus: Métrica alvo para otimização (ex: 'r2', 'mae', 'mse').
        """
        self.metric_focus = metric_focus
        self.param_grid = dict_params if dict_params is not None else ModelConfig.get_param_grid()        
        self.refit_metric = METRIC_SCORING_MAP[metric_focus] # Métrica principal (ex: 'r2' ou 'neg_mean_squared_error')
        self.scoring = SCORING_PIPELINE_MAP # Dicionário com métricas válidas de regressão
        self.random_state = 31

    def _create_base_pipeline(self) -> Pipeline:
        """
        Cria o pipeline base. Os passos são sobrescritos dinamicamente pelo GridSearch.

        Returns:
            Pipeline configurado com placeholders.
        """
        return Pipeline([
            ("scaler", StandardScaler()),
            ("reducao", PCA()),
            ("clf", SVR())  
        ])

    def train(self, X_train: np.ndarray, y_train: np.ndarray, random_state: int = 67) -> Any:
        """
        Executa o GridSearchCV nos dados de treino.

        Args:
            X_train: Features do conjunto de treino.
            y_train: Labels/Valores contínuos do conjunto de treino.

        Returns:
            Objeto GridSearchCV treinado.
        """
        pipeline = self._create_base_pipeline()

        cv = KFold(
            n_splits=5,
            shuffle=True,
            random_state=random_state
        )

        grid = GridSearchCV(
            estimator=pipeline,
            param_grid=self.param_grid,
            cv=cv,
            n_jobs=-2,
            scoring=self.scoring,
            refit=self.refit_metric,
            #verbose=2,
        )
        grid.fit(X_train, y_train)
        return grid