"""
Ponto de entrada da aplicação.
"""
from controllers.training_controller import TrainingController

if __name__ == "__main__":
    # Definição de caminhos para planilhas
    DATA_PATH = "./planilhas/planilhas_dados/dados_pe_frontal_esquerdo_150_2_col.xlsx"
    RESULTS_PATH = "./planilhas/planilhas_resultados/resultados_pe_frontal_esquerdo_150.xlsx"

    # Métrica alvo: 'f1_score', 'accuracy', 'precision' ou 'recall'
    METRIC_FOCO = "recall"

    # Inicializa e executa o controlador MVC
    controller = TrainingController(
        data_path=DATA_PATH,
        results_path=RESULTS_PATH,
        metric_focus=METRIC_FOCO,
        iterations=10,
    )
    controller.run()