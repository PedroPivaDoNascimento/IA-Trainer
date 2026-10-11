"""
Ponto de entrada da aplicação.
"""
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

from sklearn.decomposition import PCA
from sklearn.linear_model import Ridge

from controllers.training_controller import TrainingController
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, Normalizer, QuantileTransformer, PowerTransformer
import warnings

if __name__ == "__main__":
    warnings.filterwarnings("ignore")

    #Parametros específicos para o KNN
    dict_params = {'clf': [RandomForestRegressor(random_state=42)], 'clf__ccp_alpha': [0.01], 'clf__criterion': ['squared_error'], 'clf__max_depth': [None], 'clf__min_samples_split': [5], 'clf__n_estimators': [145], 'reducao': ['passthrough'], 'scaler': [None]}

    #dict_params = None

    # Definição de caminhos para planilhas
    DATA_PATH = "./planilhas/Machine learning ganhos de forca (FIM POS).xlsx"

    # Métrica alvo para Regressão: 'r2', 'mae', 'mse' ou 'rmse'
    METRIC_FOCO = "rmse"

    # Inicializa e executa o controlador
    controller = TrainingController(    
        data_path=DATA_PATH,
        metric_focus=METRIC_FOCO,
        iterations=10,
        dict_params=dict_params
    )
    controller.run_data_analysis()
    #controller.run()
