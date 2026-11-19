        ====== MODELO 8 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.5785
Métrica (CV - MAE)           1.3970
Métrica (CV - MSE)           3.1704
Métrica (CV - RMSE)          1.6865
Desvio Padrão (CV - rmse)    0.5710
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.8978
MAE      : 0.9073
MSE      : 1.2078
RMSE     : 1.0990

Parâmetros: {'clf': LinearRegression(), 'clf__fit_intercept': True, 'clf__positive': False, 'reducao': PCA(n_components=0.95, random_state=31), 'scaler': RobustScaler(quantile_range=(10, 90))}
Random State usado: 857

         ====== MODELO 3 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.6488
Métrica (CV - MAE)           1.2439
Métrica (CV - MSE)           2.7092
Métrica (CV - RMSE)          1.6332
Desvio Padrão (CV - rmse)    0.2048
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.8984
MAE      : 0.8551
MSE      : 1.2508
RMSE     : 1.1184

Parâmetros: {'clf': Ridge(), 'clf__alpha': 0.25, 'clf__fit_intercept': False, 'reducao': 'passthrough', 'scaler': MaxAbsScaler()}
Random State usado: 775

        ====== MODELO 6 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.5151
Métrica (CV - MAE)           1.4158
Métrica (CV - MSE)           3.6191
Métrica (CV - RMSE)          1.8301
Desvio Padrão (CV - rmse)    0.5193
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.8771
MAE      : 0.8402
MSE      : 1.1735
RMSE     : 1.0833

Parâmetros: {'clf': ElasticNet(random_state=42), 'clf__alpha': 0.1, 'clf__fit_intercept': True, 'clf__l1_ratio': 0.7, 'reducao': 'passthrough', 'scaler': StandardScaler()}
Random State usado: 863

        ====== MODELO 6 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.0592
Métrica (CV - MAE)           1.4171
Métrica (CV - MSE)           3.3059
Métrica (CV - RMSE)          1.7877
Desvio Padrão (CV - rmse)    0.3318
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.9042
MAE      : 1.0276
MSE      : 1.9417
RMSE     : 1.3935

Parâmetros: {'clf': SVR(), 'clf__C': 60, 'clf__gamma': 'scale', 'clf__kernel': 'linear', 'reducao': PCA(n_components=0.97, random_state=31), 'scaler': StandardScaler()}
Random State usado: 781


        ====== MODELO 9 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.6618
Métrica (CV - MAE)           1.2947
Métrica (CV - MSE)           2.7233
Métrica (CV - RMSE)          1.6379
Desvio Padrão (CV - rmse)    0.2015
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.8922
MAE      : 0.8402
MSE      : 1.2234
RMSE     : 1.1061

Parâmetros: {'clf': SVR(), 'clf__C': 60, 'clf__gamma': 'auto', 'clf__kernel': 'rbf', 'reducao': PCA(n_components=0.97, random_state=31), 'scaler': MaxAbsScaler()}
Random State usado: 288

        ====== MODELO 4 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.1579
Métrica (CV - MAE)           1.7886
Métrica (CV - MSE)           5.5590
Métrica (CV - RMSE)          2.3259
Desvio Padrão (CV - rmse)    0.3859
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.7053
MAE      : 1.5778
MSE      : 3.9035
RMSE     : 1.9757

Parâmetros: {'clf': RandomForestRegressor(random_state=42), 'clf__ccp_alpha': 0.01, 'clf__criterion': 'squared_error', 'clf__max_depth': None, 'clf__min_samples_split': 5, 'clf__n_estimators': 145, 'reducao': 'passthrough', 'scaler': None}
Random State usado: 268

        ====== MODELO 2 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.4284
Métrica (CV - MAE)           1.6946
Métrica (CV - MSE)           4.6698
Métrica (CV - RMSE)          2.1402
Desvio Padrão (CV - rmse)    0.2987
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.7794
MAE      : 1.0903
MSE      : 2.0989
RMSE     : 1.4487

Parâmetros: {'clf': GradientBoostingRegressor(random_state=42), 'clf__learning_rate': 0.125, 'clf__loss': 'absolute_error', 'clf__max_depth': 4, 'clf__n_estimators': 125, 'reducao': 'passthrough', 'scaler': None}
Random State usado: 123