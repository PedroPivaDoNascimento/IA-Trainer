"""
Ponto de entrada da aplicação.
"""
from sklearn.decomposition import PCA
from sklearn.svm import SVC

from controllers.training_controller import TrainingController
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, Normalizer, QuantileTransformer, PowerTransformer
import warnings

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    dict_params = {}

    # Definição de caminhos para planilhas
    DATA_PATH = "./planilhas/Agachamento_Unipodal/dados_treinamento_quadril_esquerdo.xlsx"

    # Métrica alvo: 'f1_score', 'accuracy', 'balanced_accuracy', 'precision','recall', 'roc_auc' ou 'mcc'
    METRIC_FOCO = "balanced_accuracy"

    # Inicializa e executa o controlador
    controller = TrainingController(
        data_path=DATA_PATH,
        metric_focus=METRIC_FOCO,
        iterations=1,
        dict_params=dict_params
    )
    #controller.run_data_analysis()
    controller.run()
