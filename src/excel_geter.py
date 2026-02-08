import pandas as pd
import numpy as np

def preparar_dados_para_ia(caminho_estatistico, caminho_resultados):
    df_estatistico = pd.read_excel(caminho_estatistico, engine='openpyxl')
    
    # Removo as colunas de texto/identificação para a matriz de treino
    # Mantemos apenas os valores numéricos (das estatísticas calculadas)
    # .iloc[:, 2:] pula 'voluntario' e 'repeticao'
    X = df_estatistico.iloc[:, 2:].values
    
    df_resultados = pd.read_excel(caminho_resultados, engine='openpyxl')
    
    # Extrai apenas a coluna 'Resultado' como um vetor (0 e 1)
    y = df_resultados['Resultado'].values
    
    return X, y

# Altere para o caminho real da pasta de dados
#X, y = preparar_dados_para_ia('./planilhas/planilha_dados/dados_pe_frontal_.xlsx', './planilhas/planilha_resultados.xlsx')


# Verificação do formato
#print(f"Formato da Matriz de Atributos (X): {X.shape}") # (n_amostras, n_estatisticas)
#print(f"Formato do Vetor de Rótulos (y): {y.shape}")    # (n_amostras,)
