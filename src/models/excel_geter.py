import pandas as pd

def preparar_dados_para_treino(caminho_estatistico, caminho_resultados):
    """Função que pega os valores da planilha de estatístico e de resultados e retorna os dados para o treinameto"""
    
    # Leitura dos dados estatísticos
    df_estatistico = pd.read_excel(caminho_estatistico, engine='openpyxl')
    
    # Extrai todas as colunas a partir da terceira coluna
    X = df_estatistico.iloc[:, 2:].values
    
    # Leitura dos dados de resultados
    df_resultados = pd.read_excel(caminho_resultados, engine='openpyxl')
    
    # Extrai apenas a coluna 'Resultado' como um vetor (0 e 1)
    y = df_resultados['Resultado'].values
    
    return X, y

