"""
Configurações globais, mapeamentos de métricas e constantes do projeto.
"""
from sklearn.metrics import make_scorer, matthews_corrcoef

# MCC (Matthews Correlation Coefficient) não é uma string de scoring nativa
# no formato usado aqui, então criamos um scorer customizado com `make_scorer`
# seguindo a mesma lógica das demais métricas (ex: f1).
MCC_SCORER = make_scorer(matthews_corrcoef)

# Mapeamento entre nomes amigáveis e strings internas do scikit-learn
METRIC_SCORING_MAP = {
    "f1_score": "f1",
    "accuracy": "accuracy",
    "precision": "precision",
    "recall": "recall",
    "roc_auc": "roc_auc",
    "mcc": MCC_SCORER,
}

SCORING_PIPELINE_MAP = {
    "f1": "f1",
    "accuracy": "accuracy",
    "precision": "precision",
    "recall": "recall",
    "roc_auc": "roc_auc",
    "mcc": MCC_SCORER,
}

# Nomes das colunas de desvio padrão nos resultados do GridSearchCV
STD_MAP = {
    "f1_score": "std_test_f1",
    "accuracy": "std_test_accuracy",
    "precision": "std_test_precision",
    "recall": "std_test_recall",
    "roc_auc": "std_test_roc_auc",
    "mcc": "std_test_mcc",
}

# Nomes das classes no relatório de classificação
CLASS_NAMES = ["CERTO (0)", "ERRADO (1)"]