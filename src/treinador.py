import pandas as pd
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import (
    StandardScaler, RobustScaler, MinMaxScaler, MaxAbsScaler, 
    QuantileTransformer, Normalizer, PowerTransformer
)
from excel_geter import preparar_dados_para_ia

def carregar_e_dividir_dados(arquivo_entrada, arquivo_resultados, test_size=0.2):
    """Carrega os dados do Excel e realiza a divisão estratificada."""
    X, y = preparar_dados_para_ia(arquivo_entrada, arquivo_resultados)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42, stratify=y
    )
    return X_train, X_test, y_train, y_test

def obter_configuracao_grid():
    """Define todos os scalers e a grade de parâmetros para o GridSearchCV."""
    scalers = [
        StandardScaler(), RobustScaler(), MinMaxScaler(), MaxAbsScaler(),
        QuantileTransformer(output_distribution='uniform', random_state=42),
        QuantileTransformer(output_distribution='normal', random_state=42),
        PowerTransformer(method='yeo-johnson'),
        Normalizer(norm='l2'),
        None 
    ]

    param_grid = [
        {
            'clf': [SVC(class_weight='balanced', random_state=42), 
                    LinearSVC(class_weight='balanced', random_state=42, max_iter=10000),
                    LogisticRegression(class_weight='balanced', solver='liblinear', random_state=42)],
            'scaler': scalers,
            'clf__C': [0.1, 1, 10, 100]
        },
        {
            'clf': [RandomForestClassifier(class_weight='balanced', random_state=42),
                    GradientBoostingClassifier(random_state=42)],
            'scaler': scalers,
            'clf__n_estimators': [100, 200],
            'clf__max_depth': [3, 5, None]
        },
        {
            'clf': [KNeighborsClassifier()],
            'scaler': scalers,
            'clf__n_neighbors': [3, 5, 7, 9],
            'clf__weights': ['uniform', 'distance']
        }
    ]
    return param_grid

def treinar_modelo(X_train, y_train, param_grid):
    """Executa o GridSearchCV e retorna o objeto do grid treinado."""
    pipe = Pipeline([('scaler', StandardScaler()), ('clf', SVC())])
    grid = GridSearchCV(pipe, param_grid, cv=8, n_jobs=-1, scoring='accuracy')
    grid.fit(X_train, y_train)
    return grid

def exibir_relatorio_detalhado(grid):
    """Mostra o desempenho de cada combinação testada no console."""
    print("\n" + "="*50)
    print("📊 RELATÓRIO COMPLETO DE TESTES (GRID SEARCH)")
    print("="*50)
    
    means = grid.cv_results_['mean_test_score']
    stds = grid.cv_results_['std_test_score']
    params = grid.cv_results_['params']

    for mean, std, param in zip(means, stds, params):
        modelo_nome = str(param['clf']).split('(')[0]
        print(f"Modelo: {modelo_nome}")
        print(f"-> Média: {mean*100:.2f}% (+/- {std:.4f})") 
        print(f"-> Parâmetros: {param}")
        print("-" * 30)

def avaliar_melhor_modelo(grid, X_test, y_test):
    """Realiza predições com o melhor modelo e exibe métricas por classe."""
    melhor_modelo = grid.best_estimator_
    y_pred = melhor_modelo.predict(X_test)
    
    df_performance = pd.DataFrame({'Real': y_test, 'Previsto': y_pred})

    print("\n" + "="*55)
    print("📊 RELATÓRIO DE TAXA DE ACERTO (PORCENTAGEM)")
    print("="*55)

    for classe in [0, 1]:
        nome = "CERTO (0)" if classe == 0 else "ERRADO (1)"
        total_da_classe = df_performance[df_performance['Real'] == classe]
        acertos_da_classe = total_da_classe[total_da_classe['Previsto'] == classe]
        
        if len(total_da_classe) > 0:
            taxa_acerto = (len(acertos_da_classe) / len(total_da_classe)) * 100
            print(f"🔹 Classe {nome}:")
            print(f"   -> Taxa de Acerto: {taxa_acerto:.2f}%")
            print(f"   -> Acertou {len(acertos_da_classe)} de {len(total_da_classe)} vídeos")
        else:
            print(f"🔹 Classe {nome}: Sem dados no conjunto de teste.")
        print("-" * 55)

    acerto_total = accuracy_score(y_test, y_pred) * 100
    melhor_std = grid.cv_results_['std_test_score'][grid.best_index_]
    
    print(f"🚀 ACURÁCIA GERAL NO TESTE: {acerto_total:.2f}%")
    print(f"📉 DESVIO PADRÃO (ESTABILIDADE): {melhor_std:.4f}")
    print(f"🏆 MELHOR PARÂMETRO: {grid.best_params_}")
    print("="*55)

def salvar_modelo(grid, nome_arquivo):
    """Exporta o melhor pipeline encontrado para um arquivo .pkl."""
    joblib.dump(grid.best_estimator_, nome_arquivo)
    print(f"\n💾 Modelo exportado com sucesso para: '{nome_arquivo}'")


if __name__ == "__main__":
    dados_frontal_direito = './planilhas/planilhas_dados/dados_pe_frontal_direito.xlsx'
    resultados_frontal_direito = './planilhas/planilhas_resultados/resultados_pe_frontal_direito.xlsx'
    X_train, X_test, y_train, y_test = carregar_e_dividir_dados(dados_frontal_direito, resultados_frontal_direito)
    
    config_params = obter_configuracao_grid()
    grid_treinado = treinar_modelo(X_train, y_train, config_params)
    
    exibir_relatorio_detalhado(grid_treinado)
    avaliar_melhor_modelo(grid_treinado, X_test, y_test)
    
    salvar_modelo(grid_treinado, 'modelo_pe_frontal_direito.pkl')