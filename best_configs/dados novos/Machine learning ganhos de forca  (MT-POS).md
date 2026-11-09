        ====== MODELO 8 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.7690
Métrica (CV - MAE)           1.0912
Métrica (CV - MSE)           1.9169
Métrica (CV - RMSE)          1.3601
Desvio Padrão (CV - rmse)    0.2588
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.8806
MAE      : 1.1125
MSE      : 1.8498
RMSE     : 1.3601

Parâmetros: {'clf': LinearRegression(), 'clf__fit_intercept': True, 'clf__positive': False, 'reducao': PCA(n_components=0.99, random_state=31), 'scaler': MinMaxScaler()}
Random State usado: 938

        ====== MODELO 3 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.7379
Métrica (CV - MAE)           1.2007
Métrica (CV - MSE)           2.1983
Métrica (CV - RMSE)          1.4550
Desvio Padrão (CV - rmse)    0.2850
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.9102
MAE      : 0.8431
MSE      : 1.2709
RMSE     : 1.1273

Parâmetros: {'clf': Ridge(), 'clf__alpha': 0.75, 'clf__fit_intercept': True, 'clf__tol': 0.00055, 'reducao': 'passthrough', 'scaler': RobustScaler(quantile_range=(20, 80))}
Random State usado: 102


        ====== MODELO 7 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.7614
Métrica (CV - MAE)           1.2087
Métrica (CV - MSE)           2.0631
Métrica (CV - RMSE)          1.3893
Desvio Padrão (CV - rmse)    0.3647
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.9118
MAE      : 0.7217
MSE      : 0.9588
RMSE     : 0.9792

Parâmetros: {'clf': ElasticNet(random_state=42), 'clf__alpha': 0.1, 'clf__fit_intercept': True, 'clf__l1_ratio': 0.7, 'reducao': 'passthrough', 'scaler': PowerTransformer()}
Random State usado: 567

               
                MELHOR
        ====== MODELO 7 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.5517
Métrica (CV - MAE)           1.3549
Métrica (CV - MSE)           2.7845
Métrica (CV - RMSE)          1.5967
Desvio Padrão (CV - rmse)    0.4848
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.9204
MAE      : 0.9123
MSE      : 1.2253
RMSE     : 1.1069

Parâmetros: {'clf': SVR(), 'clf__C': 50, 'clf__gamma': 'scale', 'clf__kernel': 'linear', 'reducao': PCA(n_components=0.98, random_state=31), 'scaler': StandardScaler()}
Random State usado: 462

        ====== MODELO 7 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.7761
Métrica (CV - MAE)           1.2148
Métrica (CV - MSE)           2.2927
Métrica (CV - RMSE)          1.4334
Desvio Padrão (CV - rmse)    0.4881
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.8929
MAE      : 0.8806
MSE      : 1.0948
RMSE     : 1.0463

Parâmetros: {'clf': SVR(), 'clf__C': 75, 'clf__gamma': 'auto', 'clf__kernel': 'rbf', 'reducao': PCA(n_components=0.99, random_state=31), 'scaler': MaxAbsScaler()}
Random State usado: 214

        ====== MODELO 3 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.5881
Métrica (CV - MAE)           1.5749
Métrica (CV - MSE)           3.7532
Métrica (CV - RMSE)          1.9118
Desvio Padrão (CV - rmse)    0.3135
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.8523
MAE      : 0.8723
MSE      : 1.3020
RMSE     : 1.1410

Parâmetros: {'clf': RandomForestRegressor(random_state=42), 'clf__ccp_alpha': 0.01, 'clf__criterion': 'squared_error', 'clf__max_depth': None, 'clf__min_samples_split': 5, 'clf__n_estimators': 145, 'reducao': 'passthrough', 'scaler': None}
Random State usado: 620

        ====== MODELO 9 ======

============================================================
MELHOR MODELO — OTIMIZADO POR: RMSE
============================================================
Métrica (CV - R2 Score)      0.5164
Métrica (CV - MAE)           1.6324
Métrica (CV - MSE)           4.0139
Métrica (CV - RMSE)          1.9618
Desvio Padrão (CV - rmse)    0.4066
------------------------------------------------------------
=== Relatório de Avaliação no Teste ===
R2 Score : 0.9026
MAE      : 0.9192
MSE      : 1.4185
RMSE     : 1.1910

Parâmetros: {'clf': GradientBoostingRegressor(random_state=42), 'clf__learning_rate': 0.125, 'clf__loss': 'absolute_error', 'clf__max_depth': 4, 'clf__n_estimators': 125, 'reducao': 'passthrough', 'scaler': None}
Random State usado: 301