import time
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score, f1_score, precision_score,
    recall_score, classification_report
)
from sklearn.svm import SVC, LinearSVC
from sklearn.calibration import CalibratedClassifierCV
from sklearn.ensemble import (
    RandomForestClassifier, GradientBoostingClassifier, ExtraTreesClassifier
)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression, Perceptron, RidgeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import (
    StandardScaler, RobustScaler, MinMaxScaler, MaxAbsScaler,
    QuantileTransformer, Normalizer, PowerTransformer
)
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest, f_classif
from excel_geter import preparar_dados_para_ia


# ─────────────────────────────────────────────
# 1. CARREGAMENTO E DIVISÃO DOS DADOS
# ─────────────────────────────────────────────

def carregar_e_dividir_dados(arquivo_entrada, arquivo_resultados, test_size=0.2):
    """Carrega os dados do Excel e realiza a divisão estratificada."""
    X, y = preparar_dados_para_ia(arquivo_entrada, arquivo_resultados)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42, stratify=y
    )
    return X_train, X_test, y_train, y_test


# ─────────────────────────────────────────────
# 2. CONFIGURAÇÃO DO GRID
# ─────────────────────────────────────────────

def obter_configuracao_grid():
    """Define scalers e a grade de parâmetros para o GridSearchCV."""

    scalers = [
        StandardScaler(),
        RobustScaler(),
        MinMaxScaler(),
        MaxAbsScaler(),
        QuantileTransformer(output_distribution='uniform', random_state=42),
        QuantileTransformer(output_distribution='normal', random_state=42),
        PowerTransformer(method='yeo-johnson'),
        Normalizer(norm='l2'),
        None,
    ]

    # Descomente reduções se quiser testar PCA/SelectKBest (aumenta tempo)
    reducoes = [
        'passthrough',
        # PCA(n_components=0.95),
        # PCA(n_components=0.80),
        # SelectKBest(f_classif, k=10),
        # SelectKBest(f_classif, k=20),
    ]

    param_grid = [

        # 1. PERCEPTRON
        {
            'clf':          [Perceptron(random_state=42, class_weight='balanced')],
            'clf__eta0':    [0.1, 0.01, 1.0],
            'clf__penalty': ['l2', 'l1', 'elasticnet'],
            'scaler':       scalers,
            'reducao':      ['passthrough'],
        },

        # 2. MLP (Neural Network)
        {
            'scaler':                   [StandardScaler(), MinMaxScaler(), RobustScaler()],
            'reducao':                  reducoes,
            'clf':                      [MLPClassifier(random_state=31, solver='adam')],
            'clf__hidden_layer_sizes':  [(64,), (128,), (64, 32), (128, 64)],
            'clf__activation':          ['relu', 'tanh'],
            'clf__alpha':               [0.0001, 0.001, 0.01],
            'clf__learning_rate_init':  [0.001, 0.01],
            'clf__early_stopping':      [True],
            'clf__validation_fraction': [0.1],
            'clf__max_iter':            [1000],
        },

        # 3. SVC (Support Vector Classifier)
        {
            'clf':         [SVC(random_state=42, class_weight='balanced')],
            'clf__C':      [0.1, 1, 5, 10, 50, 100],
            'clf__kernel': ['rbf', 'poly'],
            'clf__gamma':  ['scale', 'auto'],
            'scaler':      scalers,
            'reducao':     reducoes,
        },

        # 4. LINEAR SVC
        {
            'clf':          [LinearSVC(random_state=42, class_weight='balanced')],
            'clf__max_iter':[1000, 2000],
            'clf__C':       [0.1, 1, 5, 10, 50, 100],
            'clf__dual':    [False],
            'scaler':       scalers,
            'reducao':      reducoes,
        },

        # 5. RANDOM FOREST
        {
            'clf':               [RandomForestClassifier(random_state=42, class_weight='balanced')],
            'clf__n_estimators': [100, 300, 500],
            'clf__max_depth':    [None, 10, 20],
            'clf__criterion':    ['gini', 'entropy'],
            'scaler':            [None],
            'reducao':           ['passthrough'],
        },

        # 6. EXTRA TREES  ← novo: geralmente mais rápido que Random Forest
        {
            'clf':               [ExtraTreesClassifier(random_state=42, class_weight='balanced')],
            'clf__n_estimators': [100, 300],
            'clf__max_depth':    [None, 10, 20],
            'clf__criterion':    ['gini', 'entropy'],
            'scaler':            [None],
            'reducao':           ['passthrough'],
        },

        # 7. GRADIENT BOOSTING
        {
            'clf':                [GradientBoostingClassifier(random_state=42)],
            'clf__n_estimators':  [100, 200],
            'clf__learning_rate': [0.05, 0.1, 0.2],
            'clf__max_depth':     [3, 5],
            'scaler':             [None],
            'reducao':            ['passthrough'],
        },

        # 8. KNN
        {
            'clf':               [KNeighborsClassifier()],
            'clf__n_neighbors':  [1, 3, 5, 7, 9, 11],
            'clf__weights':      ['uniform', 'distance'],
            'clf__metric':       ['euclidean', 'manhattan'],
            'scaler':            scalers,
            'reducao':           reducoes,
        },

        # 9. LOGISTIC REGRESSION
        {
            'clf':          [LogisticRegression(random_state=42, class_weight='balanced', max_iter=1000)],
            'clf__C':       [0.01, 0.1, 1, 5, 10, 50, 100],
            'clf__solver':  ['liblinear', 'lbfgs'],
            'scaler':       scalers,
            'reducao':      reducoes,
        },

        # 10. RIDGE CLASSIFIER  ← novo: linear, muito rápido como baseline adicional
        {
            'clf':        [RidgeClassifier(class_weight='balanced')],
            'clf__alpha': [0.1, 1.0, 10.0, 100.0],
            'scaler':     scalers,
            'reducao':    ['passthrough'],
        },
    ]

    return param_grid


