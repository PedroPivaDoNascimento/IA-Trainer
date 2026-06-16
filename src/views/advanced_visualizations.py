"""
Visualizações avançadas para análise de modelos de Machine Learning.
Inclui comparações de importância de features, plots 2D e diagnósticos.
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from typing import Tuple, List, Dict, Any


class AdvancedVisualizations:
    """Classe responsável por gerar visualizações avançadas de análise de modelos."""

    @staticmethod
    def plot_confusion_matrix(
        y_true: np.ndarray,
        y_pred: np.ndarray,
        class_names: List[str] = None,
        dataset_name: str = "Dataset"
    ) -> None:
        """
        Plota a matriz de confusão com anotações.

        Args:
            y_true: Array com os labels verdadeiros.
            y_pred: Array com os labels previstos.
            class_names: Nomes das classes para os rótulos dos eixos.
            dataset_name: Nome do dataset para o título.
        """
        from sklearn.metrics import confusion_matrix
        import seaborn as sns

        cm = confusion_matrix(y_true, y_pred)
        plt.figure(figsize=(6, 5))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                    xticklabels=class_names, yticklabels=class_names)
        plt.xlabel('Predito')
        plt.ylabel('Verdadeiro')
        plt.title(f'Matriz de Confusão - {dataset_name}', fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_feature_importance_comparison(
        permutation_importance_df: pd.DataFrame,
        rf_feature_importances: np.ndarray,
        lr_coefficients: np.ndarray,
        feature_names: List[str],
        dataset_name: str = "Dataset"
    ) -> None:
        """
        Plota 3 gráficos de barras horizontais comparando a importância das features
        pelos métodos: Permutation Importance, Random Forest Native e Logistic Regression.

        Args:
            permutation_importance_df: DataFrame com Permutation Importance.
            rf_feature_importances: Array com importâncias nativas do Random Forest.
            lr_coefficients: Array com coeficientes da Regressão Logística (média por feature).
            feature_names: Lista de nomes das features.
            dataset_name: Nome do dataset para o título.
        """
        fig, axes = plt.subplots(1, 3, figsize=(18, 6))

        # Permutation Importance
        perm_imp = permutation_importance_df.set_index('Feature')['Importance_Drop']
        perm_imp = perm_imp.reindex(feature_names)
        axes[0].barh(feature_names, perm_imp.values, color='steelblue')
        axes[0].set_xlabel('Queda na Acurácia')
        axes[0].set_title('Permutation Importance', fontsize=12, fontweight='bold')
        axes[0].invert_yaxis()
        axes[0].grid(axis='x', linestyle=':', alpha=0.6)

        # Random Forest Feature Importances
        axes[1].barh(feature_names, rf_feature_importances, color='darkorange')
        axes[1].set_xlabel('Importância (Gini Impurity Decrease)')
        axes[1].set_title('Random Forest Native', fontsize=12, fontweight='bold')
        axes[1].invert_yaxis()
        axes[1].grid(axis='x', linestyle=':', alpha=0.6)

        # Logistic Regression Coefficients
        axes[2].barh(feature_names, lr_coefficients, color='forestgreen')
        axes[2].set_xlabel('Média dos Coeficientes Absolutos')
        axes[2].set_title('Logistic Regression Coefficients', fontsize=12, fontweight='bold')
        axes[2].invert_yaxis()
        axes[2].grid(axis='x', linestyle=':', alpha=0.6)

        plt.suptitle(f'Comparação de Importância de Features - {dataset_name}', 
                     fontsize=14, fontweight='bold', y=1.02)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def get_top_2_features(
        permutation_importance_df: pd.DataFrame,
        rf_feature_importances: np.ndarray,
        lr_coefficients: np.ndarray,
        feature_names: List[str]
    ) -> Dict[str, Tuple[str, str]]:
        """
        Identifica as 2 features mais importantes de acordo com cada método.

        Args:
            permutation_importance_df: DataFrame com Permutation Importance.
            rf_feature_importances: Array com importâncias do Random Forest.
            lr_coefficients: Array com coeficientes da Regressão Logística.
            feature_names: Lista de nomes das features.

        Returns:
            Dicionário com as top 2 features de cada método.
        """
        # Top 2 Permutation Importance
        perm_top2 = permutation_importance_df.nlargest(2, 'Importance_Drop')['Feature'].tolist()

        # Top 2 Random Forest
        rf_indices = np.argsort(rf_feature_importances)[::-1][:2]
        rf_top2 = [feature_names[i] for i in rf_indices]

        # Top 2 Logistic Regression
        lr_indices = np.argsort(lr_coefficients)[::-1][:2]
        lr_top2 = [feature_names[i] for i in lr_indices]

        return {
            'permutation': tuple(perm_top2),
            'random_forest': tuple(rf_top2),
            'logistic_regression': tuple(lr_top2)
        }

    @staticmethod
    def plot_2d_scatter_top_features(
        X: pd.DataFrame,
        y: np.ndarray,
        top_features_dict: Dict[str, Tuple[str, str]],
        class_names: List[str] = None,
        dataset_name: str = "Dataset"
    ) -> None:
        """
        Cria 3 scatter plots 2D usando as top 2 features de cada método.

        Args:
            X: DataFrame com as features.
            y: Array com os labels.
            top_features_dict: Dicionário com as top 2 features de cada método.
            class_names: Nomes das classes para legenda.
            dataset_name: Nome do dataset para o título.
        """
        fig, axes = plt.subplots(1, 3, figsize=(18, 5))

        method_titles = {
            'permutation': 'Top 2 - Permutation Importance',
            'random_forest': 'Top 2 - Random Forest',
            'logistic_regression': 'Top 2 - Logistic Regression'
        }

        colors = plt.cm.Set1(np.linspace(0, 1, len(np.unique(y))))

        for idx, (method, (feat1, feat2)) in enumerate(top_features_dict.items()):
            ax = axes[idx]
            
            # Plot scatter
            for class_idx, class_val in enumerate(np.unique(y)):
                mask = y == class_val
                label = class_names[class_idx] if class_names is not None else f'Classe {class_val}'
                ax.scatter(X.loc[mask, feat1], X.loc[mask, feat2], 
                          c=[colors[class_idx]], label=label, alpha=0.7, edgecolors='k', s=50)

            ax.set_xlabel(feat1, fontsize=11)
            ax.set_ylabel(feat2, fontsize=11)
            ax.set_title(method_titles[method], fontsize=12, fontweight='bold')
            ax.legend(loc='best', fontsize=9)
            ax.grid(True, linestyle=':', alpha=0.6)

        plt.suptitle(f'Visualização 2D das Features Mais Importantes - {dataset_name}', 
                     fontsize=14, fontweight='bold', y=1.05)
        plt.tight_layout()
        plt.show()

    


class TrainingDiagnostic:
    """Classe responsável por diagnósticos de treinamento (overfitting/underfitting)."""

    @staticmethod
    def analisar_aprendizado(
        modelo: Any,
        X_treino: np.ndarray,
        y_treino: np.ndarray,
        X_teste: np.ndarray,
        y_teste: np.ndarray,
        metricas: List[str] = ['accuracy', 'f1']
    ) -> Dict[str, float]:
        """
        Analisa se o modelo apresentou Overfitting, Underfitting ou Bom Ajuste.

        Args:
            modelo: Modelo treinado (deve ter método .score() ou ser um pipeline).
            X_treino: Features de treino.
            y_treino: Labels de treino.
            X_teste: Features de teste.
            y_teste: Labels de teste.
            metricas: Lista de métricas para calcular ('accuracy', 'f1').

        Returns:
            Dicionário com as métricas calculadas e o diagnóstico.
        """
        from sklearn.metrics import accuracy_score, f1_score

        # Calcular previsões
        y_pred_treino = modelo.predict(X_treino)
        y_pred_teste = modelo.predict(X_teste)

        resultados = {}

        # Calcular métricas
        if 'accuracy' in metricas:
            acc_treino = accuracy_score(y_treino, y_pred_treino)
            acc_teste = accuracy_score(y_teste, y_pred_teste)
            resultados['accuracy_treino'] = acc_treino
            resultados['accuracy_teste'] = acc_teste

        if 'f1' in metricas:
            f1_treino = f1_score(y_treino, y_pred_treino, average='weighted', zero_division=0)
            f1_teste = f1_score(y_teste, y_pred_teste, average='weighted', zero_division=0)
            resultados['f1_treino'] = f1_treino
            resultados['f1_teste'] = f1_teste

        # Diagnóstico
        diagnostico = TrainingDiagnostic._diagnosticar(resultados)

        # Imprimir relatório
        TrainingDiagnostic._imprimir_diagnostico(resultados, diagnostico)

        resultados['diagnostico'] = diagnostico
        return resultados

    @staticmethod
    def _diagnosticar(resultados: Dict[str, float]) -> str:
        """
        Determina o tipo de ajuste baseado nas métricas.

        Args:
            resultados: Dicionário com métricas de treino e teste.

        Returns:
            String com o diagnóstico: 'OVERFITTING', 'UNDERFITTING' ou 'BOM AJUSTE'.
        """
        acc_treino = resultados.get('accuracy_treino', 0)
        acc_teste = resultados.get('accuracy_teste', 0)

        # Thresholds para diagnóstico
        threshold_bom = 0.7  # Mínimo para considerar "bom"
        gap_overfitting = 0.15  # Diferença máxima aceitável entre treino e teste

        if acc_treino >= threshold_bom and acc_teste < threshold_bom:
            return "OVERFITTING"
        elif acc_treino < threshold_bom and acc_teste < threshold_bom:
            return "UNDERFITTING"
        elif (acc_treino - acc_teste) > gap_overfitting:
            return "OVERFITTING (Leve)"
        else:
            return "BOM AJUSTE"

    @staticmethod
    def _imprimir_diagnostico(resultados: Dict[str, float], diagnostico: str) -> None:
        """
        Imprime um relatório textual claro do diagnóstico.

        Args:
            resultados: Dicionário com métricas.
            diagnostico: Tipo de ajuste identificado.
        """
        print(f"\n{'='*60}")
        print("DIAGNÓSTICO DE APRENDIZADO DO MODELO")
        print(f"{'='*60}")

        if 'accuracy_treino' in resultados:
            print(f"Acurácia no Treino:  {resultados['accuracy_treino']:.2%}")
            print(f"Acurácia no Teste:   {resultados['accuracy_teste']:.2%}")
            print(f"Diferença:           {(resultados['accuracy_treino'] - resultados['accuracy_teste']):.2%}")

        if 'f1_treino' in resultados:
            print(f"F1-Score no Treino:  {resultados['f1_treino']:.2%}")
            print(f"F1-Score no Teste:   {resultados['f1_teste']:.2%}")
            print(f"Diferença:           {(resultados['f1_treino'] - resultados['f1_teste']):.2%}")

        print(f"\nDIAGNÓSTICO: {diagnostico}")

        if diagnostico == "OVERFITTING":
            print("\n O modelo memorizou os dados de treino e não generaliza bem.")
            print("   Sugestões:")
            print("   - Reduzir complexidade do modelo")
            print("   - Aumentar regularização")
            print("   - Adicionar mais dados de treino")
            print("   - Usar técnicas de dropout ou early stopping")

        elif diagnostico == "UNDERFITTING":
            print("\n O modelo não conseguiu aprender padrões suficientes.")
            print("   Sugestões:")
            print("   - Aumentar complexidade do modelo")
            print("   - Adicionar mais features relevantes")
            print("   - Reduzir regularização")
            print("   - Treinar por mais épocas/iterações")

        else: 
            print("\n O modelo apresentou bom equilíbrio entre aprendizado e generalização.")
            print("   Continue monitorando em dados não vistos.")

        print(f"{'='*60}\n")
