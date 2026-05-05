"""
Treinamento de modelos com validação cruzada.
"""
from typing import Any
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from config.settings import METRIC_SCORING_MAP, SCORING_PIPELINE_MAP
from models.model_config import ModelConfig


class Trainer:
    """Orquestra o treinamento e a busca de hiperparâmetros."""

    def __init__(self, metric_focus: str) -> None:
        """
        Inicializa o treinador.

        Args:
            metric_focus: Métrica alvo para otimização (ex: 'f1_score', 'recall').
        """
        self.metric_focus = metric_focus
        self.param_grid = ModelConfig.get_param_grid()
        self.refit_metric = METRIC_SCORING_MAP[metric_focus] # Metrica que o treinamento irá tentar achar o melhor modelo
        self.scoring = SCORING_PIPELINE_MAP # Metricas usadas no GridSearch

    def _create_base_pipeline(self) -> Pipeline:
        """
        Cria o pipeline base. Os passos são sobrescritos dinamicamente pelo GridSearch.

        Returns:
            Pipeline configurado com placeholders.
        """
        return Pipeline([
            ("scaler", StandardScaler()),
            ("reducao", PCA()),
            ("clf", SVC())
        ])

    def train(self, X_train: np.ndarray, y_train: np.ndarray) -> Any:
        """
        Executa o GridSearchCV nos dados de treino.

        Args:
            X_train: Features do conjunto de treino.
            y_train: Labels do conjunto de treino.

        Returns:
            Objeto GridSearchCV treinado.
        """
        pipeline = self._create_base_pipeline()
        grid = GridSearchCV(
            estimator=pipeline,
            param_grid=self.param_grid,
            cv=5,
            n_jobs=-2,
            scoring=self.scoring,
            refit=self.refit_metric,
            verbose=2,
        )
        grid.fit(X_train, y_train)
        return grid