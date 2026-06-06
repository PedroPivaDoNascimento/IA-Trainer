# Treinador de IA - Classificador Multi-Modelo

Este é um framework modular de machine learning desenvolvido em Python para treinar, comparar e avaliar múltiplos classificadores automaticamente. Utilizando `GridSearchCV` e validação cruzada, o sistema testa diversas combinações de hiperparâmetros, escalonadores e técnicas de redução de dimensionalidade para encontrar o melhor modelo para sua base de dados.

## 🌟 Recursos

- **Busca Automática de Hiperparâmetros:** Executa `GridSearchCV` com validação cruzada (5 folds) para encontrar a melhor combinação de parâmetros.
- **Múltiplos Classificadores:** Suporte nativo para 10 algoritmos diferentes:
  - Perceptron, MLP (Redes Neurais), SVC, LinearSVC
  - Random Forest, Extra Trees, Gradient Boosting
  - K-Nearest Neighbors, Regressão Logística, Ridge Classifier
- **Pré-processamento Flexível:** Testa automaticamente 9 tipos de escalonadores (`StandardScaler`, `RobustScaler`, `MinMaxScaler`, etc.) e suporta redução de dimensionalidade (`PCA`, `SelectKBest`).
- **Múltiplas Métricas de Otimização:** Treine focando em `accuracy`, `f1_score`, `precision` ou `recall`, ideal para bases balanceadas ou desbalanceadas.
- **Avaliação Robusta:** Executa o treinamento com múltiplas sementes aleatórias (`random_state`) e calcula a média estatística dos resultados para maior confiabilidade.
- **Persistência de Modelos:** Exporta automaticamente o melhor pipeline treinado para arquivos `.pkl` usando `joblib`.
- **Arquitetura MVC + SOLID:** Código organizado em módulos (Model, View, Controller) seguindo boas práticas de engenharia de software, facilitando manutenção e testes.

## 💻 Tecnologias Utilizadas

- **Python 3.8+:** Linguagem de programação principal.
- **Scikit-Learn:** Biblioteca para modelos de machine learning, pipelines e validação cruzada.
- **Pandas:** Manipulação e análise de dados estruturados.
- **NumPy:** Operações matemáticas e arrays multidimensionais de alta performance.
- **Joblib:** Serialização eficiente de modelos treinados.
- **OpenPyXL:** Leitura de arquivos Excel (.xlsx).
- **Regex (`re`):** Processamento de texto para extração de métricas dos relatórios.

## 🚀 Instalação

Siga estes passos para configurar e executar o projeto localmente:

1.  Clone o repositório ou acesse o diretório do projeto:
    ```bash
    cd caminho/para/o/projeto
    ```

2.  (Opcional, mas recomendado) Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv && source venv/bin/activate  # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  Crie o arquivo `requirements.txt` na raiz do projeto e cole o conteúdo fornecido neste repositório, ou simplesmente execute:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuração de Módulos:**
    - Certifique-se de que o arquivo `excel_geter.py` (com a função `preparar_dados_para_treino`) esteja na **raiz do projeto**.
    - Crie arquivos `__init__.py` vazios dentro das pastas `config/`, `models/`, `evaluators/`, `views/` e `controllers/` para habilitar os imports relativos do Python.

## 🏃 Como usar

1.  Prepare suas planilhas de entrada:
    - Uma planilha com as **features** (variáveis preditoras).
    - Uma planilha com os **rótulos** (classes alvo: 0 ou 1).

2.  Configure os caminhos no arquivo `main.py`:
    ```python
    DATA_PATH = "./planilhas/planilhas_dados/sua_planilha_dados.xlsx"
    RESULTS_PATH = "./planilhas/planilhas_resultados/sua_planilha_resultados.xlsx"
    METRIC_FOCO = "recall"  # Opções: 'f1_score', 'accuracy', 'precision', 'recall'
    ```

3.  Execute o script principal para iniciar o treinamento:
    ```bash
    python main.py
    ```

4.  Acompanhe os resultados no console:
    - Métricas de validação cruzada para cada execução.
    - `classification_report` completo para o conjunto de teste.
    - Relatório consolidado com a média das métricas entre todas as execuções.
    - Modelos salvos automaticamente como `modelo_pe_frontal_esquerdo_X.pkl`.

### 📁 Estrutura do Projeto
projeto_ml/
├── main.py                      # Ponto de entrada
├── requirements.txt             # Lista de dependências (pip)
├── excel_geter.py               # [SEU ARQUIVO] Função preparar_dados_para_treino
│
├── config/
│   ├── init.py
│   └── settings.py              # Constantes e mapeamentos globais
│
├── models/
│   ├── init.py
│   ├── data_handler.py          # Carregamento e split dos dados
│   ├── model_config.py          # Definição de grade de hiperparâmetros
│   └── trainer.py               # Pipeline e execução do GridSearchCV
│
├── evaluators/
│   ├── init.py
│   └── metrics_handler.py       # Cálculo e agregação de métricas
│
├── views/
│   ├── init.py
│   └── report_view.py           # Exibição no console e salvamento de modelos
│
└── controllers/
    ├── init.py
    └── training_controller.py   # Orquestrador principal (MVC Controller)

## ⚙️ Personalização

### Adicionar um Novo Classificador
Edite o método `get_param_grid()` em `models/model_config.py` e adicione um novo dicionário com os parâmetros desejados:

```python
{
    'clf': [NovoClassificador(random_state=42)],
    'clf__param1': [valor1, valor2],
    'scaler': scalers,  # Reutiliza a lista de escaladores
    'reducao': ['passthrough'],
}
```

### Alterar a Métrica de Otimização
No arquivo main.py, modifique a variável METRIC_FOCO:
```python
METRIC_FOCO = "f1_score"  # Recomendado para dados desbalanceados
```

### Ajustar Número de Execuções
No TrainingController, altere o parâmetro iterations para executar com mais ou menos sementes aleatórias:
```python
controller = TrainingController(..., iterations=20)  # Default: 10
```

## 📬 Contato
Se você tiver alguma dúvida, sugestão ou encontrar algum bug, sinta-se à vontade para entrar em contato:
📧 pedropiva9@gmail.com