# ─────────────────────────────────────────────
# 3. TREINAMENTO
# ─────────────────────────────────────────────

def treinar_modelo(X_train, y_train, param_grid, metrica_foco):
    """Executa o GridSearchCV com múltiplas métricas e retorna o objeto treinado."""

    # Mapeamento da escolha do usuário para o nome interno do scoring
    mapa_scoring = {
        'f1_score':  'f1',
        'accuracy':  'accuracy',
        'precision': 'precision',
        'recall':    'recall',
    }

    refit_metrica = mapa_scoring[metrica_foco]

    pipe = Pipeline(
        [('scaler', StandardScaler()), ('reducao', PCA()), ('clf', SVC())],
        verbose=False,
    )

    scoring = {
        'f1':        'f1_weighted',
        'accuracy':  'accuracy',
        'precision': 'precision_weighted',
        'recall':    'recall_weighted',
    }

    grid = GridSearchCV(
        pipe, param_grid,
        cv=5, n_jobs=-2,
        scoring=scoring,
        refit=refit_metrica,   # melhor modelo escolhido pela métrica que você definiu
        verbose=2,
        return_train_score=False,
    )
    grid.fit(X_train, y_train)
    return grid


# ─────────────────────────────────────────────
# 4. RELATÓRIOS
# ─────────────────────────────────────────────

