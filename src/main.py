"""
Ponto de entrada da aplicação.
"""
from controllers.training_controller import TrainingController
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, Normalizer, QuantileTransformer, PowerTransformer
import warnings

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    # Parametros específicos para o MLP
    #dict_params = {'clf': [MLPClassifier(random_state=31)], 'clf__activation': ['tanh'], 'clf__alpha': [0.0001], 'clf__early_stopping': [True], 'clf__hidden_layer_sizes': [(32,)], 'clf__learning_rate_init': [0.01], 'clf__max_iter': [1000], 'clf__validation_fraction': [0.1], 'reducao': ['passthrough'], 'scaler': [RobustScaler()]}

    #Parametros específicos para o KNN
    #dict_params = {'clf': [KNeighborsClassifier()], 'clf__metric': ['euclidean'], 'clf__n_neighbors': [5], 'clf__weights': ['uniform'], 'reducao': ['passthrough'], 'scaler': [PowerTransformer()]}

    dict_params = None

    # Definição de caminhos para planilhas
    DATA_PATH = "./planilhas/planilhas_dados/dados_pe_frontal_esquerdo_150_2_col.xlsx"
    RESULTS_PATH = "./planilhas/planilhas_resultados/resultados_pe_frontal_esquerdo_150.xlsx"

    # Métrica alvo: 'f1_score', 'accuracy', 'precision','recall' ou 'roc_auc'
    METRIC_FOCO = "f1_score"

    # Inicializa e executa o controlador
    controller = TrainingController(
        data_path=DATA_PATH,
        results_path=RESULTS_PATH,
        metric_focus=METRIC_FOCO,
        iterations=10,
        dict_params=dict_params
    )
    #controller.run_data_analysis()
    controller.run()
