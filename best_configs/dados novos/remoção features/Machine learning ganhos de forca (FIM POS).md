        ====== MODELO 1 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.5863
Métrica (CV - MAE)           2.3862
Métrica (CV - MSE)           9.8000
Métrica (CV - RMSE)          2.9970
Desvio Padrão (CV - rmse)    0.9043
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.9228
MAE      : 0.9903
MSE      : 1.8592
RMSE     : 1.3635

Parâmetros: {'clf': Ridge(), 'clf__alpha': 0.9, 'clf__fit_intercept': True, 'reducao': 'passthrough', 'scaler': RobustScaler(quantile_range=(30, 70))}
Random State usado: 202
removed_features = ["1RM-PRE", "MT PRE", "MQ PRE"]