def exibir_relatorio_detalhado(grid, metrica_foco):
    """Mostra no terminal o desempenho de cada combinação, ordenado pela métrica escolhida."""

    mapa_coluna = {
        'f1_score':  'mean_test_f1',
        'accuracy':  'mean_test_accuracy',
        'precision': 'mean_test_precision',
        'recall':    'mean_test_recall',
    }
    coluna_ordenacao = mapa_coluna[metrica_foco]

    cv     = grid.cv_results_
    params = cv['params']

    # Ordena os índices pela métrica de foco (maior para menor)
    indices_ordenados = sorted(
        range(len(params)),
        key=lambda i: cv[coluna_ordenacao][i],
        reverse=True
    )

    print("\n" + "=" * 65)
    print(f"📊 RELATÓRIO COMPLETO — ORDENADO POR: {metrica_foco.upper()}")
    print("=" * 65)

    for rank, i in enumerate(indices_ordenados, start=1):
        param       = params[i]
        modelo_nome = str(param['clf']).split('(')[0]
        scaler_nome = str(param.get('scaler', 'None')).split('(')[0]
        reducao_str = str(param.get('reducao', 'passthrough')).split('(')[0]

        f1    = cv['mean_test_f1'][i] * 100
        acc   = cv['mean_test_accuracy'][i] * 100
        prec  = cv['mean_test_precision'][i] * 100
        rec   = cv['mean_test_recall'][i] * 100
        std   = cv[f'std_test_{mapa_coluna[metrica_foco].split("_")[-1]}'][i]

        print(f"#{rank:>3} | Modelo: {modelo_nome}  |  Scaler: {scaler_nome}  |  Redução: {reducao_str}")
        print(f"       F1-Score : {f1:.2f}%   Acurácia : {acc:.2f}%   Precisão : {prec:.2f}%   Recall : {rec:.2f}%   Std({metrica_foco}): {std:.4f}")
        print(f"       Params   : {param}")
        print("-" * 65)


def avaliar_melhor_modelo(grid, X_test, y_test, metrica_foco):
    """Realiza predições com o melhor modelo e exibe métricas completas."""

    mapa_std = {
        'f1_score':  'std_test_f1',
        'accuracy':  'std_test_accuracy',
        'precision': 'std_test_precision',
        'recall':    'std_test_recall',
    }

    melhor_modelo = grid.best_estimator_
    y_pred        = melhor_modelo.predict(X_test)

    acuracia   = accuracy_score(y_test, y_pred) * 100
    f1_w       = f1_score(y_test, y_pred, average='weighted') * 100
    precisao_w = precision_score(y_test, y_pred, average='weighted', zero_division=0) * 100
    recall_w   = recall_score(y_test, y_pred, average='weighted', zero_division=0) * 100
    melhor_std = grid.cv_results_[mapa_std[metrica_foco]][grid.best_index_]

    print("\n" + "=" * 60)
    print(f"🏆 MELHOR MODELO — OTIMIZADO POR: {metrica_foco.upper()}")
    print("=" * 60)
    print(f"{'Acurácia':<28} {acuracia:.2f}%")
    print(f"{'F1-Score (weighted)':<28} {f1_w:.2f}%")
    print(f"{'Precisão (weighted)':<28} {precisao_w:.2f}%")
    print(f"{'Recall (weighted)':<28} {recall_w:.2f}%")
    print(f"{'Desvio Padrão (CV - ' + metrica_foco + ')':<28} {melhor_std:.4f}")
    print("-" * 60)

    # ── Métricas por classe ────────────────── ─────────────────────────────
    print("\n📌 MÉTRICAS POR CLASSE:")
    print("-" * 60)
    nomes_classes = {0: "CERTO (0)", 1: "ERRADO (1)"}

    for classe in sorted(set(y_test)):
        nome  = nomes_classes.get(classe, str(classe))
        mask  = y_test == classe
        total = mask.sum()
        acertos = ((y_pred == classe) & mask).sum()
        taxa  = (acertos / total * 100) if total > 0 else 0.0

        f1_c  = f1_score(y_test, y_pred, labels=[classe], average='macro', zero_division=0) * 100
        prec  = precision_score(y_test, y_pred, labels=[classe], average='macro', zero_division=0) * 100
        rec   = recall_score(y_test, y_pred, labels=[classe], average='macro', zero_division=0) * 100

        print(f"🔹 Classe {nome}:")
        print(f"   Taxa de Acerto : {taxa:.2f}%  ({acertos}/{total} amostras)")
        print(f"   F1-Score       : {f1_c:.2f}%")
        print(f"   Precisão       : {prec:.2f}%")
        print(f"   Recall         : {rec:.2f}%")
        print("-" * 60)

    # ── Relatório detalhado do sklearn ────────────────────────────────────
    print("\n📋 CLASSIFICATION REPORT (sklearn):")
    print(classification_report(y_test, y_pred, target_names=["CERTO (0)", "ERRADO (1)"], zero_division=0))

    print(f"🏆 MELHORES PARÂMETROS: {grid.best_params_}")
    print("=" * 60)


