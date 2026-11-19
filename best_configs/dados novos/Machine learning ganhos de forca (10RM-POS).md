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

       ====== MODELO 1 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.5864
Métrica (CV - MAE)           0.9947
Métrica (CV - MSE)           1.5392
Métrica (CV - RMSE)          1.2330
Desvio Padrão (CV - rmse)    0.1372
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.8576
MAE      : 1.0010
MSE      : 1.7173
RMSE     : 1.3105

Parâmetros: {'clf': Ridge(), 'clf__alpha': 0.5, 'clf__fit_intercept': True, 'reducao': PCA(n_components=0.95, random_state=31), 'scaler': QuantileTransformer(random_state=42)}
Random State usado: 416

        ====== MODELO 1 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.5172
Métrica (CV - MAE)           1.0706
Métrica (CV - MSE)           1.8892
Métrica (CV - RMSE)          1.3566
Desvio Padrão (CV - rmse)    0.2207
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.8496
MAE      : 0.9898
MSE      : 1.2166
RMSE     : 1.1030

Parâmetros: {'clf': ElasticNet(random_state=42), 'clf__alpha': 0.1, 'clf__fit_intercept': True, 'clf__l1_ratio': 0.3, 'reducao': 'passthrough', 'scaler': StandardScaler()}
Random State usado: 19


        ====== MODELO 1 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.6342
Métrica (CV - MAE)           1.1278
Métrica (CV - MSE)           1.9918
Métrica (CV - RMSE)          1.3842
Desvio Padrão (CV - rmse)    0.2753
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.8985
MAE      : 0.6262
MSE      : 0.6759
RMSE     : 0.8222

Parâmetros: {'clf': SVR(), 'clf__C': 100, 'clf__gamma': 'scale', 'clf__kernel': 'linear', 'reducao': PCA(n_components=0.99, random_state=31), 'scaler': PowerTransformer()}
Random State usado: 202

        ====== MODELO 5 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.4273
Métrica (CV - MAE)           1.1732
Métrica (CV - MSE)           2.0479
Métrica (CV - RMSE)          1.4120
Desvio Padrão (CV - rmse)    0.2328
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.9197
MAE      : 0.7735
MSE      : 0.8242
RMSE     : 0.9078

Parâmetros: {'clf': SVR(), 'clf__C': 75, 'clf__gamma': 'auto', 'clf__kernel': 'rbf', 'reducao': PCA(n_components=0.99, random_state=31), 'scaler': MaxAbsScaler()}
Random State usado: 468

       ====== MODELO 6 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.5032
Métrica (CV - MAE)           1.2953
Métrica (CV - MSE)           2.7615
Métrica (CV - RMSE)          1.6510
Desvio Padrão (CV - rmse)    0.1887
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.7994
MAE      : 0.9569
MSE      : 1.8179
RMSE     : 1.3483

Parâmetros: {'clf': RandomForestRegressor(random_state=42), 'clf__ccp_alpha': 0.01, 'clf__criterion': 'squared_error', 'clf__max_depth': None, 'clf__min_samples_split': 5, 'clf__n_estimators': 145, 'reducao': 'passthrough', 'scaler': None}
Random State usado: 841

       ====== MODELO 2 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.4320
Métrica (CV - MAE)           1.3464
Métrica (CV - MSE)           3.1309
Métrica (CV - RMSE)          1.7447
Desvio Padrão (CV - rmse)    0.2950
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.8132
MAE      : 1.1707
MSE      : 1.9217
RMSE     : 1.3863

Parâmetros: {'clf': GradientBoostingRegressor(random_state=42), 'clf__learning_rate': 0.125, 'clf__loss': 'absolute_error', 'clf__max_depth': 4, 'clf__n_estimators': 125, 'reducao': 'passthrough', 'scaler': None}
Random State usado: 352
