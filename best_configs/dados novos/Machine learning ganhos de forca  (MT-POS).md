        ====== MODELO 6 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.6804
Métrica (CV - MAE)           1.3004
Métrica (CV - MSE)           2.7361
Métrica (CV - RMSE)          1.6247
Desvio Padrão (CV - rmse)    0.3105
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.9079
MAE      : 0.8283
MSE      : 0.8685
RMSE     : 0.9320

Parâmetros: {'clf': LinearRegression(), 'clf__fit_intercept': True, 'clf__positive': False, 'reducao': PCA(n_components=0.99, random_state=31), 'scaler': MinMaxScaler()}
Random State usado: 704

        ====== MODELO 3 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.7733
Métrica (CV - MAE)           1.1655
Métrica (CV - MSE)           2.1025
Métrica (CV - RMSE)          1.3992
Desvio Padrão (CV - rmse)    0.3804
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.9123
MAE      : 0.9073
MSE      : 1.1868
RMSE     : 1.0894

Parâmetros: {'clf': Ridge(), 'clf__alpha': 0.75, 'clf__fit_intercept': True, 'clf__tol': 0.00055, 'reducao': 'passthrough', 'scaler': RobustScaler(quantile_range=(20, 80))}
Random State usado: 233

         ====== MODELO 1 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.7608
Métrica (CV - MAE)           1.2133
Métrica (CV - MSE)           2.0694
Métrica (CV - RMSE)          1.3924
Desvio Padrão (CV - rmse)    0.3616
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.9122
MAE      : 0.7211
MSE      : 0.9545
RMSE     : 0.9770

Parâmetros: {'clf': ElasticNet(random_state=42), 'clf__alpha': 0.1, 'clf__fit_intercept': True, 'clf__l1_ratio': 0.7, 'reducao': 'passthrough', 'scaler': PowerTransformer()}
Random State usado: 567

        ====== MODELO 1 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.5547
Métrica (CV - MAE)           1.3538
Métrica (CV - MSE)           2.7740
Métrica (CV - RMSE)          1.5945
Desvio Padrão (CV - rmse)    0.4811
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.9204
MAE      : 0.9122
MSE      : 1.2245
RMSE     : 1.1066

Parâmetros: {'clf': SVR(), 'clf__C': 50, 'clf__gamma': 'scale', 'clf__kernel': 'linear', 'reducao': PCA(n_components=0.98, random_state=31), 'scaler': StandardScaler()}
Random State usado: 462

         ====== MODELO 1 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.7636
Métrica (CV - MAE)           1.2390
Métrica (CV - MSE)           2.4183
Métrica (CV - RMSE)          1.4647
Desvio Padrão (CV - rmse)    0.5223
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.9045
MAE      : 0.8361
MSE      : 0.9760
RMSE     : 0.9879

Parâmetros: {'clf': SVR(), 'clf__C': 75, 'clf__gamma': 'auto', 'clf__kernel': 'rbf', 'reducao': PCA(n_components=0.99, random_state=31), 'scaler': MaxAbsScaler()}
Random State usado: 214

        ====== MODELO 1 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.5848
Métrica (CV - MAE)           1.5771
Métrica (CV - MSE)           3.7849
Métrica (CV - RMSE)          1.9198
Desvio Padrão (CV - rmse)    0.3147
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.8528
MAE      : 0.8757
MSE      : 1.2976
RMSE     : 1.1391

Parâmetros: {'clf': RandomForestRegressor(random_state=42), 'clf__ccp_alpha': 0.01, 'clf__criterion': 'squared_error', 'clf__max_depth': None, 'clf__min_samples_split': 5, 'clf__n_estimators': 145, 'reducao': 'passthrough', 'scaler': None}
Random State usado: 620

         ====== MODELO 1 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.5589
Métrica (CV - MAE)           1.5239
Métrica (CV - MSE)           3.5972
Métrica (CV - RMSE)          1.8448
Desvio Padrão (CV - rmse)    0.4402
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.8877
MAE      : 1.0007
MSE      : 1.6361
RMSE     : 1.2791

Parâmetros: {'clf': GradientBoostingRegressor(random_state=42), 'clf__learning_rate': 0.125, 'clf__loss': 'absolute_error', 'clf__max_depth': 4, 'clf__n_estimators': 125, 'reducao': 'passthrough', 'scaler': None}
Random State usado: 301