        ====== MODELO 1 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.7091
Métrica (CV - MAE)           0.9975
Métrica (CV - MSE)           1.5387
Métrica (CV - RMSE)          1.2113
Desvio Padrão (CV - rmse)    0.2676
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.9093
MAE      : 0.7890
MSE      : 0.9424
RMSE     : 0.9708

Parâmetros: {'clf': LinearRegression(), 'clf__fit_intercept': True, 'clf__positive': True, 'reducao': 'passthrough', 'scaler': QuantileTransformer(random_state=42)}
Random State usado: 758
removed_features = ["Estatura", "Treino tradicional", "MQ PRE", "Massa"]
