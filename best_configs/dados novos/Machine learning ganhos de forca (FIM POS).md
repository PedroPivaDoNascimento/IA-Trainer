        ====== MODELO 1 ======

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


        ====== MODELO 1 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.5634
Métrica (CV - MAE)           2.4845
Métrica (CV - MSE)           10.3356
Métrica (CV - RMSE)          3.0644
Desvio Padrão (CV - rmse)    0.9723
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.9096
MAE      : 1.2125
MSE      : 2.1772
RMSE     : 1.4755

Parâmetros: {'clf': Ridge(), 'clf__alpha': 0.9, 'clf__fit_intercept': True, 'reducao': 'passthrough', 'scaler': RobustScaler(quantile_range=(30, 70))}
Random State usado: 202

        ====== MODELO 1 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.4011
Métrica (CV - MAE)           2.5183
Métrica (CV - MSE)           10.9669
Métrica (CV - RMSE)          3.1830
Desvio Padrão (CV - rmse)    0.9141
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.8748
MAE      : 1.4035
MSE      : 3.6243
RMSE     : 1.9038

Parâmetros: {'clf': ElasticNet(random_state=42), 'clf__alpha': 0.1, 'clf__fit_intercept': True, 'clf__l1_ratio': 0.7, 'reducao': 'passthrough', 'scaler': RobustScaler()}
Random State usado: 708

       ====== MODELO 7 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.5270
Métrica (CV - MAE)           2.2864
Métrica (CV - MSE)           9.8855
Métrica (CV - RMSE)          3.0873
Desvio Padrão (CV - rmse)    0.5952
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.8257
MAE      : 1.9852
MSE      : 6.3022
RMSE     : 2.5104

Parâmetros: {'clf': SVR(), 'clf__C': 60, 'clf__gamma': 'scale', 'clf__kernel': 'linear', 'reducao': PCA(n_components=0.99, random_state=31), 'scaler': MaxAbsScaler()}
Random State usado: 695

        ====== MODELO 10 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.3668
Métrica (CV - MAE)           2.4819
Métrica (CV - MSE)           11.0132
Métrica (CV - RMSE)          3.2864
Desvio Padrão (CV - rmse)    0.4613
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.8345
MAE      : 1.6393
MSE      : 4.7119
RMSE     : 2.1707

Parâmetros: {'clf': SVR(), 'clf__C': 60, 'clf__gamma': 'auto', 'clf__kernel': 'rbf', 'reducao': 'passthrough', 'scaler': MinMaxScaler()}
Random State usado: 887

        ====== MODELO 8 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.2789
Métrica (CV - MAE)           3.0520
Métrica (CV - MSE)           15.0334
Métrica (CV - RMSE)          3.7689
Desvio Padrão (CV - rmse)    0.9105
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.7969
MAE      : 1.2876
MSE      : 2.2227
RMSE     : 1.4909

Parâmetros: {'clf': RandomForestRegressor(random_state=42), 'clf__ccp_alpha': 0.01, 'clf__criterion': 'squared_error', 'clf__max_depth': None, 'clf__min_samples_split': 5, 'clf__n_estimators': 145, 'reducao': 'passthrough', 'scaler': None}
Random State usado: 936

       ====== MODELO 1 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.4950
Métrica (CV - MAE)           2.8572
Métrica (CV - MSE)           12.5801
Métrica (CV - RMSE)          3.4990
Desvio Padrão (CV - rmse)    0.5807
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.8312
MAE      : 1.4759
MSE      : 3.8238
RMSE     : 1.9555

Parâmetros: {'clf': GradientBoostingRegressor(random_state=42), 'clf__learning_rate': 0.125, 'clf__loss': 'absolute_error', 'clf__max_depth': 4, 'clf__n_estimators': 125, 'reducao': PCA(n_components=0.95, random_state=31), 'scaler': None}
Random State usado: 613