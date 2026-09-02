"""
Visualizações avançadas para análise de modelos de Machine Learning (Regressão).
Inclui comparações de importância de features, plots 2D, gráficos de resíduos e diagnósticos.
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from typing import Tuple, List, Dict, Any


class AdvancedVisualizations:
    """Classe responsável por gerar visualizações avançadas de análise de modelos de regressão."""

    @staticmethod
    def plot_regression_diagnostics(
        y_true: np.ndarray,
        y_pred: np.ndarray,
        dataset_name: str = "Dataset"
    ) -> None:
        """
        Plota diagnósticos básicos de regressão:
        1. Predito vs. Real
        2. Resíduos vs. Predito (para checar heterocedasticidade e padrões)

        Args:
            y_true: Array com os valores reais.
            y_pred: Array com os valores previstos.
            dataset_name: Nome do dataset para o título.
        """
        residuos = y_true - y_pred

        fig, axes = plt.subplots(1, 2, figsize=(14, 5))

        # 1. Valores Reais vs. Preditos
        axes[0].scatter(y_true, y_pred, alpha=0.6, color='crimson', edgecolors='k')
        
        # Linha de identidade (perfeição)
        min_val = min(np.min(y_true), np.min(y_pred))
        max_val = max(np.max(y_true), np.max(y_pred))
        axes[0].plot([min_val, max_val], [min_val, max_val], 'k--', lw=2, label='Ideal (y = y_pred)')
        
        axes[0].set_xlabel('Valor Real', fontsize=11)
        axes[0].set_ylabel('Valor Predito', fontsize=11)
        axes[0].set_title('Valores Reais vs. Preditos', fontsize=12, fontweight='bold')
        axes[0].legend(loc='best')
        axes[0].grid(True, linestyle=':', alpha=0.6)

        # 2. Resíduos vs. Predito
        axes[1].scatter(y_pred, residuos, alpha=0.6, color='purple', edgecolors='k')
        axes[1].axhline(y=0, color='black', linestyle='--', lw=2)
        axes[1].set_xlabel('Valor Predito', fontsize=11)
        axes[1].set_ylabel('Resíduo (Real - Predito)', fontsize=11)
        axes[1].set_title('Gráfico de Resíduos', fontsize=12, fontweight='bold')
        axes[1].grid(True, linestyle=':', alpha=0.6)

        plt.suptitle(f'Diagnóstico de Regressão - {dataset_name}', fontsize=14, fontweight='bold', y=1.02)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_feature_importance_comparison(
        permutation_importance_df: pd.DataFrame,
        tree_feature_importances: np.ndarray,
        linear_coefficients: np.ndarray,
        feature_names: List[str],
        dataset_name: str = "Dataset"
    ) -> None:
        """
        Plota 3 gráficos de barras horizontais comparando a importância das features
        pelos métodos: Permutation Importance, Modelo Baseado em Árvore (ex: RandomForestRegressor)
        e Modelo Linear (ex: Regressão Linear/Ridge/Lasso).

        Args:
            permutation_importance_df: DataFrame com Permutation Importance.
            tree_feature_importances: Array com importâncias nativas de modelos de árvore.
            linear_coefficients: Array com coeficientes do modelo linear.
            feature_names: Lista de nomes das features.
            dataset_name: Nome do dataset para o título.
        """
        fig, axes = plt.subplots(1, 3, figsize=(18, 6))

        # Permutation Importance (Em Regressão, costuma ser a queda no R2 ou aumento no MSE)
        perm_imp = permutation_importance_df.set_index('Feature')['Importance_Drop']
        perm_imp = perm_imp.reindex(feature_names)
        axes[0].barh(feature_names, perm_imp.values, color='steelblue')
        axes[0].set_xlabel('Métrica de Queda (ex: R² drop)')
        axes[0].set_title('Permutation Importance', fontsize=12, fontweight='bold')
        axes[0].invert_yaxis()
        axes[0].grid(axis='x', linestyle=':', alpha=0.6)

        # Tree-based Feature Importances
        axes[1].barh(feature_names, tree_feature_importances, color='darkorange')
        axes[1].set_xlabel('Importância Relativa')
        axes[1].set_title('Tree-Based Model Native', fontsize=12, fontweight='bold')
        axes[1].invert_yaxis()
        axes[1].grid(axis='x', linestyle=':', alpha=0.6)

        # Linear Model Coefficients (Usa valor absoluto para comparar magnitude)
        abs_coefs = np.abs(linear_coefficients)
        axes[2].barh(feature_names, abs_coefs, color='forestgreen')
        axes[2].set_xlabel('Magnitude Absoluta dos Coeficientes')
        axes[2].set_title('Linear Model Coefficients (|w|)', fontsize=12, fontweight='bold')
        axes[2].invert_yaxis()
        axes[2].grid(axis='x', linestyle=':', alpha=0.6)

        plt.suptitle(f'Comparação de Importância de Features - {dataset_name}', 
                     fontsize=14, fontweight='bold', y=1.02)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def get_top_2_features(
        permutation_importance_df: pd.DataFrame,
        tree_feature_importances: np.ndarray,
        linear_coefficients: np.ndarray,
        feature_names: List[str]
    ) -> Dict[str, Tuple[str, str]]:
        """
        Identifica as 2 features mais importantes de acordo com cada método.

        Returns:
            Dicionário com as top 2 features de cada método.
        """
        # Top 2 Permutation Importance
        perm_top2 = permutation_importance_df.nlargest(2, 'Importance_Drop')['Feature'].tolist()

        # Top 2 Tree Model
        tree_indices = np.argsort(tree_feature_importances)[::-1][:2]
        tree_top2 = [feature_names[i] for i in tree_indices]

        # Top 2 Linear Model (baseado no valor absoluto)
        linear_indices = np.argsort(np.abs(linear_coefficients))[::-1][:2]
        linear_top2 = [feature_names[i] for i in linear_indices]

        return {
            'permutation': tuple(perm_top2),
            'tree_model': tuple(tree_top2),
            'linear_model': tuple(linear_top2)
        }

    @staticmethod
    def plot_2d_scatter_top_features(
        X: pd.DataFrame,
        y: np.ndarray,
        top_features_dict: Dict[str, Tuple[str, str]],
        dataset_name: str = "Dataset"
    ) -> None:
        """
        Cria 3 scatter plots 2D usando as top 2 features de cada método.
        Usa um mapa de cores (colormap) contínuo para representar o valor do alvo (y).

        Args:
            X: DataFrame com as features.
            y: Array contínuo com os valores alvo (target).
            top_features_dict: Dicionário com as top 2 features de cada método.
            dataset_name: Nome do dataset para o título.
        """
        fig, axes = plt.subplots(1, 3, figsize=(18, 5))

        method_titles = {
            'permutation': 'Top 2 - Permutation Importance',
            'tree_model': 'Top 2 - Tree Model',
            'linear_model': 'Top 2 - Linear Model'
        }

        for idx, (method, (feat1, feat2)) in enumerate(top_features_dict.items()):
            ax = axes[idx]
            
            # Scatter plot usando o alvo `y` como gradiente de cor
            sc = ax.scatter(X[feat1], X[feat2], c=y, cmap='viridis', 
                            alpha=0.7, edgecolors='k', s=50)

            ax.set_xlabel(feat1, fontsize=11)
            ax.set_ylabel(feat2, fontsize=11)
            ax.set_title(method_titles.get(method, method), fontsize=12, fontweight='bold')
            ax.grid(True, linestyle=':', alpha=0.6)
            
            cbar = plt.colorbar(sc, ax=ax)
            cbar.set_label('Target (y)', fontsize=10)

        plt.suptitle(f'Visualização 2D das Features Mais Importantes - {dataset_name}', 
                     fontsize=14, fontweight='bold', y=1.05)
        plt.tight_layout()
        plt.show()


class TrainingDiagnostic:
    """Classe responsável por diagnósticos de treinamento em Regressão (overfitting/underfitting)."""

    @staticmethod
    def analisar_aprendizado(
        modelo: Any,
        X_treino: np.ndarray,
        y_treino: np.ndarray,
        X_teste: np.ndarray,
        y_teste: np.ndarray,
        metricas: List[str] = ['r2', 'rmse', 'mae']
    ) -> Dict[str, float]:
        """
        Analisa se o modelo de regressão apresentou Overfitting, Underfitting ou Bom Ajuste.

        Args:
            modelo: Modelo treinado.
            X_treino: Features de treino.
            y_treino: Labels de treino.
            X_teste: Features de teste.
            y_teste: Labels de teste.
            metricas: Lista de métricas para calcular ('r2', 'rmse', 'mae').

        Returns:
            Dicionário com as métricas calculadas e o diagnóstico.
        """
        from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

        # Calcular previsões
        y_pred_treino = modelo.predict(X_treino)
        y_pred_teste = modelo.predict(X_teste)

        resultados = {}

        # Calcular métricas selecionadas
        if 'r2' in metricas:
            resultados['r2_treino'] = r2_score(y_treino, y_pred_treino)
            resultados['r2_teste'] = r2_score(y_teste, y_pred_teste)

        if 'rmse' in metricas:
            resultados['rmse_treino'] = np.sqrt(mean_squared_error(y_treino, y_pred_treino))
            resultados['rmse_teste'] = np.sqrt(mean_squared_error(y_teste, y_pred_teste))

        if 'mae' in metricas:
            resultados['mae_treino'] = mean_absolute_error(y_treino, y_pred_treino)
            resultados['mae_teste'] = mean_absolute_error(y_teste, y_pred_teste)

        # Diagnóstico baseado no R²
        diagnostico = TrainingDiagnostic._diagnosticar(resultados)

        # Imprimir relatório
        TrainingDiagnostic._imprimir_diagnostico(resultados, diagnostico)           

        resultados['diagnostico'] = diagnostico
        return resultados

    @staticmethod
    def _diagnosticar(resultados: Dict[str, float]) -> str:
        """
        Determina o tipo de ajuste baseado na métrica R² (coeficiente de determinação).

        Args:
            resultados: Dicionário com métricas de treino e teste.

        Returns:
            String com o diagnóstico: 'OVERFITTING', 'UNDERFITTING' ou 'BOM AJUSTE'.
        """
        r2_treino = resultados.get('r2_treino', 0)       
        r2_teste = resultados.get('r2_teste', 0)

        # Thresholds customizáveis para regressão
        threshold_bom = 0.60  # R² mínimo desejável
        gap_overfitting = 0.15  # Diferença máxima tolerada de R² entre treino e teste

        if r2_treino >= threshold_bom and r2_teste < threshold_bom:
            return "OVERFITTING"
        elif r2_treino < threshold_bom and r2_teste < threshold_bom:
            return "UNDERFITTING"
        elif (r2_treino - r2_teste) > gap_overfitting:
            return "OVERFITTING (Leve)"
        else:
            return "BOM AJUSTE"

    @staticmethod
    def _imprimir_diagnostico(resultados: Dict[str, float], diagnostico: str) -> None:
        """
        Imprime um relatório textual claro do diagnóstico de regressão.

        Args:
            resultados: Dicionário com métricas.
            diagnostico: Tipo de ajuste identificado.
        """
        print(f"\n{'='*60}")
        print("DIAGNÓSTICO DE APRENDIZADO DO MODELO DE REGRESSÃO")
        print(f"{'='*60}")

        if 'r2_treino' in resultados:
            print(f"R² no Treino:        {resultados['r2_treino']:.4f}")
            print(f"R² no Teste:         {resultados['r2_teste']:.4f}")
            print(f"Diferença no R²:     {(resultados['r2_treino'] - resultados['r2_teste']):.4f}")

        if 'rmse_treino' in resultados:
            print(f"RMSE no Treino:      {resultados['rmse_treino']:.4f}")
            print(f"RMSE no Teste:       {resultados['rmse_teste']:.4f}")

        if 'mae_treino' in resultados:
            print(f"MAE no Treino:       {resultados['mae_treino']:.4f}")
            print(f"MAE no Teste:        {resultados['mae_teste']:.4f}")

        print(f"\nDIAGNÓSTICO: {diagnostico}")

        if "OVERFITTING" in diagnostico:
            print("\n O modelo memorizou os dados de treino e tem baixo R² / alto erro no teste.")
            print("   Sugestões:")
            print("   - Reduzir a complexidade do modelo (ex: limitar profundidade da árvore)")
            print("   - Aumentar regularização (ex: Lasso/Ridge, aumentar alpha/lambda)")
            print("   - Fazer seleção de features (remover colunas ruidosas)")

        elif diagnostico == "UNDERFITTING":
            print("\n O modelo teve desempenho fraco tanto no treino quanto no teste.")
            print("   Sugestões:")
            print("   - Aumentar a complexidade do modelo (trocar modelo linear por Gradient Boosting, etc.)")
            print("   - Criar novas features relevantes (Feature Engineering/Polinomiais)")
            print("   - Reduzir a regularização")

        else: 
            print("\n O modelo apresentou bom equilíbrio entre aprendizado e generalização.")
            print("   Continue monitorando os resíduos e a performance em produção.")

        print(f"{'='*60}\n")