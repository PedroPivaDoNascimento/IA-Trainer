import pandas as pd

def preparar_dados_para_treino(caminho_estatistico):
    """Função que pega os valores da planilha de estatístico e de resultados e retorna os dados para o treinamento"""
    
    # Leitura dos dados estatísticos
    df = pd.read_excel(caminho_estatistico, engine='openpyxl')
    
    # Extrai as colunas a partir da terceira (índice 2) até a penúltima (excluindo a última)
    X = df.iloc[:, 2:-1]
        
    # Extrai apenas a coluna 'Resultado' como um vetor (0 e 1)
    y = df['Resultados'].values

    return X, y

def pegar_nomes_das_features(caminho_estatistico):
    """Função que retorna os nomes das features a partir da planilha de estatístico"""
    df_estatistico = pd.read_excel(caminho_estatistico, engine='openpyxl')
    feature_names = df_estatistico.columns[2:-1].tolist()  # Pegando os nomes das colunas a partir da terceira coluna

    return feature_names