# ─────────────────────────────────────────────
# 5. EXPORTAÇÃO DO MODELO
# ─────────────────────────────────────────────

def salvar_modelo(grid, nome_arquivo):
    """Exporta o melhor pipeline encontrado para um arquivo .pkl."""
    joblib.dump(grid.best_estimator_, nome_arquivo)
    print(f"\n💾 Modelo exportado com sucesso para: '{nome_arquivo}'")


# ─────────────────────────────────────────────
# 6. MAIN
# ─────────────────────────────────────────────

if __name__ == "__main__":
    inicio = time.time()

    # ──────────────────────────────────────────────────────────────────────
    # ⚙️  ALTERE AQUI a métrica que vai guiar a escolha do melhor modelo.
    #     O relatório será ordenado por ela e o modelo salvo será o melhor
    #     segundo esse critério.
    #
    #     Opções disponíveis:
    #       'f1_score'  → melhor equilíbrio entre precisão e recall (recomendado para dados desbalanceados)
    #       'accuracy'  → maior taxa de acerto geral
    #       'precision' → minimiza falsos positivos (quando errar "certo" é caro)
    #       'recall'    → minimiza falsos negativos (quando perder um "errado" é caro)
    # ──────────────────────────────────────────────────────────────────────
    METRICA_FOCO = 'f1_score'

    dados_frontal_direito      = './planilhas/planilhas_dados/dados_pe_frontal_direito.xlsx'
    resultados_frontal_direito = './planilhas/planilhas_resultados/resultados_pe_frontal_direito.xlsx'

    dados_frontal_esquerdo      = './planilhas/planilhas_dados/dados_pe_frontal_esquerdo.xlsx'
    resultados_frontal_esquerdo = './planilhas/planilhas_resultados/resultados_pe_frontal_esquerdo.xlsx'

    dados_frontal_esquerdo_antigo      = './planilhas/planilhas_dados/dados_pe_frontal_esquerdo_antigo.xlsx'
    resultados_frontal_esquerdo_antigo = './planilhas/planilhas_resultados/resultados_pe_frontal_esquerdo_antigo.xlsx'

    dados_frontal_esquerdo_90_videos      = './planilhas/planilhas_dados/dados_pe_frontal_esquerdo_90_videos.xlsx'
    resultados_frontal_esquerdo_90_videos = './planilhas/planilhas_resultados/resultados_pe_frontal_esquerdo_90_videos.xlsx'

    dados_frontal_esquerdo_90_videos_sem_min_max_amplitude = (
        './planilhas/planilhas_dados/dados_pe_frontal_esquerdo_90_videos_sem_o_min_max_amplitude.xlsx'
    )
    dados_frontal_esquerdo_90_videos_novas_colunas = (
        './planilhas/planilhas_dados/dados_pe_frontal_esquerdo_90_videos_novas_colunas.xlsx'
    )
    dados_pe_frontal_esquerdo_90_videos_std = (
        './planilhas/planilhas_dados/dados_pe_frontal_esquerdo_90_videos_std.xlsx'
    )

    # ── Escolha o conjunto que deseja treinar ──
    X_train, X_test, y_train, y_test = carregar_e_dividir_dados(
        dados_frontal_direito, resultados_frontal_direito
    )

    config_params = obter_configuracao_grid()
    grid_treinado = treinar_modelo(X_train, y_train, config_params, METRICA_FOCO)

    exibir_relatorio_detalhado(grid_treinado, METRICA_FOCO)
    avaliar_melhor_modelo(grid_treinado, X_test, y_test, METRICA_FOCO)

    salvar_modelo(grid_treinado, 'modelo_pe_frontal_esquerdo.pkl')

    fim = time.time()
    minutos = (fim - inicio) / 60
    print(f"\n⏱️  Tempo total de execução: {minutos:.1f} minutos")