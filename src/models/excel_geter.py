import pandas as pd

import pandas as pd

def preparar_dados_para_treino(caminho_estatistico):
    """Função que pega todas as colunas exceto a última para o X e a última para o y"""
    
    # Leitura dos dados
    df_estatistico = pd.read_excel(caminho_estatistico, engine='openpyxl')
    
    # X pega todas as colunas EXCETO a última
    X = df_estatistico.iloc[:, :-1]
    
    # y pega APENAS a última coluna
    y = df_estatistico.iloc[:, -1].values

    return X, y

def pegar_nomes_das_features(caminho_estatistico):
    """Função que retorna os nomes das features a partir da planilha de estatístico"""
    df_estatistico = pd.read_excel(caminho_estatistico, engine='openpyxl')
    feature_names = df_estatistico.columns[:-1].tolist()  # Pegando os nomes das colunas exepto a ultima

    return feature_names

