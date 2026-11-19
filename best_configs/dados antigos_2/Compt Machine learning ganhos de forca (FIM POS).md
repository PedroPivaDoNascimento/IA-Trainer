        
        ====== MODELO 3 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.3727
Métrica (CV - MAE)           2.8009
Métrica (CV - MSE)           13.3597
Métrica (CV - RMSE)          3.5224
Desvio Padrão (CV - rmse)    0.9760
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.8965
MAE      : 1.5264
MSE      : 3.4069
RMSE     : 1.8458

Parâmetros: {'clf': LinearRegression(), 'clf__fit_intercept': True, 'clf__positive': False, 'reducao': 'passthrough', 'scaler': RobustScaler()}
Random State usado: 991


            MELHOR
        ====== MODELO 2 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.5629
Métrica (CV - MAE)           2.4936
Métrica (CV - MSE)           10.3426
Métrica (CV - RMSE)          3.0696
Desvio Padrão (CV - rmse)    0.9593
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.9089
MAE      : 1.2119
MSE      : 2.1932
RMSE     : 1.4809

Parâmetros: {'clf': Ridge(), 'clf__alpha': 0.9, 'clf__fit_intercept': True, 'reducao': 'passthrough', 'scaler': RobustScaler(quantile_range=(30, 70))}
Random State usado: 202

        ====== MODELO 2 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.3996
Métrica (CV - MAE)           2.5303
Métrica (CV - MSE)           11.0011
Métrica (CV - RMSE)          3.1921
Desvio Padrão (CV - rmse)    0.9010
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.8751
MAE      : 1.4052
MSE      : 3.6157
RMSE     : 1.9015

Parâmetros: {'clf': ElasticNet(random_state=42), 'clf__alpha': 0.1, 'clf__fit_intercept': True, 'clf__l1_ratio': 0.7, 'reducao': 'passthrough', 'scaler': RobustScaler()}
Random State usado: 708

        ====== MODELO 6 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.5608
Métrica (CV - MAE)           2.1438
Métrica (CV - MSE)           9.3392
Métrica (CV - RMSE)          2.8983
Desvio Padrão (CV - rmse)    0.9691
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.7639
MAE      : 1.9642
MSE      : 6.4366
RMSE     : 2.5370

Parâmetros: {'clf': SVR(), 'clf__C': 60, 'clf__gamma': 'scale', 'clf__kernel': 'linear', 'reducao': PCA(n_components=0.99, random_state=31), 'scaler': MaxAbsScaler()}
Random State usado: 938

        ====== MODELO 5 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.5792
Métrica (CV - MAE)           2.2909
Métrica (CV - MSE)           9.9858
Métrica (CV - RMSE)          3.0523
Desvio Padrão (CV - rmse)    0.8181
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.8181
MAE      : 1.8852
MSE      : 5.7705
RMSE     : 2.4022

Parâmetros: {'clf': SVR(), 'clf__C': 60, 'clf__gamma': 'auto', 'clf__kernel': 'rbf', 'reducao': 'passthrough', 'scaler': MinMaxScaler()}
Random State usado: 140

        ====== MODELO 8 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.4613
Métrica (CV - MAE)           2.8784
Métrica (CV - MSE)           14.7132
Métrica (CV - RMSE)          3.5922
Desvio Padrão (CV - rmse)    1.3452
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.7198
MAE      : 1.6185
MSE      : 4.1708
RMSE     : 2.0423

Parâmetros: {'clf': RandomForestRegressor(random_state=42), 'clf__ccp_alpha': 0.01, 'clf__criterion': 'squared_error', 'clf__max_depth': None, 'clf__min_samples_split': 5, 'clf__n_estimators': 145, 'reducao': 'passthrough', 'scaler': None}
Random State usado: 142

        ====== MODELO 4 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.5026
Métrica (CV - MAE)           2.8180
Métrica (CV - MSE)           12.4251
Métrica (CV - RMSE)          3.4743
Desvio Padrão (CV - rmse)    0.5952
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.7728
MAE      : 1.9191
MSE      : 5.1464
RMSE     : 2.2686

Parâmetros: {'clf': GradientBoostingRegressor(random_state=42), 'clf__learning_rate': 0.125, 'clf__loss': 'absolute_error', 'clf__max_depth': 4, 'clf__n_estimators': 125, 'reducao': PCA(n_components=0.95, random_state=31), 'scaler': None}
Random State usado: 613