"""
Ponto de entrada da aplicação.
"""
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import ElasticNet, LinearRegression

from sklearn.decomposition import PCA
from sklearn.linear_model import Ridge
from sklearn.svm import SVR

from controllers.training_controller import TrainingController
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MaxAbsScaler, MinMaxScaler, StandardScaler, RobustScaler, Normalizer, QuantileTransformer, PowerTransformer
import warnings

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    #dict_params = None
    dict_params = {'clf': [GradientBoostingRegressor(random_state=42)], 'clf__learning_rate': [0.125], 'clf__loss': ['absolute_error'], 'clf__max_depth': [4], 'clf__n_estimators': [125], 'reducao': ['passthrough'], 'scaler': [None]}


    # Definição de caminhos para planilhas
    DATA_PATH = "./planilhas/João/dados_novos/Machine learning ganhos de forca (FIM POS).xlsx"

    # Métrica alvo para Regressão: 'r2', 'mae', 'mse' ou 'rmse'
    METRIC_FOCO = "rmse"

    # Inicializa e executa o controlador
    controller = TrainingController(    
        data_path=DATA_PATH,
        metric_focus=METRIC_FOCO,
        iterations=10,
        dict_params=dict_params
    )
    #controller.run_data_analysis()
    controller.run()
