"""
Script de demonstração das novas funcionalidades de análise e visualização.
Utiliza os datasets Iris e Digits com Random Forest, Regressão Logística e SVM.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris, load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, RobustScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.inspection import permutation_importance
from sklearn.decomposition import PCA

# Importar as novas classes de visualização e diagnóstico
from views.advanced_visualizations import AdvancedVisualizations, TrainingDiagnostic


def analisar_dataset_iris():
    """Executa todas as análises no dataset Iris."""
    print("=" * 70)
    print("ANÁLISE DO DATASET IRIS")
    print("=" * 70)
    
    # Carregar dados
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = iris.target
    feature_names = iris.feature_names
    class_names = iris.target_names
    
    print(f"\nDataset Iris: {X.shape[0]} amostras, {X.shape[1]} features")
    print(f"Features: {feature_names}")
    print(f"Classes: {class_names}")
    
    # Dividir dados
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=777, stratify=y
    )
    
    # Escalonar dados
    scaler = RobustScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    X_full_scaled = scaler.fit_transform(X)
    X_full_df = pd.DataFrame(X_full_scaled, columns=feature_names)
    
    # ============================================================
    # 1. TREINAR MODELOS PARA COMPARAÇÃO
    # ============================================================
    print("\n--- Treinando Modelos ---")
    
    # Random Forest
    rf_model = RandomForestClassifier(n_estimators=100, random_state=777, n_jobs=-1)
    rf_model.fit(X_train_scaled, y_train)
    print(f"Random Forest - Acurácia no teste: {rf_model.score(X_test_scaled, y_test):.4f}")
    
    # Regressão Logística
    lr_model = LogisticRegression(max_iter=1000, random_state=777)
    lr_model.fit(X_train_scaled, y_train)
    print(f"Regressão Logística - Acurácia no teste: {lr_model.score(X_test_scaled, y_test):.4f}")
    
    # SVM
    svm_model = SVC(kernel='rbf', random_state=777)
    svm_model.fit(X_train_scaled, y_train)
    print(f"SVM - Acurácia no teste: {svm_model.score(X_test_scaled, y_test):.4f}")
    
    # ============================================================
    # 2. DIAGNÓSTICO DE APRENDIZADO (OVERFITTING/UNDERFITTING)
    # ============================================================
    print("\n" + "=" * 70)
    print("DIAGNÓSTICO DE APRENDIZADO - RANDOM FOREST")
    print("=" * 70)
    TrainingDiagnostic.analisar_aprendizado(
        modelo=rf_model,
        X_treino=X_train_scaled,
        y_treino=y_train,
        X_teste=X_test_scaled,
        y_teste=y_test
    )
    
    print("\n" + "=" * 70)
    print("DIAGNÓSTICO DE APRENDIZADO - REGRESSÃO LOGÍSTICA")
    print("=" * 70)
    TrainingDiagnostic.analisar_aprendizado(
        modelo=lr_model,
        X_treino=X_train_scaled,
        y_treino=y_train,
        X_teste=X_test_scaled,
        y_teste=y_test
    )
    
    # ============================================================
    # 3. PERMUTATION IMPORTANCE
    # ============================================================
    print("\n--- Permutation Importance ---")
    result = permutation_importance(rf_model, X_test_scaled, y_test, n_repeats=10, random_state=777, n_jobs=-1)
    importance_df = pd.DataFrame({
        'Feature': feature_names,
        'Importance_Drop': result.importances_mean
    }).sort_values(by='Importance_Drop', ascending=False)
    print(importance_df.to_string(index=False))
    
    # ============================================================
    # 4. EXTRAIR IMPORTÂNCIAS NATIVAS
    # ============================================================
    rf_feature_importances = rf_model.feature_importances_
    
    # Para Regressão Logística multiclasse: média dos valores absolutos dos coeficientes
    if len(lr_model.coef_.shape) == 2 and lr_model.coef_.shape[0] > 1:
        lr_coefficients = np.mean(np.abs(lr_model.coef_), axis=0)
    else:
        lr_coefficients = np.abs(lr_model.coef_.flatten())
    
    # ============================================================
    # 5. COMPARAÇÃO DE IMPORTÂNCIA DE FEATURES COM GRÁFICOS
    # ============================================================
    print("\n[1/4] Gerando comparação de importância de features...")
    AdvancedVisualizations.plot_feature_importance_comparison(
        permutation_importance_df=importance_df,
        rf_feature_importances=rf_feature_importances,
        lr_coefficients=lr_coefficients,
        feature_names=feature_names,
        dataset_name="Iris"
    )
    
    # ============================================================
    # 6. IDENTIFICAR TOP 2 FEATURES DE CADA MÉTODO
    # ============================================================
    top_features_dict = AdvancedVisualizations.get_top_2_features(
        permutation_importance_df=importance_df,
        rf_feature_importances=rf_feature_importances,
        lr_coefficients=lr_coefficients,
        feature_names=feature_names
    )
    
    print(f"\nTop 2 Features - Permutation Importance: {top_features_dict['permutation']}")
    print(f"Top 2 Features - Random Forest: {top_features_dict['random_forest']}")
    print(f"Top 2 Features - Logistic Regression: {top_features_dict['logistic_regression']}")
    
    # ============================================================
    # 7. PLOTS 2D COM AS DUAS MELHORES FEATURES DE CADA MÉTODO
    # ============================================================
    print("\n[2/4] Gerando plots 2D das top features...")
    AdvancedVisualizations.plot_2d_scatter_top_features(
        X=X_full_df,
        y=y,
        top_features_dict=top_features_dict,
        class_names=class_names,
        dataset_name="Iris"
    )
    
    # ============================================================
    # 8. PCA 2D COM FEATURES DE INFLUÊNCIA POSITIVA
    # ============================================================
    print("\n[3/4] Gerando PCA com features de influência positiva...")
    positive_mask_lr = lr_coefficients > 0
    
    AdvancedVisualizations.plot_pca_positive_influence(
        X=X_full_df,
        y=y,
        feature_names=feature_names,
        positive_mask=positive_mask_lr,
        class_names=class_names,
        dataset_name="Iris"
    )
    
    print("\n" + "=" * 70)
    print("ANÁLISE DO DATASET IRIS CONCLUÍDA!")
    print("=" * 70)


def analisar_dataset_digits():
    """Executa análises similares no dataset Digits."""
    print("\n\n" + "=" * 70)
    print("ANÁLISE DO DATASET DIGITS")
    print("=" * 70)
    
    # Carregar dados
    digits = load_digits()
    X = pd.DataFrame(digits.data, columns=[f'pixel_{i}' for i in range(digits.data.shape[1])])
    y = digits.target
    feature_names = [f'pixel_{i}' for i in range(digits.data.shape[1])]
    class_names = [str(i) for i in range(10)]
    
    print(f"\nDataset Digits: {X.shape[0]} amostras, {X.shape[1]} features")
    print(f"Classes: {class_names}")
    
    # Dividir dados
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=777, stratify=y
    )
    
    # Escalonar dados
    scaler = RobustScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    X_full_scaled = scaler.fit_transform(X)
    X_full_df = pd.DataFrame(X_full_scaled, columns=feature_names)
    
    # ============================================================
    # TREINAR MODELOS
    # ============================================================
    print("\n--- Treinando Modelos ---")
    
    # Random Forest
    rf_model = RandomForestClassifier(n_estimators=100, random_state=777, n_jobs=-1)
    rf_model.fit(X_train_scaled, y_train)
    print(f"Random Forest - Acurácia no teste: {rf_model.score(X_test_scaled, y_test):.4f}")
    
    # Regressão Logística
    lr_model = LogisticRegression(max_iter=1000, random_state=777)
    lr_model.fit(X_train_scaled, y_train)
    print(f"Regressão Logística - Acurácia no teste: {lr_model.score(X_test_scaled, y_test):.4f}")
    
    # ============================================================
    # DIAGNÓSTICO DE APRENDIZADO
    # ============================================================
    print("\n" + "=" * 70)
    print("DIAGNÓSTICO DE APRENDIZADO - RANDOM FOREST (DIGITS)")
    print("=" * 70)
    TrainingDiagnostic.analisar_aprendizado(
        modelo=rf_model,
        X_treino=X_train_scaled,
        y_treino=y_train,
        X_teste=X_test_scaled,
        y_teste=y_test
    )
    
    # ============================================================
    # PERMUTATION IMPORTANCE
    # ============================================================
    print("\n--- Permutation Importance (Top 15 features) ---")
    result = permutation_importance(rf_model, X_test_scaled, y_test, n_repeats=10, random_state=777, n_jobs=-1)
    importance_df = pd.DataFrame({
        'Feature': feature_names,
        'Importance_Drop': result.importances_mean
    }).sort_values(by='Importance_Drop', ascending=False)
    print(importance_df.head(15).to_string(index=False))
    
    # ============================================================
    # EXTRAIR IMPORTÂNCIAS NATIVAS
    # ============================================================
    rf_feature_importances = rf_model.feature_importances_
    
    if len(lr_model.coef_.shape) == 2 and lr_model.coef_.shape[0] > 1:
        lr_coefficients = np.mean(np.abs(lr_model.coef_), axis=0)
    else:
        lr_coefficients = np.abs(lr_model.coef_.flatten())
    
    # ============================================================
    # COMPARAÇÃO DE IMPORTÂNCIA (TOP 15 FEATURES)
    # ============================================================
    print("\n[1/3] Gerando comparação de importância (Top 15 features)...")
    
    # Selecionar apenas top 15 features para visualização
    top_15_features = importance_df.head(15)['Feature'].tolist()
    top_15_indices = [feature_names.index(f) for f in top_15_features]
    
    AdvancedVisualizations.plot_feature_importance_comparison(
        permutation_importance_df=importance_df.head(15),
        rf_feature_importances=rf_feature_importances[top_15_indices],
        lr_coefficients=lr_coefficients[top_15_indices],
        feature_names=top_15_features,
        dataset_name="Digits (Top 15)"
    )
    
    # ============================================================
    # IDENTIFICAR TOP 2 FEATURES
    # ============================================================
    top_features_dict = AdvancedVisualizations.get_top_2_features(
        permutation_importance_df=importance_df,
        rf_feature_importances=rf_feature_importances,
        lr_coefficients=lr_coefficients,
        feature_names=feature_names
    )
    
    print(f"\nTop 2 Features - Permutation Importance: {top_features_dict['permutation']}")
    print(f"Top 2 Features - Random Forest: {top_features_dict['random_forest']}")
    print(f"Top 2 Features - Logistic Regression: {top_features_dict['logistic_regression']}")
    
    # ============================================================
    # PLOTS 2D COM TOP FEATURES
    # ============================================================
    print("\n[2/3] Gerando plots 2D das top features...")
    AdvancedVisualizations.plot_2d_scatter_top_features(
        X=X_full_df,
        y=y,
        top_features_dict=top_features_dict,
        class_names=class_names,
        dataset_name="Digits"
    )
    
    # ============================================================
    # PCA 2D COM FEATURES DE INFLUÊNCIA POSITIVA
    # ============================================================
    print("\n[3/3] Gerando PCA com features de influência positiva...")
    positive_mask_lr = lr_coefficients > 0
    
    AdvancedVisualizations.plot_pca_positive_influence(
        X=X_full_df,
        y=y,
        feature_names=feature_names,
        positive_mask=positive_mask_lr,
        class_names=class_names,
        dataset_name="Digits"
    )
    
    print("\n" + "=" * 70)
    print("ANÁLISE DO DATASET DIGITS CONCLUÍDA!")
    print("=" * 70)


if __name__ == "__main__":
    # Executar análise no dataset Iris
    analisar_dataset_iris()
    
    # Executar análise no dataset Digits
    analisar_dataset_digits()
    
    print("\n\n" + "=" * 70)
    print("TODAS AS ANÁLISES FORAM CONCLUÍDAS COM SUCESSO!")
    print("=" * 70)
