### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 01/09/2026, 13:58:03*

**[REMOVED]**
```
(from line ~21)
    DATA_PATH = "./planilhas/Machine learning ganhos de forca (10RM-POS).xlsx"

```
**[ADDED]**
```
21        DATA_PATH = "./planilhas/Machine learning ganhos de forca (FIM POS).xlsx"
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/save.txt
*Saved at: 01/09/2026, 13:57:45*

**[REMOVED]**
```
(from line ~112)
Tempo gasto em minutos: 0.13
```
**[ADDED]**
```
112   Tempo gasto em minutos: 0.13
113   
114   
115   
116   
117   
118    Melhores modelos:
119   
120           ====== MODELO 1 ======
121   
122   ============================================================
123   MELHOR MODELO — OTIMIZADO POR: RMSE
124   ============================================================
125   Métrica (CV - R2 Score)      0.7663
126   Métrica (CV - MAE)           0.9890
127   Métrica (CV - MSE)           1.5034
128   Métrica (CV - RMSE)          1.2174
129   Desvio Padrão (CV - rmse)    0.1459
130   ------------------------------------------------------------
131   === Relatório de Avaliação no Teste ===
132   R2 Score : 0.8544
133   MAE      : 0.7604
134   MSE      : 0.9082
135   RMSE     : 0.9530
136   
137   Parâmetros: {'clf': LinearRegression(), 'reducao': PCA(n_components=0.99, random_state=31), 'scaler': QuantileTransformer(random_state=42)}
138   Random State usado: 923
139   
140           ====== MODELO 2 ======
141   
142   ============================================================
143   MELHOR MODELO — OTIMIZADO POR: RMSE
144   ============================================================
145   Métrica (CV - R2 Score)      0.7875
146   Métrica (CV - MAE)           0.8998
147   Métrica (CV - MSE)           1.2462
148   Métrica (CV - RMSE)          1.1118
149   Desvio Padrão (CV - rmse)    0.1001
150   ------------------------------------------------------------
151   === Relatório de Avaliação no Teste ===
152   R2 Score : 0.7921
153   MAE      : 0.9314
154   MSE      : 1.5220
155   RMSE     : 1.2337
156   
157   Parâmetros: {'clf': LinearRegression(), 'reducao': PCA(n_components=0.99, random_state=31), 'scaler': QuantileTransformer(random_state=42)}
158   Random State usado: 737
159   
160           ====== MODELO 3 ======
161   
162   ============================================================
163   MELHOR MODELO — OTIMIZADO POR: RMSE
164   ============================================================
165   Métrica (CV - R2 Score)      0.7593
166   Métrica (CV - MAE)           0.9719
167   Métrica (CV - MSE)           1.4560
168   Métrica (CV - RMSE)          1.2035
169   Desvio Padrão (CV - rmse)    0.0868
170   ------------------------------------------------------------
171   === Relatório de Avaliação no Teste ===
172   R2 Score : 0.8806
173   MAE      : 0.7194
174   MSE      : 0.7674
175   RMSE     : 0.8760
176   
177   Parâmetros: {'clf': LinearRegression(), 'reducao': 'passthrough', 'scaler': PowerTransformer()}
178   Random State usado: 326
179   
180           ====== MODELO 4 ======
181   
182   ============================================================
183   MELHOR MODELO — OTIMIZADO POR: RMSE
184   ============================================================
185   Métrica (CV - R2 Score)      0.7797
186   Métrica (CV - MAE)           0.8835
187   Métrica (CV - MSE)           1.3030
188   Métrica (CV - RMSE)          1.1052
189   Desvio Padrão (CV - rmse)    0.2853
190   ------------------------------------------------------------
191   === Relatório de Avaliação no Teste ===
192   R2 Score : 0.8452
193   MAE      : 1.0117
194   MSE      : 1.4432
195   RMSE     : 1.2013
196   
197   Parâmetros: {'clf': LinearRegression(), 'reducao': PCA(n_components=0.99, random_state=31), 'scaler': StandardScaler()}
198   Random State usado: 774
199   
200           ====== MODELO 5 ======
201   
202   ============================================================
203   MELHOR MODELO — OTIMIZADO POR: RMSE
204   ============================================================
205   Métrica (CV - R2 Score)      0.8111
206   Métrica (CV - MAE)           0.8674
207   Métrica (CV - MSE)           1.1684
208   Métrica (CV - RMSE)          1.0711
209   Desvio Padrão (CV - rmse)    0.1452
210   ------------------------------------------------------------
211   === Relatório de Avaliação no Teste ===
212   R2 Score : 0.6812
213   MAE      : 1.1001
214   MSE      : 1.9289
215   RMSE     : 1.3888
216   
217   Parâmetros: {'clf': LinearRegression(), 'reducao': PCA(n_components=0.99, random_state=31), 'scaler': PowerTransformer()}
218   Random State usado: 354
219   
220   ============================================================
221   CLASSIFICATION REPORT (MÉDIA GERAL)
222   ============================================================
223   === Média Métrica Final (Múltiplas Rodadas) ===
224   R2 Score Médio : 0.8107
225   MAE Médio      : 0.9046
226   MSE Médio      : 1.2223
227   RMSE Médio     : 0.0000
228   ============================================================
229   Tempo gasto em minutos: 0.12
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 01/09/2026, 13:56:09*

**[REMOVED]**
```
(from line ~21)
    DATA_PATH = "./planilhas/Machine learning ganhos de forca (1RM-POS).xlsx"

```
**[ADDED]**
```
21        DATA_PATH = "./planilhas/Machine learning ganhos de forca (10RM-POS).xlsx"
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/save.txt
*Saved at: 01/09/2026, 13:55:35*

**[ADDED]**
```
1      Melhores modelos:
2     
3             ====== MODELO 1 ======
4     
5     ============================================================
6     MELHOR MODELO — OTIMIZADO POR: RMSE
7     ============================================================
8     Métrica (CV - R2 Score)      0.7544
9     Métrica (CV - MAE)           1.2193
10    Métrica (CV - MSE)           2.3279
11    Métrica (CV - RMSE)          1.5069
12    Desvio Padrão (CV - rmse)    0.2392
13    ------------------------------------------------------------
14    === Relatório de Avaliação no Teste ===
15    R2 Score : 0.7447
16    MAE      : 1.1918
17    MSE      : 2.7963
18    RMSE     : 1.6722
19    
20    Parâmetros: {'clf': LinearRegression(), 'reducao': PCA(n_components=0.99, random_state=31), 'scaler': PowerTransformer()}
21    Random State usado: 304
22    
23            ====== MODELO 2 ======
24    
25    ============================================================
26    MELHOR MODELO — OTIMIZADO POR: RMSE
27    ============================================================
28    Métrica (CV - R2 Score)      0.7997
29    Métrica (CV - MAE)           1.1443
30    Métrica (CV - MSE)           2.2136
31    Métrica (CV - RMSE)          1.4796
32    Desvio Padrão (CV - rmse)    0.1557
33    ------------------------------------------------------------
34    === Relatório de Avaliação no Teste ===
35    R2 Score : 0.6580
36    MAE      : 1.2198
37    MSE      : 2.5945
38    RMSE     : 1.6108
39    
40    Parâmetros: {'clf': LinearRegression(), 'reducao': PCA(n_components=0.95, random_state=31), 'scaler': StandardScaler()}
41    Random State usado: 825
42    
43            ====== MODELO 3 ======
44    
45    ============================================================
46    MELHOR MODELO — OTIMIZADO POR: RMSE
47    ============================================================
48    Métrica (CV - R2 Score)      0.7386
49    Métrica (CV - MAE)           1.1696
50    Métrica (CV - MSE)           2.4454
51    Métrica (CV - RMSE)          1.5538
52    Desvio Padrão (CV - rmse)    0.1765
53    ------------------------------------------------------------
54    === Relatório de Avaliação no Teste ===
55    R2 Score : 0.7691
56    MAE      : 1.1989
57    MSE      : 2.3102
58    RMSE     : 1.5199
59    
60    Parâmetros: {'clf': LinearRegression(), 'reducao': PCA(n_components=0.99, random_state=31), 'scaler': RobustScaler()}
61    Random State usado: 991
62    
63            ====== MODELO 4 ======
64    
65    ============================================================
66    MELHOR MODELO — OTIMIZADO POR: RMSE
67    ============================================================
68    Métrica (CV - R2 Score)      0.7139
69    Métrica (CV - MAE)           1.3300
70    Métrica (CV - MSE)           2.9172
71    Métrica (CV - RMSE)          1.6928
72    Desvio Padrão (CV - rmse)    0.2274
73    ------------------------------------------------------------
74    === Relatório de Avaliação no Teste ===
75    R2 Score : 0.8508
76    MAE      : 1.0522
77    MSE      : 1.4876
78    RMSE     : 1.2197
79    
80    Parâmetros: {'clf': LinearRegression(), 'reducao': PCA(n_components=0.95, random_state=31), 'scaler': PowerTransformer()}
81    Random State usado: 112
82    
83            ====== MODELO 5 ======
84    
85    ============================================================
86    MELHOR MODELO — OTIMIZADO POR: RMSE
87    ============================================================
88    Métrica (CV - R2 Score)      0.7128
89    Métrica (CV - MAE)           1.2314
90    Métrica (CV - MSE)           2.5872
91    Métrica (CV - RMSE)          1.5954
92    Desvio Padrão (CV - rmse)    0.2045
93    ------------------------------------------------------------
94    === Relatório de Avaliação no Teste ===
95    R2 Score : 0.8684
96    MAE      : 0.8803
97    MSE      : 1.2773
98    RMSE     : 1.1302
99    
100   Parâmetros: {'clf': LinearRegression(), 'reducao': PCA(n_components=0.99, random_state=31), 'scaler': MinMaxScaler()}
101   Random State usado: 449
102   
103   ============================================================
104   CLASSIFICATION REPORT (MÉDIA GERAL)
105   ============================================================
106   === Média Métrica Final (Múltiplas Rodadas) ===
107   R2 Score Médio : 0.7782
108   MAE Médio      : 1.1086
109   MSE Médio      : 1.7619
110   RMSE Médio     : 0.0000
111   ============================================================
112   Tempo gasto em minutos: 0.13
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 01/09/2026, 13:46:02*

**[REMOVED]**
```
(from line ~52)
            #PCA(n_components=0.99, random_state=31),

```
**[ADDED]**
```
52                PCA(n_components=0.99, random_state=31),
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 01/09/2026, 13:42:12*

**[ADDED]**
```
107               #{
108               #     "clf": [KNeighborsRegressor()],
109               #     "clf__n_neighbors": [3, 5, 7, 9, 11, 13, 15, 17, 19],
110               #     "clf__weights": ["uniform", "distance"],
111               #     "clf__metric": ["euclidean", "manhattan"],
112               #     "scaler": scalers,
113               #     "reducao": reducoes,
114               #},
```
**[REMOVED]**
```
(from line ~116)
                 "clf": [KNeighborsRegressor()],
                 "clf__n_neighbors": [3, 5, 7, 9, 11, 13, 15, 17, 19],
                 "clf__weights": ["uniform", "distance"],
                 "clf__metric": ["euclidean", "manhattan"],
                 "scaler": scalers,
                 "reducao": reducoes,
            },
            {

```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 01/09/2026, 13:29:08*

**[REMOVED]**
```
(from line ~30)
        iterations=10,

```
**[ADDED]**
```
30            iterations=5,
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 01/09/2026, 13:22:51*

**[ADDED]**
```
107               {
108                    "clf": [KNeighborsRegressor()],
109                    "clf__n_neighbors": [3, 5, 7, 9, 11, 13, 15, 17, 19],
110                    "clf__weights": ["uniform", "distance"],
111                    "clf__metric": ["euclidean", "manhattan"],
112                    "scaler": scalers,
113                    "reducao": reducoes,
114               },
115               {
116                   "clf": [LinearRegression()],
117                   "scaler": scalers,
118                   "reducao": reducoes,
119               },
```
**[REMOVED]**
```
(from line ~121)
            #     "clf": [KNeighborsRegressor()],
            #     "clf__n_neighbors": [3, 5, 7, 9, 11, 13, 15, 17, 19],
            #     "clf__weights": ["uniform", "distance"],
            #     "clf__metric": ["euclidean", "manhattan"],
            #     "scaler": scalers,
            #     "reducao": reducoes,
            #},
            #{
            #    "clf": [LinearRegression()],
            #    "scaler": scalers,
            #    "reducao": reducoes,
            #},
            #{

```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 01/09/2026, 13:10:20*

**[REMOVED]**
```
(from line ~68)
            # {
            #     "clf": [SGDRegressor(random_state=42)],
            #     "clf__eta0": [0.1, 0.01, 0.001],
            #     "clf__penalty": ["l2", "l1", "elasticnet"],
            #     "scaler": scalers,
            #     "reducao": ["passthrough"],
            # },
            #  {
            #      "scaler": scalers,
            #      "reducao": reducoes,
            #      "clf": [MLPRegressor(random_state=31)],
            #      "clf__activation": [
            #          "tanh",
            #          "relu"
            #      ],
            #      "clf__hidden_layer_sizes": [
            #          (24,),
            #          (32,),
            #          #(40,),
            #          #(48,),
            #          #(24, 12),
            #          #(32, 16)
            #      ],
            #      "clf__alpha": [
            #          0.00005,
            #          0.0001,
            #          #0.0002,
            #          #0.0005,
            #          #0.01
            #      ],
            #      "clf__learning_rate_init": [
            #          #0.005,
            #          #0.0075,
            #          0.01,
            #          0.015,
            #          #0.1
            #      ],
            #      "clf__early_stopping": [True],
            #      "clf__validation_fraction": [
            #          0.08, 
            #          0.10, 
            #          #0.12, 
            #          #0.15
            #      ],
            #      "clf__max_iter": [
            #          500,
            #          1000,
            #          #1500
            #      ],
            #      "clf__n_iter_no_change": [
            #          10, 
            #          15, 
            #          #20
            #      ],
            #      "clf__tol": [
            #          0.0001, 
            #          0.00005
            #      ]
            #  },

```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 01/09/2026, 13:09:44*

**[REMOVED]**
```
(from line ~142)
            {
                "clf": [RandomForestRegressor(random_state=42)],
                "clf__n_estimators": [100, 300, 500],
                "clf__max_depth": [None, 10, 20],
                "clf__criterion": ["squared_error", "absolute_error"],
                "scaler": [None],
                "reducao": ["passthrough"],
            },

```
**[ADDED]**
```
143               #    "clf": [RandomForestRegressor(random_state=42)],
144               #    "clf__n_estimators": [100, 300, 500],
145               #    "clf__max_depth": [None, 10, 20],
146               #    "clf__criterion": ["squared_error", "absolute_error"],
147               #    "scaler": [None],
148               #    "reducao": ["passthrough"],
149               #},
150               #{
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 01/09/2026, 13:09:38*

**[REMOVED]**
```
(from line ~33)
    controller.run_data_analysis()
    #controller.run()

```
**[ADDED]**
```
33        #controller.run_data_analysis()
34        controller.run()
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 31/08/2026, 15:06:11*

**[REMOVED]**
```
(from line ~124)
        X_val_scaled = PowerTransformer().fit_transform(X_val)
        importance_df = self.data_handler.make_permutation_importance(model, X_val_scaled, y_val, feature_names)

```
**[ADDED]**
```
124           #X_val_scaled = PowerTransformer().fit_transform(X_val)
125           importance_df = self.data_handler.make_permutation_importance(model, X_val, y_val, feature_names)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 31/08/2026, 15:03:58*

**[ADDED]**
```
142               {
143                   "clf": [RandomForestRegressor(random_state=42)],
144                   "clf__n_estimators": [100, 300, 500],
145                   "clf__max_depth": [None, 10, 20],
146                   "clf__criterion": ["squared_error", "absolute_error"],
147                   "scaler": [None],
148                   "reducao": ["passthrough"],
149               },
```
**[REMOVED]**
```
(from line ~151)
            #    "clf": [RandomForestRegressor(random_state=42)],
            #    "clf__n_estimators": [100, 300, 500],
            #    "clf__max_depth": [None, 10, 20],
            #    "clf__criterion": ["squared_error", "absolute_error"],
            #    "scaler": [None],
            #    "reducao": ["passthrough"],
            #},
            #{

```
**[REMOVED]**
```
(from line ~179)
            {
                "clf": [Ridge()],
                "clf__alpha": [0.01, 0.1],
                "scaler": scalers,
                "reducao": reducoes,
            },

```
**[ADDED]**
```
180               #    "clf": [Ridge()],
181               #    "clf__alpha": [0.01, 0.1],
182               #    "scaler": scalers,
183               #    "reducao": reducoes,
184               #},
185               #{
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 31/08/2026, 15:01:18*

**[REMOVED]**
```
(from line ~131)
                
        print("\n--- Gerando Visualizações Detalhadas ---")
        
        # Preparar dados completos para visualizações (sem split)
        X_full, y_full = preparar_dados_para_treino(self.data_handler.data_path)
        X_full_df = pd.DataFrame(X_full, columns=feature_names)
        
        # Treinar modelos adicionais para comparação de importância
        rf_model = RandomForestRegressor(n_estimators=100, random_state=rs, n_jobs=-1)
        rf_model.fit(X_full, y_full)
        
        lr_model =  LogisticRegression(max_iter=1000, random_state=rs)
        lr_model.fit(X_full, y_full)
        
        # Extrair importâncias da árcore
        rf_feature_importances = rf_model.feature_importances_
        
        # Para Regressão Logística eu peguei a média dos valores absolutos dos coeficientes
        if len(lr_model.coef_.shape) == 2 and lr_model.coef_.shape[0] > 1:
            lr_coefficients = np.mean(np.abs(lr_model.coef_), axis=0)
        else:
            lr_coefficients = np.abs(lr_model.coef_.flatten())
        
        # Comparação de Importância de Features com Gráficos
        print("\n Gerando comparação de importância de features...")
        AdvancedVisualizations.plot_feature_importance_comparison(
            permutation_importance_df=importance_df,
            rf_feature_importances=rf_feature_importances,
            lr_coefficients=lr_coefficients,
            feature_names=feature_names,
            dataset_name="Pé frontal esquerdo - 150 amostras - 2 classes"
        )
        
        # Identificar Top 2 features de cada método
        top_features_dict = AdvancedVisualizations.get_top_2_features(
            permutation_importance_df=importance_df,
            rf_feature_importances=rf_feature_importances,
            lr_coefficients=lr_coefficients,
            feature_names=feature_names
        )
        
        print(f"\nTop 2 Features - Permutation Importance: {top_features_dict['permutation']}")
        print(f"Top 2 Features - Random Forest: {top_features_dict['random_forest']}")
        print(f"Top 2 Features - Logistic Regression: {top_features_dict['logistic_regression']}")
        
        # Plots 2D com as Duas Melhores Features de Cada Método
        print("\nGerando plots 2D das top features...")
        AdvancedVisualizations.plot_2d_scatter_top_features(
            X=X_full_df,
            y=y_full,
            top_features_dict=top_features_dict,
            class_names=["Classe 0", "Classe 1"],
            dataset_name="Pé frontal esquerdo - 150 amostras - 2 classes"
        )
        

```
**[ADDED]**
```
131   
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 31/08/2026, 15:00:26*

**[REMOVED]**
```
(from line ~141)
                

```
**[ADDED]**
```
141           
142           lr_model =  LogisticRegression(max_iter=1000, random_state=rs)
143           lr_model.fit(X_full, y_full)
144           
```
**[REMOVED]**
```
(from line ~147)
            

```
**[ADDED]**
```
147           
148           # Para Regressão Logística eu peguei a média dos valores absolutos dos coeficientes
149           if len(lr_model.coef_.shape) == 2 and lr_model.coef_.shape[0] > 1:
150               lr_coefficients = np.mean(np.abs(lr_model.coef_), axis=0)
151           else:
152               lr_coefficients = np.abs(lr_model.coef_.flatten())
153           
```
**[ADDED]**
```
159               lr_coefficients=lr_coefficients,
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 31/08/2026, 14:59:15*

**[REMOVED]**
```
(from line ~144)
        
        # Para Regressão Logística eu peguei a média dos valores absolutos dos coeficientes
        if len(lr_model.coef_.shape) == 2 and lr_model.coef_.shape[0] > 1:
            lr_coefficients = np.mean(np.abs(lr_model.coef_), axis=0)
        else:
            lr_coefficients = np.abs(lr_model.coef_.flatten())
        

```
**[ADDED]**
```
144               
```
**[REMOVED]**
```
(from line ~150)
            lr_coefficients=lr_coefficients,

```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 31/08/2026, 14:58:46*

**[REMOVED]**
```
(from line ~141)
        
        lr_model = LogisticRegressionRegressor(max_iter=1000, random_state=rs)
        lr_model.fit(X_full, y_full)
        

```
**[ADDED]**
```
141                   
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 31/08/2026, 14:58:28*

**[REMOVED]**
```
(from line ~142)
        lr_model = LogisticRegression(max_iter=1000, random_state=rs)

```
**[ADDED]**
```
142           lr_model = LogisticRegressionRegressor(max_iter=1000, random_state=rs)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 31/08/2026, 14:57:52*

**[REMOVED]**
```
(from line ~14)
from sklearn.ensemble import RandomForestClassifier

```
**[ADDED]**
```
14    from sklearn.ensemble import RandomForestRegressor
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 31/08/2026, 14:57:38*

**[REMOVED]**
```
(from line ~139)
        rf_model = RandomForestClassifier(n_estimators=100, random_state=rs, n_jobs=-1)

```
**[ADDED]**
```
139           rf_model = RandomForestRegressor(n_estimators=100, random_state=rs, n_jobs=-1)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 31/08/2026, 14:57:11*

**[REMOVED]**
```
(from line ~136)
        #X_full_scaled = RobustScaler().fit_transform(X_full)

```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 31/08/2026, 14:57:08*

**[REMOVED]**
```
(from line ~136)
        X_full_scaled = RobustScaler().fit_transform(X_full)
        X_full_df = pd.DataFrame(X_full_scaled, columns=feature_names)

```
**[ADDED]**
```
136           #X_full_scaled = RobustScaler().fit_transform(X_full)
137           X_full_df = pd.DataFrame(X_full, columns=feature_names)
```
**[REMOVED]**
```
(from line ~141)
        rf_model.fit(X_full_scaled, y_full)

```
**[ADDED]**
```
141           rf_model.fit(X_full, y_full)
```
**[REMOVED]**
```
(from line ~144)
        lr_model.fit(X_full_scaled, y_full)

```
**[ADDED]**
```
144           lr_model.fit(X_full, y_full)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 31/08/2026, 14:55:42*

**[REMOVED]**
```
(from line ~135)
        X_full, y_full = preparar_dados_para_treino(self.data_handler.data_path, self.data_handler.results_path)

```
**[ADDED]**
```
135           X_full, y_full = preparar_dados_para_treino(self.data_handler.data_path)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 31/08/2026, 14:55:04*

**[REMOVED]**
```
(from line ~131)
        
        # Matriz de Confusão
        AdvancedVisualizations.plot_confusion_matrix(y_val, model.predict(X_val_scaled), class_names=["Classe 0", "Classe 1"], dataset_name="Pé frontal esquerdo - 150 amostras - 2 classes")
        
  

```
**[ADDED]**
```
131                   
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/views/advanced_visualizations.py
*Saved at: 31/08/2026, 14:53:52*

**[REMOVED]**
```
(from line ~2)
Visualizações avançadas para análise de modelos de Machine Learning.
Inclui comparações de importância de features, plots 2D e diagnósticos.

```
**[ADDED]**
```
2     Visualizações avançadas para análise de modelos de Machine Learning (Regressão).
3     Inclui comparações de importância de features, plots 2D, gráficos de resíduos e diagnósticos.
```
**[REMOVED]**
```
(from line ~8)
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

```
**[REMOVED]**
```
(from line ~12)
    """Classe responsável por gerar visualizações avançadas de análise de modelos."""

```
**[ADDED]**
```
12        """Classe responsável por gerar visualizações avançadas de análise de modelos de regressão."""
```
**[REMOVED]**
```
(from line ~15)
    def plot_confusion_matrix(

```
**[ADDED]**
```
15        def plot_regression_diagnostics(
```
**[REMOVED]**
```
(from line ~18)
        class_names: List[str] = None,

```
**[REMOVED]**
```
(from line ~21)
        Plota a matriz de confusão com anotações.

```
**[ADDED]**
```
21            Plota diagnósticos básicos de regressão:
22            1. Predito vs. Real
23            2. Resíduos vs. Predito (para checar heterocedasticidade e padrões)
```
**[REMOVED]**
```
(from line ~26)
            y_true: Array com os labels verdadeiros.
            y_pred: Array com os labels previstos.
            class_names: Nomes das classes para os rótulos dos eixos.

```
**[ADDED]**
```
26                y_true: Array com os valores reais.
27                y_pred: Array com os valores previstos.
```
**[REMOVED]**
```
(from line ~30)
        from sklearn.metrics import confusion_matrix
        import seaborn as sns

```
**[ADDED]**
```
30            residuos = y_true - y_pred
```
**[REMOVED]**
```
(from line ~32)
        cm = confusion_matrix(y_true, y_pred)
        plt.figure(figsize=(6, 5))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                    xticklabels=class_names, yticklabels=class_names)
        plt.xlabel('Predito')
        plt.ylabel('Verdadeiro')
        plt.title(f'Matriz de Confusão - {dataset_name}', fontsize=14, fontweight='bold')

```
**[ADDED]**
```
32            fig, axes = plt.subplots(1, 2, figsize=(14, 5))
33    
34            # 1. Valores Reais vs. Preditos
35            axes[0].scatter(y_true, y_pred, alpha=0.6, color='crimson', edgecolors='k')
36            
37            # Linha de identidade (perfeição)
38            min_val = min(np.min(y_true), np.min(y_pred))
39            max_val = max(np.max(y_true), np.max(y_pred))
40            axes[0].plot([min_val, max_val], [min_val, max_val], 'k--', lw=2, label='Ideal (y = y_pred)')
41            
42            axes[0].set_xlabel('Valor Real', fontsize=11)
43            axes[0].set_ylabel('Valor Predito', fontsize=11)
44            axes[0].set_title('Valores Reais vs. Preditos', fontsize=12, fontweight='bold')
45            axes[0].legend(loc='best')
46            axes[0].grid(True, linestyle=':', alpha=0.6)
47    
48            # 2. Resíduos vs. Predito
49            axes[1].scatter(y_pred, residuos, alpha=0.6, color='purple', edgecolors='k')
50            axes[1].axhline(y=0, color='black', linestyle='--', lw=2)
51            axes[1].set_xlabel('Valor Predito', fontsize=11)
52            axes[1].set_ylabel('Resíduo (Real - Predito)', fontsize=11)
53            axes[1].set_title('Gráfico de Resíduos', fontsize=12, fontweight='bold')
54            axes[1].grid(True, linestyle=':', alpha=0.6)
55    
56            plt.suptitle(f'Diagnóstico de Regressão - {dataset_name}', fontsize=14, fontweight='bold', y=1.02)
```
**[REMOVED]**
```
(from line ~63)
        rf_feature_importances: np.ndarray,
        lr_coefficients: np.ndarray,

```
**[ADDED]**
```
63            tree_feature_importances: np.ndarray,
64            linear_coefficients: np.ndarray,
```
**[REMOVED]**
```
(from line ~70)
        pelos métodos: Permutation Importance, Random Forest Native e Logistic Regression.

```
**[ADDED]**
```
70            pelos métodos: Permutation Importance, Modelo Baseado em Árvore (ex: RandomForestRegressor)
71            e Modelo Linear (ex: Regressão Linear/Ridge/Lasso).
```
**[REMOVED]**
```
(from line ~75)
            rf_feature_importances: Array com importâncias nativas do Random Forest.
            lr_coefficients: Array com coeficientes da Regressão Logística (média por feature).

```
**[ADDED]**
```
75                tree_feature_importances: Array com importâncias nativas de modelos de árvore.
76                linear_coefficients: Array com coeficientes do modelo linear.
```
**[REMOVED]**
```
(from line ~82)
        # Permutation Importance

```
**[ADDED]**
```
82            # Permutation Importance (Em Regressão, costuma ser a queda no R2 ou aumento no MSE)
```
**[REMOVED]**
```
(from line ~86)
        axes[0].set_xlabel('Queda na Acurácia')

```
**[ADDED]**
```
86            axes[0].set_xlabel('Métrica de Queda (ex: R² drop)')
```
**[REMOVED]**
```
(from line ~91)
        # Random Forest Feature Importances
        axes[1].barh(feature_names, rf_feature_importances, color='darkorange')
        axes[1].set_xlabel('Importância (Gini Impurity Decrease)')
        axes[1].set_title('Random Forest Native', fontsize=12, fontweight='bold')

```
**[ADDED]**
```
91            # Tree-based Feature Importances
92            axes[1].barh(feature_names, tree_feature_importances, color='darkorange')
93            axes[1].set_xlabel('Importância Relativa')
94            axes[1].set_title('Tree-Based Model Native', fontsize=12, fontweight='bold')
```
**[REMOVED]**
```
(from line ~98)
        # Logistic Regression Coefficients
        axes[2].barh(feature_names, lr_coefficients, color='forestgreen')
        axes[2].set_xlabel('Média dos Coeficientes Absolutos')
        axes[2].set_title('Logistic Regression Coefficients', fontsize=12, fontweight='bold')

```
**[ADDED]**
```
98            # Linear Model Coefficients (Usa valor absoluto para comparar magnitude)
99            abs_coefs = np.abs(linear_coefficients)
100           axes[2].barh(feature_names, abs_coefs, color='forestgreen')
101           axes[2].set_xlabel('Magnitude Absoluta dos Coeficientes')
102           axes[2].set_title('Linear Model Coefficients (|w|)', fontsize=12, fontweight='bold')
```
**[REMOVED]**
```
(from line ~114)
        rf_feature_importances: np.ndarray,
        lr_coefficients: np.ndarray,

```
**[ADDED]**
```
114           tree_feature_importances: np.ndarray,
115           linear_coefficients: np.ndarray,
```
**[REMOVED]**
```
(from line ~121)
        Args:
            permutation_importance_df: DataFrame com Permutation Importance.
            rf_feature_importances: Array com importâncias do Random Forest.
            lr_coefficients: Array com coeficientes da Regressão Logística.
            feature_names: Lista de nomes das features.


```
**[REMOVED]**
```
(from line ~127)
        # Top 2 Random Forest
        rf_indices = np.argsort(rf_feature_importances)[::-1][:2]
        rf_top2 = [feature_names[i] for i in rf_indices]

```
**[ADDED]**
```
127           # Top 2 Tree Model
128           tree_indices = np.argsort(tree_feature_importances)[::-1][:2]
129           tree_top2 = [feature_names[i] for i in tree_indices]
```
**[REMOVED]**
```
(from line ~131)
        # Top 2 Logistic Regression
        lr_indices = np.argsort(lr_coefficients)[::-1][:2]
        lr_top2 = [feature_names[i] for i in lr_indices]

```
**[ADDED]**
```
131           # Top 2 Linear Model (baseado no valor absoluto)
132           linear_indices = np.argsort(np.abs(linear_coefficients))[::-1][:2]
133           linear_top2 = [feature_names[i] for i in linear_indices]
```
**[REMOVED]**
```
(from line ~137)
            'random_forest': tuple(rf_top2),
            'logistic_regression': tuple(lr_top2)

```
**[ADDED]**
```
137               'tree_model': tuple(tree_top2),
138               'linear_model': tuple(linear_top2)
```
**[REMOVED]**
```
(from line ~146)
        class_names: List[str] = None,

```
**[ADDED]**
```
150           Usa um mapa de cores (colormap) contínuo para representar o valor do alvo (y).
```
**[REMOVED]**
```
(from line ~154)
            y: Array com os labels.

```
**[ADDED]**
```
154               y: Array contínuo com os valores alvo (target).
```
**[REMOVED]**
```
(from line ~156)
            class_names: Nomes das classes para legenda.

```
**[REMOVED]**
```
(from line ~162)
            'random_forest': 'Top 2 - Random Forest',
            'logistic_regression': 'Top 2 - Logistic Regression'

```
**[ADDED]**
```
162               'tree_model': 'Top 2 - Tree Model',
163               'linear_model': 'Top 2 - Linear Model'
```
**[REMOVED]**
```
(from line ~166)
        colors = plt.cm.Set1(np.linspace(0, 1, len(np.unique(y))))


```
**[REMOVED]**
```
(from line ~169)
            # Plot scatter
            for class_idx, class_val in enumerate(np.unique(y)):
                mask = y == class_val
                label = class_names[class_idx] if class_names is not None else f'Classe {class_val}'
                ax.scatter(X.loc[mask, feat1], X.loc[mask, feat2], 
                          c=[colors[class_idx]], label=label, alpha=0.7, edgecolors='k', s=50)

```
**[ADDED]**
```
169               # Scatter plot usando o alvo `y` como gradiente de cor
170               sc = ax.scatter(X[feat1], X[feat2], c=y, cmap='viridis', 
171                               alpha=0.7, edgecolors='k', s=50)
```
**[REMOVED]**
```
(from line ~175)
            ax.set_title(method_titles[method], fontsize=12, fontweight='bold')
            ax.legend(loc='best', fontsize=9)

```
**[ADDED]**
```
175               ax.set_title(method_titles.get(method, method), fontsize=12, fontweight='bold')
```
**[ADDED]**
```
177               
178               cbar = plt.colorbar(sc, ax=ax)
179               cbar.set_label('Target (y)', fontsize=10)
```
**[REMOVED]**
```
(from line ~186)
    

```
**[REMOVED]**
```
(from line ~187)


```
**[REMOVED]**
```
(from line ~188)
    """Classe responsável por diagnósticos de treinamento (overfitting/underfitting)."""

```
**[ADDED]**
```
188       """Classe responsável por diagnósticos de treinamento em Regressão (overfitting/underfitting)."""
```
**[REMOVED]**
```
(from line ~197)
        metricas: List[str] = ['accuracy', 'f1']

```
**[ADDED]**
```
197           metricas: List[str] = ['r2', 'rmse', 'mae']
```
**[REMOVED]**
```
(from line ~200)
        Analisa se o modelo apresentou Overfitting, Underfitting ou Bom Ajuste.

```
**[ADDED]**
```
200           Analisa se o modelo de regressão apresentou Overfitting, Underfitting ou Bom Ajuste.
```
**[REMOVED]**
```
(from line ~203)
            modelo: Modelo treinado (deve ter método .score() ou ser um pipeline).

```
**[ADDED]**
```
203               modelo: Modelo treinado.
```
**[REMOVED]**
```
(from line ~208)
            metricas: Lista de métricas para calcular ('accuracy', 'f1').

```
**[ADDED]**
```
208               metricas: Lista de métricas para calcular ('r2', 'rmse', 'mae').
```
**[REMOVED]**
```
(from line ~213)
        from sklearn.metrics import accuracy_score, f1_score

```
**[ADDED]**
```
213           from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
```
**[REMOVED]**
```
(from line ~221)
        # Calcular métricas
        if 'accuracy' in metricas:
            acc_treino = accuracy_score(y_treino, y_pred_treino)
            acc_teste = accuracy_score(y_teste, y_pred_teste)
            resultados['accuracy_treino'] = acc_treino
            resultados['accuracy_teste'] = acc_teste

```
**[ADDED]**
```
221           # Calcular métricas selecionadas
222           if 'r2' in metricas:
223               resultados['r2_treino'] = r2_score(y_treino, y_pred_treino)
224               resultados['r2_teste'] = r2_score(y_teste, y_pred_teste)
```
**[REMOVED]**
```
(from line ~226)
        if 'f1' in metricas:
            f1_treino = f1_score(y_treino, y_pred_treino, average='weighted', zero_division=0)
            f1_teste = f1_score(y_teste, y_pred_teste, average='weighted', zero_division=0)
            resultados['f1_treino'] = f1_treino
            resultados['f1_teste'] = f1_teste

```
**[ADDED]**
```
226           if 'rmse' in metricas:
227               resultados['rmse_treino'] = np.sqrt(mean_squared_error(y_treino, y_pred_treino))
228               resultados['rmse_teste'] = np.sqrt(mean_squared_error(y_teste, y_pred_teste))
```
**[REMOVED]**
```
(from line ~230)
        # Diagnóstico

```
**[ADDED]**
```
230           if 'mae' in metricas:
231               resultados['mae_treino'] = mean_absolute_error(y_treino, y_pred_treino)
232               resultados['mae_teste'] = mean_absolute_error(y_teste, y_pred_teste)
233   
234           # Diagnóstico baseado no R²
```
**[REMOVED]**
```
(from line ~246)
        Determina o tipo de ajuste baseado nas métricas.

```
**[ADDED]**
```
246           Determina o tipo de ajuste baseado na métrica R² (coeficiente de determinação).
```
**[REMOVED]**
```
(from line ~254)
        acc_treino = resultados.get('accuracy_treino', 0)       
        acc_teste = resultados.get('accuracy_teste', 0)

```
**[ADDED]**
```
254           r2_treino = resultados.get('r2_treino', 0)       
255           r2_teste = resultados.get('r2_teste', 0)
```
**[REMOVED]**
```
(from line ~257)
        # Thresholds para diagnóstico
        threshold_bom = 0.7  # Mínimo para considerar "bom"
        gap_overfitting = 0.15  # Diferença máxima aceitável entre treino e teste

```
**[ADDED]**
```
257           # Thresholds customizáveis para regressão
258           threshold_bom = 0.60  # R² mínimo desejável
259           gap_overfitting = 0.15  # Diferença máxima tolerada de R² entre treino e teste
```
**[REMOVED]**
```
(from line ~261)
        if acc_treino >= threshold_bom and acc_teste < threshold_bom:

```
**[ADDED]**
```
261           if r2_treino >= threshold_bom and r2_teste < threshold_bom:
```
**[REMOVED]**
```
(from line ~263)
        elif acc_treino < threshold_bom and acc_teste < threshold_bom:

```
**[ADDED]**
```
263           elif r2_treino < threshold_bom and r2_teste < threshold_bom:
```
**[REMOVED]**
```
(from line ~265)
        elif (acc_treino - acc_teste) > gap_overfitting:

```
**[ADDED]**
```
265           elif (r2_treino - r2_teste) > gap_overfitting:
```
**[REMOVED]**
```
(from line ~273)
        Imprime um relatório textual claro do diagnóstico.

```
**[ADDED]**
```
273           Imprime um relatório textual claro do diagnóstico de regressão.
```
**[REMOVED]**
```
(from line ~280)
        print("DIAGNÓSTICO DE APRENDIZADO DO MODELO")

```
**[ADDED]**
```
280           print("DIAGNÓSTICO DE APRENDIZADO DO MODELO DE REGRESSÃO")
```
**[REMOVED]**
```
(from line ~283)
        if 'accuracy_treino' in resultados:
            print(f"Acurácia no Treino:  {resultados['accuracy_treino']:.2%}")
            print(f"Acurácia no Teste:   {resultados['accuracy_teste']:.2%}")
            print(f"Diferença:           {(resultados['accuracy_treino'] - resultados['accuracy_teste']):.2%}")

```
**[ADDED]**
```
283           if 'r2_treino' in resultados:
284               print(f"R² no Treino:        {resultados['r2_treino']:.4f}")
285               print(f"R² no Teste:         {resultados['r2_teste']:.4f}")
286               print(f"Diferença no R²:     {(resultados['r2_treino'] - resultados['r2_teste']):.4f}")
```
**[REMOVED]**
```
(from line ~288)
        if 'f1_treino' in resultados:
            print(f"F1-Score no Treino:  {resultados['f1_treino']:.2%}")
            print(f"F1-Score no Teste:   {resultados['f1_teste']:.2%}")
            print(f"Diferença:           {(resultados['f1_treino'] - resultados['f1_teste']):.2%}")

```
**[ADDED]**
```
288           if 'rmse_treino' in resultados:
289               print(f"RMSE no Treino:      {resultados['rmse_treino']:.4f}")
290               print(f"RMSE no Teste:       {resultados['rmse_teste']:.4f}")
```
**[ADDED]**
```
292           if 'mae_treino' in resultados:
293               print(f"MAE no Treino:       {resultados['mae_treino']:.4f}")
294               print(f"MAE no Teste:        {resultados['mae_teste']:.4f}")
295   
```
**[REMOVED]**
```
(from line ~298)
        if diagnostico == "OVERFITTING":
            print("\n O modelo memorizou os dados de treino e não generaliza bem.")

```
**[ADDED]**
```
298           if "OVERFITTING" in diagnostico:
299               print("\n O modelo memorizou os dados de treino e tem baixo R² / alto erro no teste.")
```
**[REMOVED]**
```
(from line ~301)
            print("   - Reduzir complexidade do modelo")
            print("   - Aumentar regularização")
            print("   - Adicionar mais dados de treino")
            print("   - Usar técnicas de dropout ou early stopping")

```
**[ADDED]**
```
301               print("   - Reduzir a complexidade do modelo (ex: limitar profundidade da árvore)")
302               print("   - Aumentar regularização (ex: Lasso/Ridge, aumentar alpha/lambda)")
303               print("   - Fazer seleção de features (remover colunas ruidosas)")
```
**[REMOVED]**
```
(from line ~306)
            print("\n O modelo não conseguiu aprender padrões suficientes.")

```
**[ADDED]**
```
306               print("\n O modelo teve desempenho fraco tanto no treino quanto no teste.")
```
**[REMOVED]**
```
(from line ~308)
            print("   - Aumentar complexidade do modelo")
            print("   - Adicionar mais features relevantes")
            print("   - Reduzir regularização")
            print("   - Treinar por mais épocas/iterações")

```
**[ADDED]**
```
308               print("   - Aumentar a complexidade do modelo (trocar modelo linear por Gradient Boosting, etc.)")
309               print("   - Criar novas features relevantes (Feature Engineering/Polinomiais)")
310               print("   - Reduzir a regularização")
```
**[REMOVED]**
```
(from line ~314)
            print("   Continue monitorando em dados não vistos.")

```
**[ADDED]**
```
314               print("   Continue monitorando os resíduos e a performance em produção.")
```
**[REMOVED]**
```
(from line ~316)
        print(f"{'='*60}\n")

```
**[ADDED]**
```
316           print(f"{'='*60}\n")
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 31/08/2026, 14:50:42*

**[REMOVED]**
```
(from line ~142)
            {
                "clf": [RandomForestRegressor(random_state=42)],
                "clf__n_estimators": [100, 300, 500],
                "clf__max_depth": [None, 10, 20],
                "clf__criterion": ["squared_error", "absolute_error"],
                "scaler": [None],
                "reducao": ["passthrough"],
            },
            {
                "clf": [ExtraTreesRegressor(random_state=42)],
                "clf__n_estimators": [100, 300],
                "clf__max_depth": [None, 10, 20],
                "clf__criterion": ["squared_error", "absolute_error"],
                "scaler": [None],
                "reducao": ["passthrough"],
            },
            {
                "clf": [GradientBoostingRegressor(random_state=42)],
                "clf__n_estimators": [100, 200],
                "clf__learning_rate": [0.05, 0.1, 0.2],
                "clf__max_depth": [3, 5],
                "scaler": [None],
                "reducao": ["passthrough"],
            },

```
**[ADDED]**
```
143               #    "clf": [RandomForestRegressor(random_state=42)],
144               #    "clf__n_estimators": [100, 300, 500],
145               #    "clf__max_depth": [None, 10, 20],
146               #    "clf__criterion": ["squared_error", "absolute_error"],
147               #    "scaler": [None],
148               #    "reducao": ["passthrough"],
149               #},
150               #{
151               #    "clf": [ExtraTreesRegressor(random_state=42)],
152               #    "clf__n_estimators": [100, 300],
153               #    "clf__max_depth": [None, 10, 20],
154               #    "clf__criterion": ["squared_error", "absolute_error"],
155               #    "scaler": [None],
156               #    "reducao": ["passthrough"],
157               #},
158               #{
159               #    "clf": [GradientBoostingRegressor(random_state=42)],
160               #    "clf__n_estimators": [100, 200],
161               #    "clf__learning_rate": [0.05, 0.1, 0.2],
162               #    "clf__max_depth": [3, 5],
163               #    "scaler": [None],
164               #    "reducao": ["passthrough"],
165               #},
166               #{
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 31/08/2026, 14:50:19*

**[ADDED]**
```
142               {
143                   "clf": [RandomForestRegressor(random_state=42)],
144                   "clf__n_estimators": [100, 300, 500],
145                   "clf__max_depth": [None, 10, 20],
146                   "clf__criterion": ["squared_error", "absolute_error"],
147                   "scaler": [None],
148                   "reducao": ["passthrough"],
149               },
150               {
151                   "clf": [ExtraTreesRegressor(random_state=42)],
152                   "clf__n_estimators": [100, 300],
153                   "clf__max_depth": [None, 10, 20],
154                   "clf__criterion": ["squared_error", "absolute_error"],
155                   "scaler": [None],
156                   "reducao": ["passthrough"],
157               },
158               {
159                   "clf": [GradientBoostingRegressor(random_state=42)],
160                   "clf__n_estimators": [100, 200],
161                   "clf__learning_rate": [0.05, 0.1, 0.2],
162                   "clf__max_depth": [3, 5],
163                   "scaler": [None],
164                   "reducao": ["passthrough"],
165               },
```
**[REMOVED]**
```
(from line ~167)
            #    "clf": [RandomForestRegressor(random_state=42)],
            #    "clf__n_estimators": [100, 300, 500],
            #    "clf__max_depth": [None, 10, 20],
            #    "clf__criterion": ["squared_error", "absolute_error"],
            #    "scaler": [None],
            #    "reducao": ["passthrough"],
            #},
            #{
            #    "clf": [ExtraTreesRegressor(random_state=42)],
            #    "clf__n_estimators": [100, 300],
            #    "clf__max_depth": [None, 10, 20],
            #    "clf__criterion": ["squared_error", "absolute_error"],
            #    "scaler": [None],
            #    "reducao": ["passthrough"],
            #},
            #{
            #    "clf": [GradientBoostingRegressor(random_state=42)],
            #    "clf__n_estimators": [100, 200],
            #    "clf__learning_rate": [0.05, 0.1, 0.2],
            #    "clf__max_depth": [3, 5],
            #    "scaler": [None],
            #    "reducao": ["passthrough"],
            #},
            #{

```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 31/08/2026, 14:49:43*

**[REMOVED]**
```
(from line ~99)
        X, y = preparar_dados_para_treino(self.data_handler.data_path, self.data_handler.results_path)

```
**[ADDED]**
```
99            X, y = preparar_dados_para_treino(self.data_handler.data_path)
```
**[REMOVED]**
```
(from line ~102)
        DataReport.generate_report_balenceamento(y)

```
**[ADDED]**
```
102           #DataReport.generate_report_balenceamento(y)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 31/08/2026, 14:49:08*

**[REMOVED]**
```
(from line ~97)
        rs = random.randint(1, 1000) # random_state do melhor modelo encontrado para o MLP
        #rs = 647 # random_state do melhor modelo encontrado para o KNN
        #removed_features_knn = ["heel_x_iqr"]
        #removed_features_mlp = ["big_toe_x_iqr"]

```
**[ADDED]**
```
97            rs = random.randint(1, 1000)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 31/08/2026, 14:49:05*

**[REMOVED]**
```
(from line ~97)
        rs = 777 # random_state do melhor modelo encontrado para o MLP

```
**[ADDED]**
```
97            rs = random.randint(1, 1000) # random_state do melhor modelo encontrado para o MLP
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 31/08/2026, 14:48:49*

**[REMOVED]**
```
(from line ~33)
    #controller.run_data_analysis()

```
**[ADDED]**
```
33        controller.run_data_analysis()
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 31/08/2026, 14:48:42*

**[REMOVED]**
```
(from line ~34)
    controller.run()

```
**[ADDED]**
```
34        #controller.run()
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 31/08/2026, 14:43:00*

**[REMOVED]**
```
(from line ~51)
            #PCA(n_components=0.95, random_state=31),

```
**[ADDED]**
```
51                PCA(n_components=0.95, random_state=31),
```
**[REMOVED]**
```
(from line ~53)
            #SelectKBest(score_func=f_regression, k="all")

```
**[ADDED]**
```
53                SelectKBest(score_func=f_regression, k="all")
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 31/08/2026, 14:42:48*

**[REMOVED]**
```
(from line ~37)
            #None,

```
**[ADDED]**
```
37                None,
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 31/08/2026, 14:42:31*

**[REMOVED]**
```
(from line ~21)
    DATA_PATH = "./planilhas/Machine_learning_ganhosde_forca.xlsx"

```
**[ADDED]**
```
21        DATA_PATH = "./planilhas/Machine learning ganhos de forca (1RM-POS).xlsx"
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 29/08/2026, 13:55:53*

**[REMOVED]**
```
(from line ~29)
            StandardScaler(),

```
**[ADDED]**
```
29                #StandardScaler(),
```
**[REMOVED]**
```
(from line ~31)
            MinMaxScaler(),

```
**[ADDED]**
```
31                #MinMaxScaler(),
```
**[REMOVED]**
```
(from line ~33)
            QuantileTransformer(output_distribution="uniform", random_state=42),

```
**[ADDED]**
```
33                #QuantileTransformer(output_distribution="uniform", random_state=42),
```
**[REMOVED]**
```
(from line ~35)
            PowerTransformer(method="yeo-johnson"),
            Normalizer(norm="l2"),

```
**[ADDED]**
```
35                #PowerTransformer(method="yeo-johnson"),
36                #Normalizer(norm="l2"),
```
**[REMOVED]**
```
(from line ~39)
            RobustScaler(),

```
**[ADDED]**
```
39                #RobustScaler(),
```
**[REMOVED]**
```
(from line ~51)
            PCA(n_components=0.95, random_state=31),

```
**[ADDED]**
```
51                #PCA(n_components=0.95, random_state=31),
```
**[REMOVED]**
```
(from line ~53)
            SelectKBest(score_func=f_regression, k="all")

```
**[ADDED]**
```
53                #SelectKBest(score_func=f_regression, k="all")
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 29/08/2026, 13:55:35*

**[REMOVED]**
```
(from line ~181)
                "clf__alpha": [0.1, 1.0, 10.0, 100.0],

```
**[ADDED]**
```
181                   "clf__alpha": [0.01, 0.1],
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 29/08/2026, 13:49:31*

**[REMOVED]**
```
(from line ~51)
            #PCA(n_components=0.95, random_state=31),

```
**[ADDED]**
```
51                PCA(n_components=0.95, random_state=31),
```
**[REMOVED]**
```
(from line ~53)
            #SelectKBest(score_func=f_regression, k="all")

```
**[ADDED]**
```
53                SelectKBest(score_func=f_regression, k="all")
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 29/08/2026, 13:47:33*

**[REMOVED]**
```
(from line ~29)
            #StandardScaler(),

```
**[ADDED]**
```
29                StandardScaler(),
```
**[REMOVED]**
```
(from line ~31)
            #MinMaxScaler(),
            #MaxAbsScaler(),
            #QuantileTransformer(output_distribution="uniform", random_state=42),

```
**[ADDED]**
```
31                MinMaxScaler(),
32                MaxAbsScaler(),
33                QuantileTransformer(output_distribution="uniform", random_state=42),
```
**[REMOVED]**
```
(from line ~35)
            #PowerTransformer(method="yeo-johnson"),
            #Normalizer(norm="l2"),

```
**[ADDED]**
```
35                PowerTransformer(method="yeo-johnson"),
36                Normalizer(norm="l2"),
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 29/08/2026, 13:47:08*

**[REMOVED]**
```
(from line ~183)
                "reducao": ["passthrough"],

```
**[ADDED]**
```
183                   "reducao": reducoes,
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 29/08/2026, 13:46:56*

**[ADDED]**
```
179               {
180                   "clf": [Ridge()],
181                   "clf__alpha": [0.1, 1.0, 10.0, 100.0],
182                   "scaler": scalers,
183                   "reducao": ["passthrough"],
184               },
```
**[REMOVED]**
```
(from line ~186)
            #    "clf": [Ridge()],
            #    "clf__alpha": [0.1, 1.0, 10.0, 100.0],
            #    "scaler": scalers,
            #    "reducao": ["passthrough"],
            #},
            #{

```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 29/08/2026, 13:46:06*

**[REMOVED]**
```
(from line ~174)
            {
                "clf": [LinearRegression()],
                "scaler": scalers,
                "reducao": reducoes,
            },

```
**[ADDED]**
```
175               #    "clf": [LinearRegression()],
176               #    "scaler": scalers,
177               #    "reducao": reducoes,
178               #},
179               #{
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 29/08/2026, 13:45:22*

**[REMOVED]**
```
(from line ~51)
            PCA(n_components=0.95, random_state=31),

```
**[ADDED]**
```
51                #PCA(n_components=0.95, random_state=31),
```
**[REMOVED]**
```
(from line ~176)
                "clf__fit_intercept": [True, False],
                "clf__positive": [True, False],

```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 29/08/2026, 13:44:23*

**[REMOVED]**
```
(from line ~31)
            MinMaxScaler(),
            MaxAbsScaler(),
            QuantileTransformer(output_distribution="uniform", random_state=42),

```
**[ADDED]**
```
31                #MinMaxScaler(),
32                #MaxAbsScaler(),
33                #QuantileTransformer(output_distribution="uniform", random_state=42),
```
**[REMOVED]**
```
(from line ~35)
            PowerTransformer(method="yeo-johnson"),
            Normalizer(norm="l2"),

```
**[ADDED]**
```
35                #PowerTransformer(method="yeo-johnson"),
36                #Normalizer(norm="l2"),
```
**[REMOVED]**
```
(from line ~43)
            StandardScaler(),

```
**[ADDED]**
```
43                #StandardScaler(),
```
**[REMOVED]**
```
(from line ~53)
            SelectKBest(score_func=f_regression, k="all")

```
**[ADDED]**
```
53                #SelectKBest(score_func=f_regression, k="all")
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 29/08/2026, 13:42:09*

**[ADDED]**
```
176                   "clf__fit_intercept": [True, False],
177                   "clf__positive": [True, False],
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 29/08/2026, 13:40:29*

**[REMOVED]**
```
(from line ~51)
            #PCA(n_components=0.95, random_state=31),

```
**[ADDED]**
```
51                PCA(n_components=0.95, random_state=31),
```
**[REMOVED]**
```
(from line ~53)
            #SelectKBest(score_func=f_regression, k="all")

```
**[ADDED]**
```
53                SelectKBest(score_func=f_regression, k="all")
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 29/08/2026, 13:36:22*

**[REMOVED]**
```
(from line ~51)
            PCA(n_components=0.95, random_state=31),

```
**[ADDED]**
```
51                #PCA(n_components=0.95, random_state=31),
```
**[REMOVED]**
```
(from line ~53)
            SelectKBest(score_func=f_regression, k="all")

```
**[ADDED]**
```
53                #SelectKBest(score_func=f_regression, k="all")
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/config/settings.py
*Saved at: 29/08/2026, 13:35:22*

**[REMOVED]**
```
(from line ~12)
    'rmse': 'rmse'  # Bate com a chave 'rmse' definida acima

```
**[ADDED]**
```
12        'rmse': 'rmse'
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/config/settings.py
*Saved at: 29/08/2026, 13:34:31*

**[REMOVED]**
```
(from line ~1)
METRIC_SCORING_MAP = {

```
**[ADDED]**
```
1     SCORING_PIPELINE_MAP = {
```
**[REMOVED]**
```
(from line ~8)
SCORING_PIPELINE_MAP = {

```
**[ADDED]**
```
8     METRIC_SCORING_MAP = {
```
**[REMOVED]**
```
(from line ~10)
    'mae': 'neg_mean_absolute_error',
    'mse': 'neg_mean_squared_error',
    'rmse': 'neg_root_mean_squared_error'

```
**[ADDED]**
```
10        'mae': 'mae',
11        'mse': 'mse',
12        'rmse': 'rmse'  # Bate com a chave 'rmse' definida acima
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/config/settings.py
*Saved at: 29/08/2026, 12:21:03*

**[REMOVED]**
```
(from line ~1)
"""
Configurações globais, mapeamentos de métricas e constantes do projeto.
"""

# Mapeamento entre nomes amigáveis e strings internas do scikit-learn

```
**[REMOVED]**
```
(from line ~2)
    "f1_score": "f1",
    "accuracy": "accuracy",
    "precision": "precision",
    "recall": "recall",
    "roc_auc": "roc_auc",

```
**[ADDED]**
```
2         'r2': 'r2',
3         'mae': 'neg_mean_absolute_error',
4         'mse': 'neg_mean_squared_error',
5         'rmse': 'neg_root_mean_squared_error'
```
**[REMOVED]**
```
(from line ~9)
    "f1": "f1",
    "accuracy": "accuracy",
    "precision": "precision",
    "recall": "recall",
    "roc_auc": "roc_auc",

```
**[ADDED]**
```
9         'r2': 'r2',
10        'mae': 'neg_mean_absolute_error',
11        'mse': 'neg_mean_squared_error',
12        'rmse': 'neg_root_mean_squared_error'
```
**[REMOVED]**
```
(from line ~15)
# Nomes das colunas de desvio padrão nos resultados do GridSearchCV

```
**[REMOVED]**
```
(from line ~16)
    "f1_score": "std_test_f1",
    "accuracy": "std_test_accuracy",
    "precision": "std_test_precision",
    "recall": "std_test_recall",
    "roc_auc": "std_test_roc_auc",
}

# Nomes das classes no relatório de classificação
CLASS_NAMES = ["CERTO (0)", "ERRADO (1)"]
```
**[ADDED]**
```
16        'r2': 'std_test_r2',
17        'mae': 'std_test_mae',
18        'mse': 'std_test_mse',
19        'rmse': 'std_test_rmse'
20    }
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 29/08/2026, 12:20:51*

**[REMOVED]**
```
(from line ~24)
    METRIC_FOCO = "mse"

```
**[ADDED]**
```
24        METRIC_FOCO = "rmse"
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 29/08/2026, 12:20:26*

**[REMOVED]**
```
(from line ~24)
    METRIC_FOCO = "rmse"

```
**[ADDED]**
```
24        METRIC_FOCO = "mse"
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/views/report_view.py
*Saved at: 29/08/2026, 12:19:00*

**[REMOVED]**
```
(from line ~2)
Interface de visualização e salvar o modelo.

```
**[ADDED]**
```
2     Interface de visualização e salvamento do modelo (Regressão).
```
**[REMOVED]**
```
(from line ~14)
        Exibe as métricas de validação cruzada no console.

```
**[ADDED]**
```
14            Exibe as métricas de validação cruzada para regressão no console.
```
**[REMOVED]**
```
(from line ~17)
            metrics: Dicionário com as médias do CV.

```
**[ADDED]**
```
17                metrics: Dicionário com as médias do CV (r2, mae, mse, rmse, std).
```
**[REMOVED]**
```
(from line ~22)
        print(f"{'Acuracia(CV - accuracy)':<28} {metrics['accuracy']:.2f}%")
        print(f"{'Acuracia(CV - f1_score)':<28} {metrics['f1_score']:.2f}%")
        print(f"{'Acuracia(CV - precision)':<28} {metrics['precision']:.2f}%")
        print(f"{'Acuracia(CV - recall)':<28} {metrics['recall']:.2f}%")
        print(f"{'Acuracia(CV - roc_auc)':<28} {metrics['roc_auc']:.2f}%")
        print(f"{'Desvio Padrão (CV - ' + focus + ')':<28} {metrics['std']:.4f}%")

```
**[ADDED]**
```
22            print(f"{'Métrica (CV - R2 Score)':<28} {metrics['r2']:.4f}")
23            print(f"{'Métrica (CV - MAE)':<28} {metrics['mae']:.4f}")
24            print(f"{'Métrica (CV - MSE)':<28} {metrics['mse']:.4f}")
25            print(f"{'Métrica (CV - RMSE)':<28} {metrics['rmse']:.4f}")
26            print(f"{'Desvio Padrão (CV - ' + focus + ')':<28} {metrics['std']:.4f}")
```
**[REMOVED]**
```
(from line ~49)
        Exibe o resumo final do treinamento e a média dos relatórios.

```
**[ADDED]**
```
49            Exibe o resumo final do treinamento e os relatórios de regressão.
```
**[REMOVED]**
```
(from line ~53)
            all_reports: Lista de strings de classificação.

```
**[ADDED]**
```
53                all_reports: Lista de relatórios em texto.
```
**[REMOVED]**
```
(from line ~56)
            total_minutes: Tempo total de execução.

```
**[ADDED]**
```
56                metric_focus: Métrica principal da otimização.
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/evaluators/metrics_handler.py
*Saved at: 29/08/2026, 12:17:18*

**[REMOVED]**
```
(from line ~2)
Processamento de métricas e relatórios.

```
**[ADDED]**
```
2     Processamento de métricas e relatórios para Regressão.
```
**[REMOVED]**
```
(from line ~7)
from sklearn.metrics import classification_report, roc_auc_score
from config.settings import STD_MAP, CLASS_NAMES

```
**[ADDED]**
```
7     from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
8     from config.settings import STD_MAP
```
**[REMOVED]**
```
(from line ~12)
    """Calcula e agrega métricas de desempenho do modelo."""

```
**[ADDED]**
```
12        """Calcula e agrega métricas de desempenho para modelos de regressão."""
```
**[REMOVED]**
```
(from line ~20)
        Avalia o melhor modelo encontrado no GridSearch.

```
**[ADDED]**
```
20            Avalia o melhor modelo encontrado no GridSearch usando métricas de regressão.
```
**[REMOVED]**
```
(from line ~25)
            y_test: Labels de teste.

```
**[ADDED]**
```
25                y_test: Target de teste.
```
**[REMOVED]**
```
(from line ~28)
            Tupla com (dicionário de métricas CV, string do classification_report).

```
**[ADDED]**
```
28                Tupla com (dicionário de métricas CV, string do relatório de regressão).
```
**[REMOVED]**
```
(from line ~32)
        report = classification_report( 
            y_test, y_pred, target_names=CLASS_NAMES, zero_division=0

```
**[ADDED]**
```
32    
33            # Cálculo das métricas diretas no conjunto de teste
34            mae = mean_absolute_error(y_test, y_pred)
35            mse = mean_squared_error(y_test, y_pred)
36            rmse = np.sqrt(mse)
37            r2 = r2_score(y_test, y_pred)
38    
39            report = (
40                "=== Relatório de Avaliação no Teste ===\n"
41                f"R2 Score : {r2:.4f}\n"
42                f"MAE      : {mae:.4f}\n"
43                f"MSE      : {mse:.4f}\n"
44                f"RMSE     : {rmse:.4f}\n"
```
**[REMOVED]**
```
(from line ~46)
        report += f"ROC AUC: {roc_auc_score(y_test, y_pred):.2f}\n"

```
**[ADDED]**
```
48            
49            # Leitura das métricas médias da Validação Cruzada do GridSearch
50            # Nota: O scikit-learn usa valores negativos para MAE e MSE/RMSE no scoring (neg_*)
51            # Usamos abs() para salvar com sinal positivo nos relatórios.
```
**[REMOVED]**
```
(from line ~53)
            "accuracy": grid.cv_results_["mean_test_accuracy"][idx] * 100,
            "f1_score": grid.cv_results_["mean_test_f1"][idx] * 100,
            "precision": grid.cv_results_["mean_test_precision"][idx] * 100,
            "recall": grid.cv_results_["mean_test_recall"][idx] * 100,
            "roc_auc": grid.cv_results_["mean_test_roc_auc"][idx] * 100,
            "std": grid.cv_results_[self.std_key][idx] * 100,

```
**[ADDED]**
```
53                "r2": grid.cv_results_["mean_test_r2"][idx],
54                "mae": abs(grid.cv_results_["mean_test_mae"][idx]),
55                "mse": abs(grid.cv_results_["mean_test_mse"][idx]),
56                "rmse": abs(grid.cv_results_["mean_test_rmse"][idx]),
57                "std": grid.cv_results_[self.std_key][idx],
```
**[REMOVED]**
```
(from line ~64)
        Extrai os últimos `count` números de uma string.

```
**[ADDED]**
```
64            Extrai os últimos `count` números de uma string (incluindo suporte a números negativos e decimais).
```
**[REMOVED]**
```
(from line ~67)
            line: Linha do relatório de classificação.

```
**[ADDED]**
```
67                line: Linha do relatório.
```
**[REMOVED]**
```
(from line ~73)

        #\d+: Procura um ou mais dígitos (ex: 1, 50, 123).
        #\.: Procura um ponto literal (o separador decimal).
        #\d+\.\d+: Procura números com casas decimais (ex: 0.85, 10.5).
        #|: Significa "OU".
        #\d+: Procura números inteiros (ex: 50, 100).
        
        nums = [float(x) if "." in x else int(x) for x in re.findall(r"\d+\.\d+|\d+", line)]

        # Retornmas os ultimos count numeros da linha se tivermos mais de count numeros

```
**[ADDED]**
```
73            nums = [float(x) for x in re.findall(r"[-+]?\d*\.\d+|\d+", line)]
```
**[REMOVED]**
```
(from line ~78)
        Calcula a média ponderada das métricas de múltiplos relatórios.

```
**[ADDED]**
```
78            Calcula a média das métricas de regressão a partir de múltiplos relatórios.
```
**[REMOVED]**
```
(from line ~81)
            reports: Lista de strings `classification_report`.

```
**[ADDED]**
```
81                reports: Lista de strings de relatórios gerados por `evaluate`.
```
**[REMOVED]**
```
(from line ~84)
            String formatada com a média das métricas.

```
**[ADDED]**
```
84                String formatada com a média das métricas entre as iterações.
```
**[REMOVED]**
```
(from line ~89)
        # Criando um dicíonario que guarda o precision, recall, f1 e support de cada classe

```
**[REMOVED]**
```
(from line ~90)
            cls: {"p": [], "r": [], "f": [], "s": []} for cls in CLASS_NAMES

```
**[ADDED]**
```
90                "r2": [],
91                "mae": [],
92                "mse": [],
93                "rmse": []
```
**[REMOVED]**
```
(from line ~96)
        # Adicionando os valores de accuracy, macro avg e weighted avg para cada métrica
        accumulator.update({
            "accuracy": {"acc": [], "s": []},
            "macro avg": {"p": [], "r": [], "f": [], "s": []},
            "weighted avg": {"p": [], "r": [], "f": [], "s": []},
            "roc_auc": []
        })

        # Pegando cada report na lista de todos os reports

```
**[REMOVED]**
```
(from line ~97)
            for line in report.splitlines(): # Esse splitlines transforma cada quebra de linha em uma lista de strings
                for cls in CLASS_NAMES:
                    if cls in line: # Se a classe estiver na linha
                        # Extrai os últimos 4 números da linha (Precision, Recall, F1, Support).
                        nums = self.extract_last_numbers(line, 4)
                        if len(nums) == 4:
                            # zip associa as chaves ['p','r','f','s'] aos valores encontrados [num1, num2, num3, num4]
                            for k, v in zip(["p", "r", "f", "s"], nums):
                                accumulator[cls][k].append(v)

                # Verificando se estamos na linha de accuracy
                if "accuracy" in line:
                    nums = self.extract_last_numbers(line, 2)
                    if len(nums) == 2:
                        accumulator["accuracy"]["acc"].append(nums[0])
                        accumulator["accuracy"]["s"].append(nums[1])

                # Percorrendo as linhas da média
                for avg in ["macro avg", "weighted avg"]:
                    if avg in line:
                        nums = self.extract_last_numbers(line, 4)
                        if len(nums) == 4:
                            for k, v in zip(["p", "r", "f", "s"], nums):
                                accumulator[avg][k].append(v)
            
                if "ROC AUC:" in line:

```
**[ADDED]**
```
97                for line in report.splitlines():
98                    if "R2 Score" in line:
```
**[REMOVED]**
```
(from line ~100)
                    if len(nums) == 1:
                        accumulator["roc_auc"].append(nums[0])

```
**[ADDED]**
```
100                       if nums: accumulator["r2"].append(nums[0])
101                   elif "MAE" in line:
102                       nums = self.extract_last_numbers(line, 1)
103                       if nums: accumulator["mae"].append(nums[0])
104                   elif "MSE" in line:
105                       nums = self.extract_last_numbers(line, 1)
106                       if nums: accumulator["mse"].append(nums[0])
107                   elif "RMSE" in line:
108                       nums = self.extract_last_numbers(line, 1)
109                       if nums: accumulator["rmse"].append(nums[0])
```
**[REMOVED]**
```
(from line ~114)
        output = [f"{'':>12} {'precision':>9} {'recall':>9} {'f1-score':>9} {'support':>9}"]
        for cls in CLASS_NAMES:
            output.append(
                f"{cls:>12} {safe_mean(accumulator[cls]['p']):>9.2f} "
                f"{safe_mean(accumulator[cls]['r']):>9.2f} "
                f"{safe_mean(accumulator[cls]['f']):>9.2f} "
                f"{round(safe_mean(accumulator[cls]['s'])):>9}"
            )

```
**[ADDED]**
```
114           output = [
115               "=== Média Métrica Final (Múltiplas Rodadas) ===",
116               f"R2 Score Médio : {safe_mean(accumulator['r2']):.4f}",
117               f"MAE Médio      : {safe_mean(accumulator['mae']):.4f}",
118               f"MSE Médio      : {safe_mean(accumulator['mse']):.4f}",
119               f"RMSE Médio     : {safe_mean(accumulator['rmse']):.4f}",
120           ]
```
**[REMOVED]**
```
(from line ~122)
        output.append("")
        output.append(
            f"{'accuracy':>12} {safe_mean(accumulator['accuracy']['acc']):>30.2f} "
            f"{round(safe_mean(accumulator['accuracy']['s'])):>9}"
        )

        for avg in ["macro avg", "weighted avg"]:
            output.append(
                f"{avg:>12} {safe_mean(accumulator[avg]['p']):>9.2f} "
                f"{safe_mean(accumulator[avg]['r']):>9.2f} "
                f"{safe_mean(accumulator[avg]['f']):>9.2f} "
                f"{round(safe_mean(accumulator[avg]['s'])):>9}"
            )
        if accumulator["roc_auc"]:
            output.append(f"ROC AUC: {safe_mean(accumulator['roc_auc']):.2f}")


```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 29/08/2026, 11:48:21*

**[REMOVED]**
```
(from line ~24)
    METRIC_FOCO = "r2"

```
**[ADDED]**
```
24        METRIC_FOCO = "rmse"
```
**[REMOVED]**
```
(from line ~27)
    controller = TrainingController(

```
**[ADDED]**
```
27        controller = TrainingController(    
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 29/08/2026, 11:45:40*

**[REMOVED]**
```
(from line ~23)
    # Métrica alvo: 'f1_score', 'accuracy', 'precision','recall' ou 'roc_auc'
    METRIC_FOCO = "f1_score"

```
**[ADDED]**
```
23        # Métrica alvo para Regressão: 'r2', 'mae', 'mse' ou 'rmse'
24        METRIC_FOCO = "r2"
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/trainer.py
*Saved at: 29/08/2026, 11:44:42*

**[REMOVED]**
```
(from line ~41)
            ("clf", SVR())  # 2. Alterado de SVC() para SVR()

```
**[ADDED]**
```
41                ("clf", SVR())  
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/trainer.py
*Saved at: 29/08/2026, 11:44:25*

**[REMOVED]**
```
(from line ~57)
        # 1. Utilização do KFold normal (adequado para variáveis contínuas)

```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/trainer.py
*Saved at: 29/08/2026, 11:44:17*

**[REMOVED]**
```
(from line ~2)
Treinamento de modelos com validação cruzada.

```
**[ADDED]**
```
2     Treinamento de modelos com validação cruzada para REGRESSÃO.
```
**[REMOVED]**
```
(from line ~7)
from sklearn.model_selection import GridSearchCV

```
**[ADDED]**
```
7     from sklearn.model_selection import GridSearchCV, KFold  # 1. Trocado StratifiedKFold por KFold
```
**[REMOVED]**
```
(from line ~10)
from sklearn.svm import SVC

```
**[ADDED]**
```
10    from sklearn.svm import SVR  # 2. Trocado SVC por SVR (Regressor)
```
**[REMOVED]**
```
(from line ~13)
from sklearn.model_selection import StratifiedKFold

```
**[REMOVED]**
```
(from line ~16)
    """Orquestra o treinamento e a busca de hiperparâmetros."""

```
**[ADDED]**
```
16        """Orquestra o treinamento e a busca de hiperparâmetros para modelos de regressão."""
```
**[REMOVED]**
```
(from line ~23)
            metric_focus: Métrica alvo para otimização (ex: 'f1_score', 'recall').

```
**[ADDED]**
```
23                metric_focus: Métrica alvo para otimização (ex: 'r2', 'mae', 'mse').
```
**[REMOVED]**
```
(from line ~27)
        self.refit_metric = METRIC_SCORING_MAP[metric_focus] # Metrica que o treinamento irá tentar achar o melhor modelo
        self.scoring = SCORING_PIPELINE_MAP # Metricas usadas no GridSearch

```
**[ADDED]**
```
27            self.refit_metric = METRIC_SCORING_MAP[metric_focus] # Métrica principal (ex: 'r2' ou 'neg_mean_squared_error')
28            self.scoring = SCORING_PIPELINE_MAP # Dicionário com métricas válidas de regressão
```
**[REMOVED]**
```
(from line ~41)
            ("clf", SVC())

```
**[ADDED]**
```
41                ("clf", SVR())  # 2. Alterado de SVC() para SVR()
```
**[REMOVED]**
```
(from line ~50)
            y_train: Labels do conjunto de treino.

```
**[ADDED]**
```
50                y_train: Labels/Valores contínuos do conjunto de treino.
```
**[REMOVED]**
```
(from line ~57)
        cv = StratifiedKFold(
            n_splits=5, # Testar mais números 4, 5, 6

```
**[ADDED]**
```
57            # 1. Utilização do KFold normal (adequado para variáveis contínuas)
58            cv = KFold(
59                n_splits=5,
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 29/08/2026, 11:39:06*

**[REMOVED]**
```
(from line ~69)
            #     "reg": [SGDRegressor(random_state=42)],
            #     "reg__eta0": [0.1, 0.01, 0.001],
            #     "reg__penalty": ["l2", "l1", "elasticnet"],

```
**[ADDED]**
```
69                #     "clf": [SGDRegressor(random_state=42)],
70                #     "clf__eta0": [0.1, 0.01, 0.001],
71                #     "clf__penalty": ["l2", "l1", "elasticnet"],
```
**[REMOVED]**
```
(from line ~78)
            #      "reg": [MLPRegressor(random_state=31)],
            #      "reg__activation": [

```
**[ADDED]**
```
78                #      "clf": [MLPRegressor(random_state=31)],
79                #      "clf__activation": [
```
**[REMOVED]**
```
(from line ~83)
            #      "reg__hidden_layer_sizes": [

```
**[ADDED]**
```
83                #      "clf__hidden_layer_sizes": [
```
**[REMOVED]**
```
(from line ~91)
            #      "reg__alpha": [

```
**[ADDED]**
```
91                #      "clf__alpha": [
```
**[REMOVED]**
```
(from line ~98)
            #      "reg__learning_rate_init": [

```
**[ADDED]**
```
98                #      "clf__learning_rate_init": [
```
**[REMOVED]**
```
(from line ~105)
            #      "reg__early_stopping": [True],
            #      "reg__validation_fraction": [

```
**[ADDED]**
```
105               #      "clf__early_stopping": [True],
106               #      "clf__validation_fraction": [
```
**[REMOVED]**
```
(from line ~112)
            #      "reg__max_iter": [

```
**[ADDED]**
```
112               #      "clf__max_iter": [
```
**[REMOVED]**
```
(from line ~117)
            #      "reg__n_iter_no_change": [

```
**[ADDED]**
```
117               #      "clf__n_iter_no_change": [
```
**[REMOVED]**
```
(from line ~122)
            #      "reg__tol": [

```
**[ADDED]**
```
122               #      "clf__tol": [
```
**[REMOVED]**
```
(from line ~128)
            #    "reg": [SVR()],
            #    "reg__C": [0.1, 1, 5, 10, 50, 100],
            #    "reg__kernel": ["rbf", "poly"],
            #    "reg__gamma": ["scale", "auto"],

```
**[ADDED]**
```
128               #    "clf": [SVR()],
129               #    "clf__C": [0.1, 1, 5, 10, 50, 100],
130               #    "clf__kernel": ["rbf", "poly"],
131               #    "clf__gamma": ["scale", "auto"],
```
**[REMOVED]**
```
(from line ~136)
            #    "reg": [LinearSVR(random_state=42)],
            #    "reg__max_iter": [1000, 2000],
            #    "reg__C": [0.1, 1, 5, 10, 50, 100],

```
**[ADDED]**
```
136               #    "clf": [LinearSVR(random_state=42)],
137               #    "clf__max_iter": [1000, 2000],
138               #    "clf__C": [0.1, 1, 5, 10, 50, 100],
```
**[REMOVED]**
```
(from line ~143)
            #    "reg": [RandomForestRegressor(random_state=42)],
            #    "reg__n_estimators": [100, 300, 500],
            #    "reg__max_depth": [None, 10, 20],
            #    "reg__criterion": ["squared_error", "absolute_error"],

```
**[ADDED]**
```
143               #    "clf": [RandomForestRegressor(random_state=42)],
144               #    "clf__n_estimators": [100, 300, 500],
145               #    "clf__max_depth": [None, 10, 20],
146               #    "clf__criterion": ["squared_error", "absolute_error"],
```
**[REMOVED]**
```
(from line ~151)
            #    "reg": [ExtraTreesRegressor(random_state=42)],
            #    "reg__n_estimators": [100, 300],
            #    "reg__max_depth": [None, 10, 20],
            #    "reg__criterion": ["squared_error", "absolute_error"],

```
**[ADDED]**
```
151               #    "clf": [ExtraTreesRegressor(random_state=42)],
152               #    "clf__n_estimators": [100, 300],
153               #    "clf__max_depth": [None, 10, 20],
154               #    "clf__criterion": ["squared_error", "absolute_error"],
```
**[REMOVED]**
```
(from line ~159)
            #    "reg": [GradientBoostingRegressor(random_state=42)],
            #    "reg__n_estimators": [100, 200],
            #    "reg__learning_rate": [0.05, 0.1, 0.2],
            #    "reg__max_depth": [3, 5],

```
**[ADDED]**
```
159               #    "clf": [GradientBoostingRegressor(random_state=42)],
160               #    "clf__n_estimators": [100, 200],
161               #    "clf__learning_rate": [0.05, 0.1, 0.2],
162               #    "clf__max_depth": [3, 5],
```
**[REMOVED]**
```
(from line ~167)
            #     "reg": [KNeighborsRegressor()],
            #     "reg__n_neighbors": [3, 5, 7, 9, 11, 13, 15, 17, 19],
            #     "reg__weights": ["uniform", "distance"],
            #     "reg__metric": ["euclidean", "manhattan"],

```
**[ADDED]**
```
167               #     "clf": [KNeighborsRegressor()],
168               #     "clf__n_neighbors": [3, 5, 7, 9, 11, 13, 15, 17, 19],
169               #     "clf__weights": ["uniform", "distance"],
170               #     "clf__metric": ["euclidean", "manhattan"],
```
**[REMOVED]**
```
(from line ~175)
                "reg": [LinearRegression()],

```
**[ADDED]**
```
175                   "clf": [LinearRegression()],
```
**[REMOVED]**
```
(from line ~180)
            #    "reg": [Ridge()],
            #    "reg__alpha": [0.1, 1.0, 10.0, 100.0],

```
**[ADDED]**
```
180               #    "clf": [Ridge()],
181               #    "clf__alpha": [0.1, 1.0, 10.0, 100.0],
```
**[REMOVED]**
```
(from line ~186)
            #    "reg": [Lasso(random_state=42)],
            #    "reg__alpha": [0.01, 0.1, 1.0, 10.0],

```
**[ADDED]**
```
186               #    "clf": [Lasso(random_state=42)],
187               #    "clf__alpha": [0.01, 0.1, 1.0, 10.0],
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/data_handler.py
*Saved at: 29/08/2026, 10:53:27*

**[REMOVED]**
```
(from line ~41)
            X, y, test_size=test_size, random_state=random_state, stratify=y

```
**[ADDED]**
```
41                X, y, test_size=test_size, random_state=random_state
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/data_handler.py
*Saved at: 29/08/2026, 10:53:03*

**[REMOVED]**
```
(from line ~70)
        X, y = preparar_dados_para_treino(self.data_path, self.results_path)

```
**[ADDED]**
```
70            X, y = preparar_dados_para_treino(self.data_path)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/data_handler.py
*Saved at: 29/08/2026, 10:52:24*

**[REMOVED]**
```
(from line ~72)
            X, y, test_size=test_size, random_state=random_state, stratify=y

```
**[ADDED]**
```
72                X, y, test_size=test_size, random_state=random_state
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/data_handler.py
*Saved at: 29/08/2026, 10:50:51*

**[REMOVED]**
```
(from line ~41)
            X, y, test_size=test_size, random_state=random_state

```
**[ADDED]**
```
41                X, y, test_size=test_size, random_state=random_state, stratify=y
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/data_handler.py
*Saved at: 29/08/2026, 10:50:20*

**[REMOVED]**
```
(from line ~41)
            X, y, test_size=test_size, random_state=random_state, stratify=y

```
**[ADDED]**
```
41                X, y, test_size=test_size, random_state=random_state
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 29/08/2026, 10:41:17*

**[REMOVED]**
```
(from line ~64)
            X, y = preparar_dados_para_treino(self.data_handler.data_path, self.data_handler.results_path)

```
**[ADDED]**
```
64                X, y = preparar_dados_para_treino(self.data_handler.data_path)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 29/08/2026, 10:40:31*

**[ADDED]**
```
174               {
175                   "reg": [LinearRegression()],
176                   "scaler": scalers,
177                   "reducao": reducoes,
178               },
```
**[REMOVED]**
```
(from line ~180)
            #    "reg": [LinearRegression()],
            #    "scaler": scalers,
            #    "reducao": reducoes,
            #},
            #{

```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 29/08/2026, 10:35:09*

**[REMOVED]**
```
(from line ~75)
             {
                 "scaler": scalers,
                 "reducao": reducoes,
                 "reg": [MLPRegressor(random_state=31)],
                 "reg__activation": [
                     "tanh",
                     "relu"
                 ],
                 "reg__hidden_layer_sizes": [
                     (24,),
                     (32,),
                     #(40,),
                     #(48,),
                     #(24, 12),
                     #(32, 16)
                 ],
                 "reg__alpha": [
                     0.00005,
                     0.0001,
                     #0.0002,
                     #0.0005,
                     #0.01
                 ],
                 "reg__learning_rate_init": [
                     #0.005,
                     #0.0075,
                     0.01,
                     0.015,
                     #0.1
                 ],
                 "reg__early_stopping": [True],
                 "reg__validation_fraction": [
                     0.08, 
                     0.10, 
                     #0.12, 
                     #0.15
                 ],
                 "reg__max_iter": [
                     500,
                     1000,
                     #1500
                 ],
                 "reg__n_iter_no_change": [
                     10, 
                     15, 
                     #20
                 ],
                 "reg__tol": [
                     0.0001, 
                     0.00005
                 ]
             },

```
**[ADDED]**
```
75                #  {
76                #      "scaler": scalers,
77                #      "reducao": reducoes,
78                #      "reg": [MLPRegressor(random_state=31)],
79                #      "reg__activation": [
80                #          "tanh",
81                #          "relu"
82                #      ],
83                #      "reg__hidden_layer_sizes": [
84                #          (24,),
85                #          (32,),
86                #          #(40,),
87                #          #(48,),
88                #          #(24, 12),
89                #          #(32, 16)
90                #      ],
91                #      "reg__alpha": [
92                #          0.00005,
93                #          0.0001,
94                #          #0.0002,
95                #          #0.0005,
96                #          #0.01
97                #      ],
98                #      "reg__learning_rate_init": [
99                #          #0.005,
100               #          #0.0075,
101               #          0.01,
102               #          0.015,
103               #          #0.1
104               #      ],
105               #      "reg__early_stopping": [True],
106               #      "reg__validation_fraction": [
107               #          0.08, 
108               #          0.10, 
109               #          #0.12, 
110               #          #0.15
111               #      ],
112               #      "reg__max_iter": [
113               #          500,
114               #          1000,
115               #          #1500
116               #      ],
117               #      "reg__n_iter_no_change": [
118               #          10, 
119               #          15, 
120               #          #20
121               #      ],
122               #      "reg__tol": [
123               #          0.0001, 
124               #          0.00005
125               #      ]
126               #  },
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 29/08/2026, 10:34:51*

**[REMOVED]**
```
(from line ~51)
            #PCA(n_components=0.95, random_state=31),

```
**[ADDED]**
```
51                PCA(n_components=0.95, random_state=31),
```
**[REMOVED]**
```
(from line ~53)
            #SelectKBest(score_func=f_regression, k="all")

```
**[ADDED]**
```
53                SelectKBest(score_func=f_regression, k="all")
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 29/08/2026, 10:34:35*

**[REMOVED]**
```
(from line ~31)
            #MinMaxScaler(),
            #MaxAbsScaler(),
            #QuantileTransformer(output_distribution="uniform", random_state=42),

```
**[ADDED]**
```
31                MinMaxScaler(),
32                MaxAbsScaler(),
33                QuantileTransformer(output_distribution="uniform", random_state=42),
```
**[REMOVED]**
```
(from line ~35)
            #PowerTransformer(method="yeo-johnson"),
            #Normalizer(norm="l2"),

```
**[ADDED]**
```
35                PowerTransformer(method="yeo-johnson"),
36                Normalizer(norm="l2"),
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/data_handler.py
*Saved at: 29/08/2026, 10:33:14*

**[REMOVED]**
```
(from line ~26)
        self.results_path = results_path

```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/data_handler.py
*Saved at: 29/08/2026, 10:33:12*

**[REMOVED]**
```
(from line ~17)
    def __init__(self, data_path: str, results_path: str) -> None:

```
**[ADDED]**
```
17        def __init__(self, data_path: str) -> None:
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 29/08/2026, 10:33:04*

**[REMOVED]**
```
(from line ~40)
        self.data_handler = DataHandler(data_path, results_path)

```
**[ADDED]**
```
40            self.data_handler = DataHandler(data_path)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 29/08/2026, 10:33:00*

**[REMOVED]**
```
(from line ~26)
        results_path: str,

```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 29/08/2026, 10:32:54*

**[REMOVED]**
```
(from line ~29)
        results_path=RESULTS_PATH,

```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 29/08/2026, 10:32:51*

**[REMOVED]**
```
(from line ~21)
    DATA_PATH = "./planilhas/Machine learning ganhos de forca (1).xlsx"

```
**[ADDED]**
```
21        DATA_PATH = "./planilhas/Machine_learning_ganhosde_forca.xlsx"
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 29/08/2026, 10:32:43*

**[REMOVED]**
```
(from line ~21)
    DATA_PATH = "./planilhas/planilhas_dados/dados_pe_frontal_esquerdo_150_2_col.xlsx"

```
**[ADDED]**
```
21        DATA_PATH = "./planilhas/Machine learning ganhos de forca (1).xlsx"
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 29/08/2026, 10:31:58*

**[REMOVED]**
```
(from line ~22)
    RESULTS_PATH = "./planilhas/planilhas_resultados/resultados_pe_frontal_esquerdo_150.xlsx"

```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 29/08/2026, 10:20:29*

**[REMOVED]**
```
(from line ~2)
Configuração de modelos, escaladores e grade de parâmetros.

```
**[ADDED]**
```
2     Configuração de modelos de regressão, escaladores e grade de parâmetros.
```
**[REMOVED]**
```
(from line ~9)
from sklearn.svm import SVC, LinearSVC

```
**[ADDED]**
```
9     from sklearn.svm import SVR, LinearSVR
```
**[REMOVED]**
```
(from line ~11)
    RandomForestClassifier, GradientBoostingClassifier, ExtraTreesClassifier

```
**[ADDED]**
```
11        RandomForestRegressor, GradientBoostingRegressor, ExtraTreesRegressor
```
**[REMOVED]**
```
(from line ~13)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression, Perceptron, RidgeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.feature_selection import SelectKBest, f_classif

```
**[ADDED]**
```
13    from sklearn.neighbors import KNeighborsRegressor
14    from sklearn.linear_model import (
15        LinearRegression, Ridge, Lasso, ElasticNet, SGDRegressor
16    )
17    from sklearn.neural_network import MLPRegressor
18    from sklearn.feature_selection import SelectKBest, f_regression
```
**[REMOVED]**
```
(from line ~23)
    """Gerencia a configuração dos classificadores e pré-processadores."""

```
**[ADDED]**
```
23        """Gerencia a configuração dos regressores e pré-processadores."""
```
**[REMOVED]**
```
(from line ~53)
            #SelectKBest(score_func=f_classif, k="all")

```
**[ADDED]**
```
53                #SelectKBest(score_func=f_regression, k="all")
```
**[REMOVED]**
```
(from line ~69)
            #     "clf": [Perceptron(random_state=42, class_weight="balanced")],
            #     "clf__eta0": [0.1, 0.01, 1.0],
            #     "clf__penalty": ["l2", "l1", "elasticnet"],

```
**[ADDED]**
```
69                #     "reg": [SGDRegressor(random_state=42)],
70                #     "reg__eta0": [0.1, 0.01, 0.001],
71                #     "reg__penalty": ["l2", "l1", "elasticnet"],
```
**[REMOVED]**
```
(from line ~78)
                 "clf": [MLPClassifier(random_state=31)],
                 "clf__activation": [

```
**[ADDED]**
```
78                     "reg": [MLPRegressor(random_state=31)],
79                     "reg__activation": [
```
**[REMOVED]**
```
(from line ~83)
                 "clf__hidden_layer_sizes": [

```
**[ADDED]**
```
83                     "reg__hidden_layer_sizes": [
```
**[REMOVED]**
```
(from line ~91)
                 "clf__alpha": [

```
**[ADDED]**
```
91                     "reg__alpha": [
```
**[REMOVED]**
```
(from line ~98)
                 "clf__learning_rate_init": [

```
**[ADDED]**
```
98                     "reg__learning_rate_init": [
```
**[REMOVED]**
```
(from line ~105)
                 "clf__early_stopping": [True],
                 "clf__validation_fraction": [

```
**[ADDED]**
```
105                    "reg__early_stopping": [True],
106                    "reg__validation_fraction": [
```
**[REMOVED]**
```
(from line ~112)
                 "clf__max_iter": [

```
**[ADDED]**
```
112                    "reg__max_iter": [
```
**[REMOVED]**
```
(from line ~117)
                 "clf__n_iter_no_change": [

```
**[ADDED]**
```
117                    "reg__n_iter_no_change": [
```
**[REMOVED]**
```
(from line ~119)
                    15, 

```
**[ADDED]**
```
119                        15, 
```
**[REMOVED]**
```
(from line ~122)
                 "clf__tol": [

```
**[ADDED]**
```
122                    "reg__tol": [
```
**[REMOVED]**
```
(from line ~128)
            #    "clf": [SVC(random_state=42, class_weight="balanced")],
            #    "clf__C": [0.1, 1, 5, 10, 50, 100],
            #    "clf__kernel": ["rbf", "poly"],
            #    "clf__gamma": ["scale", "auto"],

```
**[ADDED]**
```
128               #    "reg": [SVR()],
129               #    "reg__C": [0.1, 1, 5, 10, 50, 100],
130               #    "reg__kernel": ["rbf", "poly"],
131               #    "reg__gamma": ["scale", "auto"],
```
**[REMOVED]**
```
(from line ~136)
            #    "clf": [LinearSVC(random_state=42, class_weight="balanced")],
            #    "clf__max_iter": [1000, 2000],
            #    "clf__C": [0.1, 1, 5, 10, 50, 100],
            #    "clf__dual": [False],

```
**[ADDED]**
```
136               #    "reg": [LinearSVR(random_state=42)],
137               #    "reg__max_iter": [1000, 2000],
138               #    "reg__C": [0.1, 1, 5, 10, 50, 100],
```
**[REMOVED]**
```
(from line ~143)
            #    "clf": [RandomForestClassifier(random_state=42, class_weight="balanced")],
            #    "clf__n_estimators": [100, 300, 500],
            #    "clf__max_depth": [None, 10, 20],
            #    "clf__criterion": ["gini", "entropy"],

```
**[ADDED]**
```
143               #    "reg": [RandomForestRegressor(random_state=42)],
144               #    "reg__n_estimators": [100, 300, 500],
145               #    "reg__max_depth": [None, 10, 20],
146               #    "reg__criterion": ["squared_error", "absolute_error"],
```
**[REMOVED]**
```
(from line ~151)
            #    "clf": [ExtraTreesClassifier(random_state=42, class_weight="balanced")],
            #    "clf__n_estimators": [100, 300],
            #    "clf__max_depth": [None, 10, 20],
            #    "clf__criterion": ["gini", "entropy"],

```
**[ADDED]**
```
151               #    "reg": [ExtraTreesRegressor(random_state=42)],
152               #    "reg__n_estimators": [100, 300],
153               #    "reg__max_depth": [None, 10, 20],
154               #    "reg__criterion": ["squared_error", "absolute_error"],
```
**[REMOVED]**
```
(from line ~159)
            #    "clf": [GradientBoostingClassifier(random_state=42)],
            #    "clf__n_estimators": [100, 200],
            #    "clf__learning_rate": [0.05, 0.1, 0.2],
            #    "clf__max_depth": [3, 5],

```
**[ADDED]**
```
159               #    "reg": [GradientBoostingRegressor(random_state=42)],
160               #    "reg__n_estimators": [100, 200],
161               #    "reg__learning_rate": [0.05, 0.1, 0.2],
162               #    "reg__max_depth": [3, 5],
```
**[REMOVED]**
```
(from line ~167)
            #     "clf": [KNeighborsClassifier()],
            #     "clf__n_neighbors": [3, 5, 7, 9, 11, 13, 15, 17, 19],
            #     "clf__weights": ["uniform", "distance"],
            #     "clf__metric": ["euclidean", "manhattan"],

```
**[ADDED]**
```
167               #     "reg": [KNeighborsRegressor()],
168               #     "reg__n_neighbors": [3, 5, 7, 9, 11, 13, 15, 17, 19],
169               #     "reg__weights": ["uniform", "distance"],
170               #     "reg__metric": ["euclidean", "manhattan"],
```
**[REMOVED]**
```
(from line ~175)
            #    "clf": [LogisticRegression(random_state=42, class_weight="balanced", max_iter=1000)],
            #    "clf__C": [0.01, 0.1, 1, 5, 10, 50, 100],
            #    "clf__solver": ["liblinear", "lbfgs"],

```
**[ADDED]**
```
175               #    "reg": [LinearRegression()],
```
**[REMOVED]**
```
(from line ~180)
            #    "clf": [RidgeClassifier(class_weight="balanced")],
            #    "clf__alpha": [0.1, 1.0, 10.0, 100.0],

```
**[ADDED]**
```
180               #    "reg": [Ridge()],
181               #    "reg__alpha": [0.1, 1.0, 10.0, 100.0],
```
**[ADDED]**
```
185               #{
186               #    "reg": [Lasso(random_state=42)],
187               #    "reg__alpha": [0.01, 0.1, 1.0, 10.0],
188               #    "scaler": scalers,
189               #    "reducao": ["passthrough"],
190               #},
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 29/08/2026, 10:08:01*

**[REMOVED]**
```
(from line ~55)
        removed_features_mlp = ["ankle_y_std", "ankle_x_iqr", "heel_x_std", "big_toe_y_std", "heel_x_iqr", "big_toe_x_iqr", "heel_y_iqr"]

```
**[ADDED]**
```
55            #removed_features_mlp = ["ankle_y_std", "ankle_x_iqr", "heel_x_std", "big_toe_y_std", "heel_x_iqr", "big_toe_x_iqr", "heel_y_iqr"]
```
**[REMOVED]**
```
(from line ~66)
            X = self.data_handler.remove_feature(X, removed_features_mlp)

```
**[ADDED]**
```
66                #X = self.data_handler.remove_feature(X, removed_features_mlp)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/excel_geter.py
*Saved at: 29/08/2026, 09:55:56*

**[REMOVED]**
```
(from line ~22)
    feature_names = df_estatistico.columns[2:].tolist()  # Pegando os nomes das colunas a partir da terceira coluna

```
**[ADDED]**
```
22        feature_names = df_estatistico.columns[:-1].tolist()  # Pegando os nomes das colunas exepto a ultima
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/excel_geter.py
*Saved at: 29/08/2026, 09:54:39*

**[REMOVED]**
```
(from line ~3)
def preparar_dados_para_treino(caminho_estatistico, caminho_resultados):
    """Função que pega os valores da planilha de estatístico e de resultados e retorna os dados para o treinameto"""

```
**[ADDED]**
```
3     import pandas as pd
4     
5     def preparar_dados_para_treino(caminho_estatistico):
6         """Função que pega todas as colunas exceto a última para o X e a última para o y"""
```
**[REMOVED]**
```
(from line ~8)
    # Leitura dos dados estatísticos

```
**[ADDED]**
```
8         # Leitura dos dados
```
**[REMOVED]**
```
(from line ~11)
    # Extrai todas as colunas a partir da terceira coluna
    X = df_estatistico.iloc[:, 2:]

```
**[ADDED]**
```
11        # X pega todas as colunas EXCETO a última
12        X = df_estatistico.iloc[:, :-1]
```
**[REMOVED]**
```
(from line ~14)
    # Leitura dos dados de resultados
    df_resultados = pd.read_excel(caminho_resultados, engine='openpyxl')
    
    # Extrai apenas a coluna 'Resultado' como um vetor (0 e 1)
    y = df_resultados['Resultado'].values

```
**[ADDED]**
```
14        # y pega APENAS a última coluna
15        y = df_estatistico.iloc[:, -1].values
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/excel_geter.py
*Saved at: 18/08/2026, 18:53:05*

**[REMOVED]**
```
(from line ~17)
    

```
**[ADDED]**
```
17    
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 06/07/2026, 23:44:00*

**[REMOVED]**
```
(from line ~35)
    controller.run_data_analysis()
    #controller.run()

```
**[ADDED]**
```
35        #controller.run_data_analysis()
36        controller.run()
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 06/07/2026, 23:43:39*

**[REMOVED]**
```
(from line ~13)
    dict_params = {'clf': [MLPClassifier(random_state=31)], 'clf__activation': ['tanh'], 'clf__alpha': [0.0001], 'clf__early_stopping': [True], 'clf__hidden_layer_sizes': [(32,)], 'clf__learning_rate_init': [0.01], 'clf__max_iter': [1000], 'clf__validation_fraction': [0.1], 'reducao': ['passthrough'], 'scaler': [RobustScaler()]}

```
**[ADDED]**
```
13        #dict_params = {'clf': [MLPClassifier(random_state=31)], 'clf__activation': ['tanh'], 'clf__alpha': [0.0001], 'clf__early_stopping': [True], 'clf__hidden_layer_sizes': [(32,)], 'clf__learning_rate_init': [0.01], 'clf__max_iter': [1000], 'clf__validation_fraction': [0.1], 'reducao': ['passthrough'], 'scaler': [RobustScaler()]}
```
**[REMOVED]**
```
(from line ~18)
    #dict_params = None

```
**[ADDED]**
```
18        dict_params = None
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 06/07/2026, 23:43:31*

**[REMOVED]**
```
(from line ~66)
            X = self.data_handler.remove_feature(X, removed_features_knn)

```
**[ADDED]**
```
66                X = self.data_handler.remove_feature(X, removed_features_mlp)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 06/07/2026, 23:43:25*

**[ADDED]**
```
55            removed_features_mlp = ["ankle_y_std", "ankle_x_iqr", "heel_x_std", "big_toe_y_std", "heel_x_iqr", "big_toe_x_iqr", "heel_y_iqr"]
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 06/07/2026, 23:33:15*

**[REMOVED]**
```
(from line ~35)
    #controller.run_data_analysis()
    controller.run()

```
**[ADDED]**
```
35        controller.run_data_analysis()
36        #controller.run()
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 06/07/2026, 23:33:05*

**[REMOVED]**
```
(from line ~97)
        #rs = 777 # random_state do melhor modelo encontrado para o MLP
        rs = 647 # random_state do melhor modelo encontrado para o KNN

```
**[ADDED]**
```
97            rs = 777 # random_state do melhor modelo encontrado para o MLP
98            #rs = 647 # random_state do melhor modelo encontrado para o KNN
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 06/07/2026, 23:32:55*

**[REMOVED]**
```
(from line ~27)
            StandardScaler(),
            RobustScaler(),
            MinMaxScaler(),
            MaxAbsScaler(),
            QuantileTransformer(output_distribution="uniform", random_state=42),
            QuantileTransformer(output_distribution="normal", random_state=42),
            PowerTransformer(method="yeo-johnson"),
            Normalizer(norm="l2"),

```
**[ADDED]**
```
27                #StandardScaler(),
28                #RobustScaler(),
29                #MinMaxScaler(),
30                #MaxAbsScaler(),
31                #QuantileTransformer(output_distribution="uniform", random_state=42),
32                #QuantileTransformer(output_distribution="normal", random_state=42),
33                #PowerTransformer(method="yeo-johnson"),
34                #Normalizer(norm="l2"),
```
**[REMOVED]**
```
(from line ~37)
            #RobustScaler(),

```
**[ADDED]**
```
37                RobustScaler(),
```
**[REMOVED]**
```
(from line ~41)
            #StandardScaler(),

```
**[ADDED]**
```
41                StandardScaler(),
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 06/07/2026, 23:32:40*

**[REMOVED]**
```
(from line ~117)
                        15, 

```
**[ADDED]**
```
117                       15, 
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 06/07/2026, 23:19:16*

**[REMOVED]**
```
(from line ~99)
        removed_features_knn = ["heel_x_iqr"]

```
**[ADDED]**
```
99            #removed_features_knn = ["heel_x_iqr"]
```
**[REMOVED]**
```
(from line ~103)
        X = self.data_handler.remove_feature(X, removed_features_knn)

```
**[ADDED]**
```
103           #X = self.data_handler.remove_feature(X, removed_features_knn)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 06/07/2026, 23:19:01*

**[REMOVED]**
```
(from line ~56)
        removed_features_knn = ["ankle_x_std", "ankle_x_iqr", "ankle_y_std", "big_toe_y_std", "big_toe_y_iqr", "heel_x_std", "heel_x_iqr", "heel_y_std"]

```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 06/07/2026, 23:04:53*

**[REMOVED]**
```
(from line ~13)
    #dict_params = {'clf': [MLPClassifier(random_state=31)], 'clf__activation': ['tanh'], 'clf__alpha': [0.0001], 'clf__early_stopping': [True], 'clf__hidden_layer_sizes': [(32,)], 'clf__learning_rate_init': [0.01], 'clf__max_iter': [1000], 'clf__validation_fraction': [0.1], 'reducao': ['passthrough'], 'scaler': [RobustScaler()]}

```
**[ADDED]**
```
13        dict_params = {'clf': [MLPClassifier(random_state=31)], 'clf__activation': ['tanh'], 'clf__alpha': [0.0001], 'clf__early_stopping': [True], 'clf__hidden_layer_sizes': [(32,)], 'clf__learning_rate_init': [0.01], 'clf__max_iter': [1000], 'clf__validation_fraction': [0.1], 'reducao': ['passthrough'], 'scaler': [RobustScaler()]}
```
**[REMOVED]**
```
(from line ~18)
    dict_params = None

```
**[ADDED]**
```
18        #dict_params = None
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 06/07/2026, 23:04:35*

**[REMOVED]**
```
(from line ~113)
                     1500

```
**[ADDED]**
```
113                        #1500
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 06/07/2026, 23:04:29*

**[REMOVED]**
```
(from line ~125)
            {

```
**[ADDED]**
```
125               #{
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 06/07/2026, 23:04:27*

**[REMOVED]**
```
(from line ~73)
            #  {
            #      "scaler": scalers,
            #      "reducao": reducoes,
            #      "clf": [MLPClassifier(random_state=31)],
            #      "clf__activation": [
            #          "tanh",
            #          "relu"
            #      ],
            #      "clf__hidden_layer_sizes": [
            #          (24,),
            #          (32,),
            #          #(40,),
            #          #(48,),
            #          #(24, 12),
            #          #(32, 16)
            #      ],
            #      "clf__alpha": [
            #          0.00005,
            #          0.0001,
            #          #0.0002,
            #          #0.0005,
            #          #0.01
            #      ],
            #      "clf__learning_rate_init": [
            #          #0.005,
            #          #0.0075,
            #          0.01,
            #          0.015,
            #          #0.1
            #      ],
            #      "clf__early_stopping": [True],
            #      "clf__validation_fraction": [
            #          0.08, 
            #          0.10, 
            #          #0.12, 
            #          #0.15
            #      ],
            #      "clf__max_iter": [
            #          500,
            #          1000,
            #          1500
            #      ],
            #      "clf__n_iter_no_change": [
            #          10, 
            #             15, 
            #          #20
            #      ],
            #      "clf__tol": [
            #          0.0001, 
            #          0.00005
            #      ]
            #  },
            #{

```
**[ADDED]**
```
73                 {
74                     "scaler": scalers,
75                     "reducao": reducoes,
76                     "clf": [MLPClassifier(random_state=31)],
77                     "clf__activation": [
78                         "tanh",
79                         "relu"
80                     ],
81                     "clf__hidden_layer_sizes": [
82                         (24,),
83                         (32,),
84                         #(40,),
85                         #(48,),
86                         #(24, 12),
87                         #(32, 16)
88                     ],
89                     "clf__alpha": [
90                         0.00005,
91                         0.0001,
92                         #0.0002,
93                         #0.0005,
94                         #0.01
95                     ],
96                     "clf__learning_rate_init": [
97                         #0.005,
98                         #0.0075,
99                         0.01,
100                        0.015,
101                        #0.1
102                    ],
103                    "clf__early_stopping": [True],
104                    "clf__validation_fraction": [
105                        0.08, 
106                        0.10, 
107                        #0.12, 
108                        #0.15
109                    ],
110                    "clf__max_iter": [
111                        500,
112                        1000,
113                        1500
114                    ],
115                    "clf__n_iter_no_change": [
116                        10, 
117                           15, 
118                        #20
119                    ],
120                    "clf__tol": [
121                        0.0001, 
122                        0.00005
123                    ]
124                },
125               {
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 06/07/2026, 23:04:09*

**[REMOVED]**
```
(from line ~165)
            {
                 "clf": [KNeighborsClassifier()],
                 "clf__n_neighbors": [3, 5, 7, 9, 11, 13, 15, 17, 19],
                 "clf__weights": ["uniform", "distance"],
                 "clf__metric": ["euclidean", "manhattan"],
                 "scaler": scalers,
                 "reducao": reducoes,
            },

```
**[ADDED]**
```
166               #     "clf": [KNeighborsClassifier()],
167               #     "clf__n_neighbors": [3, 5, 7, 9, 11, 13, 15, 17, 19],
168               #     "clf__weights": ["uniform", "distance"],
169               #     "clf__metric": ["euclidean", "manhattan"],
170               #     "scaler": scalers,
171               #     "reducao": reducoes,
172               #},
173               #{
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 06/07/2026, 22:55:59*

**[REMOVED]**
```
(from line ~18)
    #dict_params = None

```
**[ADDED]**
```
18        dict_params = None
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 06/07/2026, 22:55:55*

**[REMOVED]**
```
(from line ~16)
    dict_params = {'clf': [KNeighborsClassifier()], 'clf__metric': ['euclidean'], 'clf__n_neighbors': [5], 'clf__weights': ['uniform'], 'reducao': ['passthrough'], 'scaler': [PowerTransformer()]}

```
**[ADDED]**
```
16        #dict_params = {'clf': [KNeighborsClassifier()], 'clf__metric': ['euclidean'], 'clf__n_neighbors': [5], 'clf__weights': ['uniform'], 'reducao': ['passthrough'], 'scaler': [PowerTransformer()]}
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 06/07/2026, 22:55:51*

**[REMOVED]**
```
(from line ~35)
    controller.run_data_analysis()
    #controller.run()

```
**[ADDED]**
```
35        #controller.run_data_analysis()
36        controller.run()
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 06/07/2026, 22:55:44*

**[REMOVED]**
```
(from line ~66)
            X = self.data_handler.remove_feature(X, removed_features_mlp)

```
**[ADDED]**
```
66                X = self.data_handler.remove_feature(X, removed_features_knn)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 06/07/2026, 22:55:39*

**[REMOVED]**
```
(from line ~54)
        removed_features_mlp = ["big_toe_x_iqr", "heel_y_iqr"]

```
**[ADDED]**
```
54            #removed_features_mlp = ["big_toe_x_iqr", "heel_y_iqr"]
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 06/07/2026, 22:51:10*

**[REMOVED]**
```
(from line ~56)
        removed_features_knn = [""]

```
**[ADDED]**
```
56            removed_features_knn = ["ankle_x_std", "ankle_x_iqr", "ankle_y_std", "big_toe_y_std", "big_toe_y_iqr", "heel_x_std", "heel_x_iqr", "heel_y_std"]
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 06/07/2026, 22:31:15*

**[ADDED]**
```
56            removed_features_knn = [""]
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 06/07/2026, 22:24:59*

**[REMOVED]**
```
(from line ~35)
    #controller.run_data_analysis()
    controller.run()

```
**[ADDED]**
```
35        controller.run_data_analysis()
36        #controller.run()
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 06/07/2026, 21:45:03*

**[REMOVED]**
```
(from line ~99)
        removed_features_knn = ["heel_x_iqr", "heel_y_std"]

```
**[ADDED]**
```
99            removed_features_knn = ["heel_x_iqr"]
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 06/07/2026, 21:25:19*

**[REMOVED]**
```
(from line ~97)
        rs = 777 # random_state do melhor modelo encontrado para o MLP
        #rs = 647 # random_state do melhor modelo encontrado para o KNN

```
**[ADDED]**
```
97            #rs = 777 # random_state do melhor modelo encontrado para o MLP
98            rs = 647 # random_state do melhor modelo encontrado para o KNN
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 06/07/2026, 21:25:11*

**[REMOVED]**
```
(from line ~32)
        iterations=1,

```
**[ADDED]**
```
32            iterations=10,
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 06/07/2026, 21:25:02*

**[REMOVED]**
```
(from line ~32)
        iterations=10,

```
**[ADDED]**
```
32            iterations=1,
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 06/07/2026, 21:24:57*

**[REMOVED]**
```
(from line ~18)
    dict_params = None

```
**[ADDED]**
```
18        #dict_params = None
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 06/07/2026, 21:24:52*

**[REMOVED]**
```
(from line ~16)
    #dict_params = {'clf': [KNeighborsClassifier()], 'clf__metric': ['euclidean'], 'clf__n_neighbors': [5], 'clf__weights': ['uniform'], 'reducao': ['passthrough'], 'scaler': [PowerTransformer()]}

```
**[ADDED]**
```
16        dict_params = {'clf': [KNeighborsClassifier()], 'clf__metric': ['euclidean'], 'clf__n_neighbors': [5], 'clf__weights': ['uniform'], 'reducao': ['passthrough'], 'scaler': [PowerTransformer()]}
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 06/07/2026, 21:24:38*

**[REMOVED]**
```
(from line ~99)
        #removed_features_knn = ["heel_x_iqr", "heel_y_std"]

```
**[ADDED]**
```
99            removed_features_knn = ["heel_x_iqr", "heel_y_std"]
```
**[REMOVED]**
```
(from line ~103)
        X = self.data_handler.remove_feature(X, removed_features_mlp)

```
**[ADDED]**
```
103           X = self.data_handler.remove_feature(X, removed_features_knn)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 06/07/2026, 21:24:31*

**[REMOVED]**
```
(from line ~103)
        #X = self.data_handler.remove_feature(X, removed_features_mlp)

```
**[ADDED]**
```
103           X = self.data_handler.remove_feature(X, removed_features_mlp)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 06/07/2026, 21:23:39*

**[REMOVED]**
```
(from line ~73)
             {
                 "scaler": scalers,
                 "reducao": reducoes,
                 "clf": [MLPClassifier(random_state=31)],
                 "clf__activation": [
                     "tanh",
                     "relu"
                 ],
                 "clf__hidden_layer_sizes": [
                     (24,),
                     (32,),
                     #(40,),
                     #(48,),
                     #(24, 12),
                     #(32, 16)
                 ],
                 "clf__alpha": [
                     0.00005,
                     0.0001,
                     #0.0002,
                     #0.0005,
                     #0.01
                 ],
                 "clf__learning_rate_init": [
                     #0.005,
                     #0.0075,
                     0.01,
                     0.015,
                     #0.1
                 ],
                 "clf__early_stopping": [True],
                 "clf__validation_fraction": [
                     0.08, 
                     0.10, 
                     #0.12, 
                     #0.15
                 ],
                 "clf__max_iter": [
                     500,
                     1000,
                     1500
                 ],
                 "clf__n_iter_no_change": [
                     10, 
                        15, 
                     #20
                 ],
                 "clf__tol": [
                     0.0001, 
                     0.00005
                 ]
             },

```
**[ADDED]**
```
73                #  {
74                #      "scaler": scalers,
75                #      "reducao": reducoes,
76                #      "clf": [MLPClassifier(random_state=31)],
77                #      "clf__activation": [
78                #          "tanh",
79                #          "relu"
80                #      ],
81                #      "clf__hidden_layer_sizes": [
82                #          (24,),
83                #          (32,),
84                #          #(40,),
85                #          #(48,),
86                #          #(24, 12),
87                #          #(32, 16)
88                #      ],
89                #      "clf__alpha": [
90                #          0.00005,
91                #          0.0001,
92                #          #0.0002,
93                #          #0.0005,
94                #          #0.01
95                #      ],
96                #      "clf__learning_rate_init": [
97                #          #0.005,
98                #          #0.0075,
99                #          0.01,
100               #          0.015,
101               #          #0.1
102               #      ],
103               #      "clf__early_stopping": [True],
104               #      "clf__validation_fraction": [
105               #          0.08, 
106               #          0.10, 
107               #          #0.12, 
108               #          #0.15
109               #      ],
110               #      "clf__max_iter": [
111               #          500,
112               #          1000,
113               #          1500
114               #      ],
115               #      "clf__n_iter_no_change": [
116               #          10, 
117               #             15, 
118               #          #20
119               #      ],
120               #      "clf__tol": [
121               #          0.0001, 
122               #          0.00005
123               #      ]
124               #  },
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 06/07/2026, 21:22:50*

**[REMOVED]**
```
(from line ~27)
            #StandardScaler(),
            #RobustScaler(),
            #MinMaxScaler(),
            #MaxAbsScaler(),
            #QuantileTransformer(output_distribution="uniform", random_state=42),
            #QuantileTransformer(output_distribution="normal", random_state=42),
            #PowerTransformer(method="yeo-johnson"),
            #Normalizer(norm="l2"),

```
**[ADDED]**
```
27                StandardScaler(),
28                RobustScaler(),
29                MinMaxScaler(),
30                MaxAbsScaler(),
31                QuantileTransformer(output_distribution="uniform", random_state=42),
32                QuantileTransformer(output_distribution="normal", random_state=42),
33                PowerTransformer(method="yeo-johnson"),
34                Normalizer(norm="l2"),
```
**[REMOVED]**
```
(from line ~37)
            RobustScaler(),
            #RobustScaler(quantile_range=(20, 80)),
            #RobustScaler(quantile_range=(10, 90)),
            #RobustScaler(quantile_range=(30, 70)),
            StandardScaler(),

```
**[ADDED]**
```
37                #RobustScaler(),
38                ##RobustScaler(quantile_range=(20, 80)),
39                ##RobustScaler(quantile_range=(10, 90)),
40                ##RobustScaler(quantile_range=(30, 70)),
41                #StandardScaler(),
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 06/07/2026, 21:21:37*

**[REMOVED]**
```
(from line ~117)
                     15, 

```
**[ADDED]**
```
117                           15, 
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 06/07/2026, 21:20:10*

**[REMOVED]**
```
(from line ~107)
                     0.12, 

```
**[ADDED]**
```
107                        #0.12, 
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 30/06/2026, 10:36:34*

**[REMOVED]**
```
(from line ~27)
            StandardScaler(),
            RobustScaler(),
            MinMaxScaler(),
            MaxAbsScaler(),
            QuantileTransformer(output_distribution="uniform", random_state=42),
            QuantileTransformer(output_distribution="normal", random_state=42),
            PowerTransformer(method="yeo-johnson"),
            Normalizer(norm="l2"),

```
**[ADDED]**
```
27                #StandardScaler(),
28                #RobustScaler(),
29                #MinMaxScaler(),
30                #MaxAbsScaler(),
31                #QuantileTransformer(output_distribution="uniform", random_state=42),
32                #QuantileTransformer(output_distribution="normal", random_state=42),
33                #PowerTransformer(method="yeo-johnson"),
34                #Normalizer(norm="l2"),
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 30/06/2026, 10:36:18*

**[REMOVED]**
```
(from line ~13)
    dict_params = {'clf': [MLPClassifier(random_state=31)], 'clf__activation': ['tanh'], 'clf__alpha': [0.0001], 'clf__early_stopping': [True], 'clf__hidden_layer_sizes': [(32,)], 'clf__learning_rate_init': [0.01], 'clf__max_iter': [1000], 'clf__validation_fraction': [0.1], 'reducao': ['passthrough'], 'scaler': [RobustScaler()]}

```
**[ADDED]**
```
13        #dict_params = {'clf': [MLPClassifier(random_state=31)], 'clf__activation': ['tanh'], 'clf__alpha': [0.0001], 'clf__early_stopping': [True], 'clf__hidden_layer_sizes': [(32,)], 'clf__learning_rate_init': [0.01], 'clf__max_iter': [1000], 'clf__validation_fraction': [0.1], 'reducao': ['passthrough'], 'scaler': [RobustScaler()]}
```
**[REMOVED]**
```
(from line ~18)
    #dict_params = None

```
**[ADDED]**
```
18        dict_params = None
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 30/06/2026, 10:35:15*

**[REMOVED]**
```
(from line ~28)
            RobustScaler(),

```
**[ADDED]**
```
28                #RobustScaler(),
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 30/06/2026, 10:33:44*

**[REMOVED]**
```
(from line ~27)
            #StandardScaler(),
            #RobustScaler(),
            #MinMaxScaler(),
            #MaxAbsScaler(),
            #QuantileTransformer(output_distribution="uniform", random_state=42),
            #QuantileTransformer(output_distribution="normal", random_state=42),
            #PowerTransformer(method="yeo-johnson"),
            #Normalizer(norm="l2"),

```
**[ADDED]**
```
27                StandardScaler(),
28                RobustScaler(),
29                MinMaxScaler(),
30                MaxAbsScaler(),
31                QuantileTransformer(output_distribution="uniform", random_state=42),
32                QuantileTransformer(output_distribution="normal", random_state=42),
33                PowerTransformer(method="yeo-johnson"),
34                Normalizer(norm="l2"),
```
**[REMOVED]**
```
(from line ~37)
            RobustScaler(),

```
**[ADDED]**
```
37                #RobustScaler(),
```
**[REMOVED]**
```
(from line ~41)
            StandardScaler(),

```
**[ADDED]**
```
41                #StandardScaler(),
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 30/06/2026, 10:30:19*

**[REMOVED]**
```
(from line ~113)
                     #1500

```
**[ADDED]**
```
113                        1500
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 30/06/2026, 10:30:06*

**[REMOVED]**
```
(from line ~105)
                    # 0.08, 

```
**[ADDED]**
```
105                        0.08, 
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 30/06/2026, 10:29:57*

**[REMOVED]**
```
(from line ~98)
                     #0.0075,

```
**[ADDED]**
```
98                         0.0075,
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 30/06/2026, 10:29:48*

**[REMOVED]**
```
(from line ~84)
                     #(40,),

```
**[ADDED]**
```
84                         (40,),
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 30/06/2026, 10:29:44*

**[REMOVED]**
```
(from line ~84)
                     (40,),

```
**[ADDED]**
```
84                         #(40,),
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 30/06/2026, 10:29:26*

**[REMOVED]**
```
(from line ~90)
                     #0.00005,

```
**[ADDED]**
```
90                         0.00005,
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 30/06/2026, 10:29:12*

**[REMOVED]**
```
(from line ~28)
            RobustScaler(),

```
**[ADDED]**
```
28                #RobustScaler(),
```
**[REMOVED]**
```
(from line ~37)
            #RobustScaler(),
            #RobustScaler(quantile_range=(20, 80)),
            #RobustScaler(quantile_range=(10, 90)),
            #RobustScaler(quantile_range=(30, 70)),
            #StandardScaler(),

```
**[ADDED]**
```
37                RobustScaler(),
38                RobustScaler(quantile_range=(20, 80)),
39                RobustScaler(quantile_range=(10, 90)),
40                RobustScaler(quantile_range=(30, 70)),
41                StandardScaler(),
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 30/06/2026, 10:28:14*

**[REMOVED]**
```
(from line ~84)
                    (40,),

```
**[ADDED]**
```
84                         (40,),
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 30/06/2026, 10:28:07*

**[REMOVED]**
```
(from line ~84)
                    #(40,),

```
**[ADDED]**
```
84                        (40,),
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 30/06/2026, 10:26:50*

**[REMOVED]**
```
(from line ~54)
        removed_features_mlp = ["heel_y_iqr"]
        # "big_toe_x_iqr"

```
**[ADDED]**
```
54            removed_features_mlp = ["big_toe_x_iqr", "heel_y_iqr"]
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 30/06/2026, 10:25:07*

**[REMOVED]**
```
(from line ~54)
        removed_features_mlp = ["big_toe_x_iqr", "heel_y_iqr"]

```
**[ADDED]**
```
54            removed_features_mlp = ["heel_y_iqr"]
55            # "big_toe_x_iqr"
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 30/06/2026, 10:24:44*

**[REMOVED]**
```
(from line ~32)
        iterations=1,

```
**[ADDED]**
```
32            iterations=10,
```
**[REMOVED]**
```
(from line ~35)
    controller.run_data_analysis()
    #controller.run()

```
**[ADDED]**
```
35        #controller.run_data_analysis()
36        controller.run()
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 30/06/2026, 10:24:18*

**[REMOVED]**
```
(from line ~54)
        removed_features_mlp = ["big_toe_x_iqr", "heel_x_iqr"]

```
**[ADDED]**
```
54            removed_features_mlp = ["big_toe_x_iqr", "heel_y_iqr"]
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 30/06/2026, 10:24:02*

**[REMOVED]**
```
(from line ~54)
        removed_features_mlp = ["big_toe_x_iqr"]

```
**[ADDED]**
```
54            removed_features_mlp = ["big_toe_x_iqr", "heel_x_iqr"]
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 30/06/2026, 10:23:48*

**[REMOVED]**
```
(from line ~54)
        removed_features_mlp = ["big_toe_x_std"]

```
**[ADDED]**
```
54            removed_features_mlp = ["big_toe_x_iqr"]
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 30/06/2026, 10:23:42*

**[REMOVED]**
```
(from line ~100)
        #removed_features_mlp = ["big_toe_x_std"]

```
**[ADDED]**
```
100           #removed_features_mlp = ["big_toe_x_iqr"]
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 30/06/2026, 10:22:27*

**[REMOVED]**
```
(from line ~32)
        iterations=10,

```
**[ADDED]**
```
32            iterations=1,
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 30/06/2026, 10:21:26*

**[REMOVED]**
```
(from line ~18)
    dict_params = None

```
**[ADDED]**
```
18        #dict_params = None
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 30/06/2026, 10:21:09*

**[REMOVED]**
```
(from line ~35)
    #controller.run_data_analysis()

```
**[ADDED]**
```
35        controller.run_data_analysis()
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 30/06/2026, 10:20:41*

**[REMOVED]**
```
(from line ~36)
    controller.run()

```
**[ADDED]**
```
36        #controller.run()
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 30/06/2026, 10:17:38*

**[REMOVED]**
```
(from line ~32)
        iterations=5,

```
**[ADDED]**
```
32            iterations=10,
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 30/06/2026, 10:17:16*

**[REMOVED]**
```
(from line ~35)
    controller.run_data_analysis()
    #controller.run()

```
**[ADDED]**
```
35        #controller.run_data_analysis()
36        controller.run()
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 30/06/2026, 10:16:51*

**[REMOVED]**
```
(from line ~27)
            StandardScaler(),

```
**[ADDED]**
```
27                #StandardScaler(),
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 30/06/2026, 10:16:48*

**[REMOVED]**
```
(from line ~29)
            MinMaxScaler(),
            MaxAbsScaler(),
            QuantileTransformer(output_distribution="uniform", random_state=42),
            QuantileTransformer(output_distribution="normal", random_state=42),
            PowerTransformer(method="yeo-johnson"),
            Normalizer(norm="l2"),

```
**[ADDED]**
```
29                #MinMaxScaler(),
30                #MaxAbsScaler(),
31                #QuantileTransformer(output_distribution="uniform", random_state=42),
32                #QuantileTransformer(output_distribution="normal", random_state=42),
33                #PowerTransformer(method="yeo-johnson"),
34                #Normalizer(norm="l2"),
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 30/06/2026, 10:16:25*

**[REMOVED]**
```
(from line ~73)
            #  {
            #      "scaler": scalers,
            #      "reducao": reducoes,
            #      "clf": [MLPClassifier(random_state=31)],
            #      "clf__activation": [
            #          "tanh",
            #          "relu"
            #      ],
            #      "clf__hidden_layer_sizes": [
            #          (24,),
            #          (32,),
            #         #(40,),
            #          #(48,),
            #          #(24, 12),
            #          #(32, 16)
            #      ],
            #      "clf__alpha": [
            #          #0.00005,
            #          0.0001,
            #          0.0002,
            #          #0.0005,
            #          #0.01
            #      ],
            #      "clf__learning_rate_init": [
            #          #0.005,
            #          #0.0075,
            #          0.01,
            #          0.015,
            #          #0.1
            #      ],
            #      "clf__early_stopping": [True],
            #      "clf__validation_fraction": [
            #         # 0.08, 
            #          0.10, 
            #          0.12, 
            #          #0.15
            #      ],
            #      "clf__max_iter": [
            #          500,
            #          1000,
            #          #1500
            #      ],
            #      "clf__n_iter_no_change": [
            #          10, 
            #          15, 
            #          #20
            #      ],
            #      "clf__tol": [
            #          0.0001, 
            #          0.00005
            #      ]
            #  },

```
**[ADDED]**
```
73                 {
74                     "scaler": scalers,
75                     "reducao": reducoes,
76                     "clf": [MLPClassifier(random_state=31)],
77                     "clf__activation": [
78                         "tanh",
79                         "relu"
80                     ],
81                     "clf__hidden_layer_sizes": [
82                         (24,),
83                         (32,),
84                        #(40,),
85                         #(48,),
86                         #(24, 12),
87                         #(32, 16)
88                     ],
89                     "clf__alpha": [
90                         #0.00005,
91                         0.0001,
92                         0.0002,
93                         #0.0005,
94                         #0.01
95                     ],
96                     "clf__learning_rate_init": [
97                         #0.005,
98                         #0.0075,
99                         0.01,
100                        0.015,
101                        #0.1
102                    ],
103                    "clf__early_stopping": [True],
104                    "clf__validation_fraction": [
105                       # 0.08, 
106                        0.10, 
107                        0.12, 
108                        #0.15
109                    ],
110                    "clf__max_iter": [
111                        500,
112                        1000,
113                        #1500
114                    ],
115                    "clf__n_iter_no_change": [
116                        10, 
117                        15, 
118                        #20
119                    ],
120                    "clf__tol": [
121                        0.0001, 
122                        0.00005
123                    ]
124                },
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 30/06/2026, 10:15:59*

**[REMOVED]**
```
(from line ~32)
        iterations=1,

```
**[ADDED]**
```
32            iterations=5,
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 30/06/2026, 10:15:54*

**[REMOVED]**
```
(from line ~55)
        removed_features_knn = ["heel_x_iqr", "heel_y_std"]

```
**[ADDED]**
```
55            #removed_features_knn = ["heel_x_iqr", "heel_y_std"]
```
**[REMOVED]**
```
(from line ~65)
            X = self.data_handler.remove_feature(X, removed_features_knn)

```
**[ADDED]**
```
65                X = self.data_handler.remove_feature(X, removed_features_mlp)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 30/06/2026, 10:15:41*

**[REMOVED]**
```
(from line ~54)
        #removed_features_mlp = ["big_toe_x_std"]

```
**[ADDED]**
```
54            removed_features_mlp = ["big_toe_x_std"]
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 30/06/2026, 10:15:38*

**[REMOVED]**
```
(from line ~54)
        #removed_features_mlp = ["big_toe_x_iqr"]

```
**[ADDED]**
```
54            #removed_features_mlp = ["big_toe_x_std"]
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 30/06/2026, 10:15:14*

**[REMOVED]**
```
(from line ~100)
        #removed_features_mlp = ["big_toe_x_iqr"]

```
**[ADDED]**
```
100           #removed_features_mlp = ["big_toe_x_std"]
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 30/06/2026, 10:13:16*

**[REMOVED]**
```
(from line ~35)
    #controller.run_data_analysis()
    controller.run()

```
**[ADDED]**
```
35        controller.run_data_analysis()
36        #controller.run()
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 30/06/2026, 10:13:09*

**[REMOVED]**
```
(from line ~32)
        iterations=10,

```
**[ADDED]**
```
32            iterations=1,
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 30/06/2026, 10:13:00*

**[REMOVED]**
```
(from line ~100)
        removed_features_mlp = ["big_toe_x_iqr"]

```
**[ADDED]**
```
100           #removed_features_mlp = ["big_toe_x_iqr"]
```
**[REMOVED]**
```
(from line ~103)
        X = self.data_handler.remove_feature(X, removed_features_mlp)

```
**[ADDED]**
```
103           #X = self.data_handler.remove_feature(X, removed_features_mlp)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 30/06/2026, 10:10:51*

**[REMOVED]**
```
(from line ~103)
        X = self.data_handler.remove_feature(X, removed_features_knn)

```
**[ADDED]**
```
103           X = self.data_handler.remove_feature(X, removed_features_mlp)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 30/06/2026, 10:10:47*

**[REMOVED]**
```
(from line ~97)
        #rs = 777 # random_state do melhor modelo encontrado para o MLP

```
**[ADDED]**
```
97            rs = 777 # random_state do melhor modelo encontrado para o MLP
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 30/06/2026, 10:10:43*

**[REMOVED]**
```
(from line ~98)
        rs = 647 # random_state do melhor modelo encontrado para o KNN
        removed_features_knn = ["heel_x_iqr", "heel_y_std"]

```
**[ADDED]**
```
98            #rs = 647 # random_state do melhor modelo encontrado para o KNN
99            #removed_features_knn = ["heel_x_iqr", "heel_y_std"]
100           removed_features_mlp = ["big_toe_x_iqr"]
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 30/06/2026, 10:10:20*

**[REMOVED]**
```
(from line ~13)
    #dict_params = {'clf': [MLPClassifier(random_state=31)], 'clf__activation': ['tanh'], 'clf__alpha': [0.0001], 'clf__early_stopping': [True], 'clf__hidden_layer_sizes': [(32,)], 'clf__learning_rate_init': [0.01], 'clf__max_iter': [1000], 'clf__validation_fraction': [0.1], 'reducao': ['passthrough'], 'scaler': [RobustScaler()]}

```
**[ADDED]**
```
13        dict_params = {'clf': [MLPClassifier(random_state=31)], 'clf__activation': ['tanh'], 'clf__alpha': [0.0001], 'clf__early_stopping': [True], 'clf__hidden_layer_sizes': [(32,)], 'clf__learning_rate_init': [0.01], 'clf__max_iter': [1000], 'clf__validation_fraction': [0.1], 'reducao': ['passthrough'], 'scaler': [RobustScaler()]}
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 30/06/2026, 10:06:02*

**[REMOVED]**
```
(from line ~66)
            {
                "clf": [Perceptron(random_state=42, class_weight="balanced")],
                "clf__eta0": [0.1, 0.01, 1.0],
                "clf__penalty": ["l2", "l1", "elasticnet"],
                "scaler": scalers,
                "reducao": ["passthrough"],
            },
             {
                 "scaler": scalers,
                 "reducao": reducoes,
                 "clf": [MLPClassifier(random_state=31)],
                 "clf__activation": [
                     "tanh",
                     "relu"
                 ],
                 "clf__hidden_layer_sizes": [
                     (24,),
                     (32,),
                    #(40,),
                     #(48,),
                     #(24, 12),
                     #(32, 16)
                 ],
                 "clf__alpha": [
                     #0.00005,
                     0.0001,
                     0.0002,
                     #0.0005,
                     #0.01
                 ],
                 "clf__learning_rate_init": [
                     #0.005,
                     #0.0075,
                     0.01,
                     0.015,
                     #0.1
                 ],
                 "clf__early_stopping": [True],
                 "clf__validation_fraction": [
                    # 0.08, 
                     0.10, 
                     0.12, 
                     #0.15
                 ],
                 "clf__max_iter": [
                     500,
                     1000,
                     #1500
                 ],
                 "clf__n_iter_no_change": [
                     10, 
                     15, 
                     #20
                 ],
                 "clf__tol": [
                     0.0001, 
                     0.00005
                 ]
             },

```
**[ADDED]**
```
66                # {
67                #     "clf": [Perceptron(random_state=42, class_weight="balanced")],
68                #     "clf__eta0": [0.1, 0.01, 1.0],
69                #     "clf__penalty": ["l2", "l1", "elasticnet"],
70                #     "scaler": scalers,
71                #     "reducao": ["passthrough"],
72                # },
73                #  {
74                #      "scaler": scalers,
75                #      "reducao": reducoes,
76                #      "clf": [MLPClassifier(random_state=31)],
77                #      "clf__activation": [
78                #          "tanh",
79                #          "relu"
80                #      ],
81                #      "clf__hidden_layer_sizes": [
82                #          (24,),
83                #          (32,),
84                #         #(40,),
85                #          #(48,),
86                #          #(24, 12),
87                #          #(32, 16)
88                #      ],
89                #      "clf__alpha": [
90                #          #0.00005,
91                #          0.0001,
92                #          0.0002,
93                #          #0.0005,
94                #          #0.01
95                #      ],
96                #      "clf__learning_rate_init": [
97                #          #0.005,
98                #          #0.0075,
99                #          0.01,
100               #          0.015,
101               #          #0.1
102               #      ],
103               #      "clf__early_stopping": [True],
104               #      "clf__validation_fraction": [
105               #         # 0.08, 
106               #          0.10, 
107               #          0.12, 
108               #          #0.15
109               #      ],
110               #      "clf__max_iter": [
111               #          500,
112               #          1000,
113               #          #1500
114               #      ],
115               #      "clf__n_iter_no_change": [
116               #          10, 
117               #          15, 
118               #          #20
119               #      ],
120               #      "clf__tol": [
121               #          0.0001, 
122               #          0.00005
123               #      ]
124               #  },
```
**[ADDED]**
```
165               {
166                    "clf": [KNeighborsClassifier()],
167                    "clf__n_neighbors": [3, 5, 7, 9, 11, 13, 15, 17, 19],
168                    "clf__weights": ["uniform", "distance"],
169                    "clf__metric": ["euclidean", "manhattan"],
170                    "scaler": scalers,
171                    "reducao": reducoes,
172               },
```
**[REMOVED]**
```
(from line ~174)
            #     "clf": [KNeighborsClassifier()],
            #     "clf__n_neighbors": [3, 5, 7, 9, 11, 13, 15, 17, 19],
            #     "clf__weights": ["uniform", "distance"],
            #     "clf__metric": ["euclidean", "manhattan"],
            #     "scaler": scalers,
            #     "reducao": reducoes,
            #},
            #{

```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 30/06/2026, 10:05:33*

**[REMOVED]**
```
(from line ~38)
            RobustScaler(quantile_range=(20, 80)),
            RobustScaler(quantile_range=(10, 90)),
            RobustScaler(quantile_range=(30, 70)),

```
**[ADDED]**
```
38                #RobustScaler(quantile_range=(20, 80)),
39                #RobustScaler(quantile_range=(10, 90)),
40                #RobustScaler(quantile_range=(30, 70)),
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 30/06/2026, 10:05:27*

**[REMOVED]**
```
(from line ~27)
            #StandardScaler(),

```
**[ADDED]**
```
27                StandardScaler(),
```
**[REMOVED]**
```
(from line ~29)
            #MinMaxScaler(),
            #MaxAbsScaler(),
            #QuantileTransformer(output_distribution="uniform", random_state=42),
            #QuantileTransformer(output_distribution="normal", random_state=42),
            #PowerTransformer(method="yeo-johnson"),
            #Normalizer(norm="l2"),

```
**[ADDED]**
```
29                MinMaxScaler(),
30                MaxAbsScaler(),
31                QuantileTransformer(output_distribution="uniform", random_state=42),
32                QuantileTransformer(output_distribution="normal", random_state=42),
33                PowerTransformer(method="yeo-johnson"),
34                Normalizer(norm="l2"),
```
**[REMOVED]**
```
(from line ~38)
            #RobustScaler(quantile_range=(20, 80)),
            #RobustScaler(quantile_range=(10, 90)),
            #RobustScaler(quantile_range=(30, 70)),

```
**[ADDED]**
```
38                RobustScaler(quantile_range=(20, 80)),
39                RobustScaler(quantile_range=(10, 90)),
40                RobustScaler(quantile_range=(30, 70)),
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 30/06/2026, 10:03:26*

**[REMOVED]**
```
(from line ~53)
        #random_states = [random.randint(1, 1000) for _ in range(self.iterations)]

```
**[ADDED]**
```
53            random_states = [random.randint(1, 1000) for _ in range(self.iterations)]
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 30/06/2026, 10:03:25*

**[REMOVED]**
```
(from line ~57)
        random_states = [647] # Random State para o melhor KNN

```
**[ADDED]**
```
57            #random_states = [647] # Random State para o melhor KNN
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 30/06/2026, 10:03:11*

**[REMOVED]**
```
(from line ~16)
    dict_params = {'clf': [KNeighborsClassifier()], 'clf__metric': ['euclidean'], 'clf__n_neighbors': [5], 'clf__weights': ['uniform'], 'reducao': ['passthrough'], 'scaler': [PowerTransformer()]}

```
**[ADDED]**
```
16        #dict_params = {'clf': [KNeighborsClassifier()], 'clf__metric': ['euclidean'], 'clf__n_neighbors': [5], 'clf__weights': ['uniform'], 'reducao': ['passthrough'], 'scaler': [PowerTransformer()]}
```
**[REMOVED]**
```
(from line ~18)
    #dict_params = None

```
**[ADDED]**
```
18        dict_params = None
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 30/06/2026, 10:02:51*

**[REMOVED]**
```
(from line ~32)
        iterations=1,

```
**[ADDED]**
```
32            iterations=10,
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 30/06/2026, 10:01:09*

**[REMOVED]**
```
(from line ~55)
        removed_features_knn = ["heel_x_iqr"]

```
**[ADDED]**
```
55            removed_features_knn = ["heel_x_iqr", "heel_y_std"]
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 30/06/2026, 10:00:48*

**[REMOVED]**
```
(from line ~35)
    controller.run_data_analysis()
    #controller.run()
    
```
**[ADDED]**
```
35        #controller.run_data_analysis()
36        controller.run()
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 30/06/2026, 10:00:25*

**[REMOVED]**
```
(from line ~65)
            X = self.data_handler.remove_feature(X, removed_features_mlp)

```
**[ADDED]**
```
65                X = self.data_handler.remove_feature(X, removed_features_knn)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 30/06/2026, 10:00:19*

**[REMOVED]**
```
(from line ~65)
           #X = self.data_handler.remove_feature(X, removed_features_mlp)

```
**[ADDED]**
```
65                X = self.data_handler.remove_feature(X, removed_features_mlp)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 30/06/2026, 10:00:15*

**[REMOVED]**
```
(from line ~55)
        #removed_features_knn = ["heel_x_iqr"]

```
**[ADDED]**
```
55            removed_features_knn = ["heel_x_iqr"]
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 30/06/2026, 10:00:03*

**[REMOVED]**
```
(from line ~99)
        removed_features_knn = ["heel_x_iqr"]

```
**[ADDED]**
```
99            removed_features_knn = ["heel_x_iqr", "heel_y_std"]
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 30/06/2026, 09:54:21*

**[REMOVED]**
```
(from line ~13)
from sklearn.preprocessing import RobustScaler

```
**[ADDED]**
```
13    from sklearn.preprocessing import RobustScaler, PowerTransformer
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 30/06/2026, 09:54:10*

**[REMOVED]**
```
(from line ~126)
        X_val_scaled = RobustScaler().fit_transform(X_val)

```
**[ADDED]**
```
126           X_val_scaled = PowerTransformer().fit_transform(X_val)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 30/06/2026, 09:53:45*

**[ADDED]**
```
37        
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 30/06/2026, 09:53:43*

**[REMOVED]**
```
(from line ~37)


```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 30/06/2026, 09:53:41*

**[REMOVED]**
```
(from line ~35)
    #controller.run_data_analysis()
    controller.run()

```
**[ADDED]**
```
35        controller.run_data_analysis()
36        #controller.run()
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 30/06/2026, 09:53:15*

**[REMOVED]**
```
(from line ~35)
    controller.run_data_analysis()
    #controller.run()

```
**[ADDED]**
```
35        #controller.run_data_analysis()
36        controller.run()
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 30/06/2026, 09:53:06*

**[REMOVED]**
```
(from line ~53)
        random_states = [random.randint(1, 1000) for _ in range(self.iterations)]

```
**[ADDED]**
```
53            #random_states = [random.randint(1, 1000) for _ in range(self.iterations)]
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 30/06/2026, 09:53:05*

**[REMOVED]**
```
(from line ~56)
        random_states = [777]    # Random State para o melhor MLP 
        #random_states = [647] # Random State para o melhor KNN

```
**[ADDED]**
```
56            #random_states = [777]    # Random State para o melhor MLP 
57            random_states = [647] # Random State para o melhor KNN
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 30/06/2026, 09:53:02*

**[REMOVED]**
```
(from line ~57)
        #random_states = [732] # Random State para o melhor KNN

```
**[ADDED]**
```
57            #random_states = [647] # Random State para o melhor KNN
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 30/06/2026, 09:51:04*

**[REMOVED]**
```
(from line ~35)
    #controller.run_data_analysis()
    controller.run()

```
**[ADDED]**
```
35        controller.run_data_analysis()
36        #controller.run()
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 30/06/2026, 09:50:37*

**[REMOVED]**
```
(from line ~104)


```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 30/06/2026, 09:50:19*

**[REMOVED]**
```
(from line ~99)
        

```
**[ADDED]**
```
99            removed_features_knn = ["heel_x_iqr"]
100   
```
**[REMOVED]**
```
(from line ~102)
      

```
**[ADDED]**
```
102           X = self.data_handler.remove_feature(X, removed_features_knn)
103   
104   
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 30/06/2026, 09:47:14*

**[REMOVED]**
```
(from line ~98)
        rs = 732 # random_state do melhor modelo encontrado para o KNN

```
**[ADDED]**
```
98            rs = 647 # random_state do melhor modelo encontrado para o KNN
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 30/06/2026, 09:46:52*

**[REMOVED]**
```
(from line ~97)
        rs = 777 # random_state do melhor modelo encontrado para o MLP
        #rs = 732 # random_state do melhor modelo encontrado para o KNN

```
**[ADDED]**
```
97            #rs = 777 # random_state do melhor modelo encontrado para o MLP
98            rs = 732 # random_state do melhor modelo encontrado para o KNN
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 30/06/2026, 09:46:20*

**[REMOVED]**
```
(from line ~7)
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, Normalizer, QuantileTransformer

```
**[ADDED]**
```
7     from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, Normalizer, QuantileTransformer, PowerTransformer
```
**[REMOVED]**
```
(from line ~16)
    dict_params = {'clf': [KNeighborsClassifier()], 'clf__metric': ['euclidean'], 'clf__n_neighbors': [5], 'clf__weights': ['uniform'], 'reducao': ['passthrough'], 'scaler': [Normalizer()]}

```
**[ADDED]**
```
16        dict_params = {'clf': [KNeighborsClassifier()], 'clf__metric': ['euclidean'], 'clf__n_neighbors': [5], 'clf__weights': ['uniform'], 'reducao': ['passthrough'], 'scaler': [PowerTransformer()]}
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 30/06/2026, 09:46:00*

**[REMOVED]**
```
(from line ~16)
    dict_params = {'clf': [KNeighborsClassifier()], 'clf__metric': ['manhattan'], 'clf__n_neighbors': [5], 'clf__weights': ['uniform'], 'reducao': ['passthrough'], 'scaler': [Normalizer()]}

```
**[ADDED]**
```
16        dict_params = {'clf': [KNeighborsClassifier()], 'clf__metric': ['euclidean'], 'clf__n_neighbors': [5], 'clf__weights': ['uniform'], 'reducao': ['passthrough'], 'scaler': [Normalizer()]}
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 30/06/2026, 09:45:49*

**[REMOVED]**
```
(from line ~16)
    dict_params = {'clf': [KNeighborsClassifier()], 'clf__metric': ['manhattan'], 'clf__n_neighbors': [9], 'clf__weights': ['uniform'], 'reducao': ['passthrough'], 'scaler': [Normalizer()]}

```
**[ADDED]**
```
16        dict_params = {'clf': [KNeighborsClassifier()], 'clf__metric': ['manhattan'], 'clf__n_neighbors': [5], 'clf__weights': ['uniform'], 'reducao': ['passthrough'], 'scaler': [Normalizer()]}
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 30/06/2026, 09:38:27*

**[REMOVED]**
```
(from line ~16)
    dict_params = {'clf': [KNeighborsClassifier()], 'clf__metric': ['manhattan'], 'clf__n_neighbors': [5], 'clf__weights': ['uniform'], 'reducao': ['passthrough'], 'scaler': [Normalizer()]}

```
**[ADDED]**
```
16        dict_params = {'clf': [KNeighborsClassifier()], 'clf__metric': ['manhattan'], 'clf__n_neighbors': [9], 'clf__weights': ['uniform'], 'reducao': ['passthrough'], 'scaler': [Normalizer()]}
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 30/06/2026, 09:38:19*

**[REMOVED]**
```
(from line ~16)
    dict_params = {'clf': [KNeighborsClassifier()], 'clf__metric': ['manhattan'], 'clf__n_neighbors': [9], 'clf__weights': ['uniform'], 'reducao': ['passthrough'], 'scaler': [Normalizer()]}

```
**[ADDED]**
```
16        dict_params = {'clf': [KNeighborsClassifier()], 'clf__metric': ['manhattan'], 'clf__n_neighbors': [5], 'clf__weights': ['uniform'], 'reducao': ['passthrough'], 'scaler': [Normalizer()]}
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 30/06/2026, 09:37:40*

**[REMOVED]**
```
(from line ~13)
    dict_params = {'clf': [MLPClassifier(random_state=31)], 'clf__activation': ['tanh'], 'clf__alpha': [0.0001], 'clf__early_stopping': [True], 'clf__hidden_layer_sizes': [(32,)], 'clf__learning_rate_init': [0.01], 'clf__max_iter': [1000], 'clf__validation_fraction': [0.1], 'reducao': ['passthrough'], 'scaler': [RobustScaler()]}

```
**[ADDED]**
```
13        #dict_params = {'clf': [MLPClassifier(random_state=31)], 'clf__activation': ['tanh'], 'clf__alpha': [0.0001], 'clf__early_stopping': [True], 'clf__hidden_layer_sizes': [(32,)], 'clf__learning_rate_init': [0.01], 'clf__max_iter': [1000], 'clf__validation_fraction': [0.1], 'reducao': ['passthrough'], 'scaler': [RobustScaler()]}
```
**[REMOVED]**
```
(from line ~16)
    #dict_params = {'clf': [KNeighborsClassifier()], 'clf__metric': ['manhattan'], 'clf__n_neighbors': [9], 'clf__weights': ['uniform'], 'reducao': ['passthrough'], 'scaler': [Normalizer()]}

```
**[ADDED]**
```
16        dict_params = {'clf': [KNeighborsClassifier()], 'clf__metric': ['manhattan'], 'clf__n_neighbors': [9], 'clf__weights': ['uniform'], 'reducao': ['passthrough'], 'scaler': [Normalizer()]}
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 23/06/2026, 13:03:51*

**[REMOVED]**
```
(from line ~18)
    dict_params = None

```
**[ADDED]**
```
18        #dict_params = None
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 23/06/2026, 13:02:14*

**[REMOVED]**
```
(from line ~65)
            X = self.data_handler.remove_feature(X, removed_features_mlp)

```
**[ADDED]**
```
65               #X = self.data_handler.remove_feature(X, removed_features_mlp)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 23/06/2026, 13:02:10*

**[REMOVED]**
```
(from line ~54)
        removed_features_mlp = ["big_toe_x_iqr"]

```
**[ADDED]**
```
54            #removed_features_mlp = ["big_toe_x_iqr"]
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 23/06/2026, 13:01:07*

**[REMOVED]**
```
(from line ~32)
        iterations=10,

```
**[ADDED]**
```
32            iterations=1,
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 23/06/2026, 13:01:01*

**[REMOVED]**
```
(from line ~56)
        #random_states = [777]    # Random State para o melhor MLP 

```
**[ADDED]**
```
56            random_states = [777]    # Random State para o melhor MLP 
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 23/06/2026, 13:00:37*

**[REMOVED]**
```
(from line ~13)
    #dict_params = {'clf': [MLPClassifier(random_state=31)], 'clf__activation': ['tanh'], 'clf__alpha': [0.0001], 'clf__early_stopping': [True], 'clf__hidden_layer_sizes': [(32,)], 'clf__learning_rate_init': [0.01], 'clf__max_iter': [1000], 'clf__validation_fraction': [0.1], 'reducao': ['passthrough'], 'scaler': [RobustScaler()]}

```
**[ADDED]**
```
13        dict_params = {'clf': [MLPClassifier(random_state=31)], 'clf__activation': ['tanh'], 'clf__alpha': [0.0001], 'clf__early_stopping': [True], 'clf__hidden_layer_sizes': [(32,)], 'clf__learning_rate_init': [0.01], 'clf__max_iter': [1000], 'clf__validation_fraction': [0.1], 'reducao': ['passthrough'], 'scaler': [RobustScaler()]}
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/excel_geter.py
*Saved at: 23/06/2026, 08:26:41*

**[REMOVED]**
```
(from line ~24)
    

```
**[ADDED]**
```
24    
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/views/advanced_visualizations.py
*Saved at: 22/06/2026, 22:33:41*

**[REMOVED]**
```
(from line ~249)
        acc_treino = resultados.get('accuracy_treino', 0)

```
**[ADDED]**
```
249           acc_treino = resultados.get('accuracy_treino', 0)       
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/views/advanced_visualizations.py
*Saved at: 22/06/2026, 22:31:48*

**[REMOVED]**
```
(from line ~233)
        TrainingDiagnostic._imprimir_diagnostico(resultados, diagnostico)

```
**[ADDED]**
```
233           TrainingDiagnostic._imprimir_diagnostico(resultados, diagnostico)           
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 22/06/2026, 22:18:27*

**[REMOVED]**
```
(from line ~32)
        iterations=5,

```
**[ADDED]**
```
32            iterations=10,
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 22/06/2026, 22:17:19*

**[REMOVED]**
```
(from line ~84)
                     (40,),

```
**[ADDED]**
```
84                        #(40,),
```
**[REMOVED]**
```
(from line ~90)
                     0.00005,

```
**[ADDED]**
```
90                         #0.00005,
```
**[REMOVED]**
```
(from line ~98)
                     0.0075,

```
**[ADDED]**
```
98                         #0.0075,
```
**[REMOVED]**
```
(from line ~105)
                     0.08, 

```
**[ADDED]**
```
105                       # 0.08, 
```
**[REMOVED]**
```
(from line ~113)
                     1500

```
**[ADDED]**
```
113                        #1500
```
**[REMOVED]**
```
(from line ~118)
                     20

```
**[ADDED]**
```
118                        #20
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 22/06/2026, 22:16:10*

**[REMOVED]**
```
(from line ~27)
            StandardScaler(),
            #RobustScaler(),

```
**[ADDED]**
```
27                #StandardScaler(),
28                RobustScaler(),
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 22/06/2026, 22:16:07*

**[REMOVED]**
```
(from line ~28)
            RobustScaler(),
            MinMaxScaler(),
            MaxAbsScaler(),
            QuantileTransformer(output_distribution="uniform", random_state=42),

```
**[ADDED]**
```
28                #RobustScaler(),
29                #MinMaxScaler(),
30                #MaxAbsScaler(),
31                #QuantileTransformer(output_distribution="uniform", random_state=42),
```
**[REMOVED]**
```
(from line ~33)
            PowerTransformer(method="yeo-johnson"),
            Normalizer(norm="l2"),

```
**[ADDED]**
```
33                #PowerTransformer(method="yeo-johnson"),
34                #Normalizer(norm="l2"),
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 22/06/2026, 22:15:43*

**[REMOVED]**
```
(from line ~53)
        #random_states = [random.randint(1, 1000) for _ in range(self.iterations)]

```
**[ADDED]**
```
53            random_states = [random.randint(1, 1000) for _ in range(self.iterations)]
```
**[REMOVED]**
```
(from line ~56)
        random_states = [777]    # Random State para o melhor MLP 

```
**[ADDED]**
```
56            #random_states = [777]    # Random State para o melhor MLP 
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 22/06/2026, 22:15:35*

**[REMOVED]**
```
(from line ~32)
        iterations=1,

```
**[ADDED]**
```
32            iterations=5,
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 22/06/2026, 22:15:23*

**[REMOVED]**
```
(from line ~13)
    dict_params = {'clf': [MLPClassifier(random_state=31)], 'clf__activation': ['tanh'], 'clf__alpha': [0.0001], 'clf__early_stopping': [True], 'clf__hidden_layer_sizes': [(32,)], 'clf__learning_rate_init': [0.01], 'clf__max_iter': [1000], 'clf__validation_fraction': [0.1], 'reducao': ['passthrough'], 'scaler': [RobustScaler()]}

```
**[ADDED]**
```
13        #dict_params = {'clf': [MLPClassifier(random_state=31)], 'clf__activation': ['tanh'], 'clf__alpha': [0.0001], 'clf__early_stopping': [True], 'clf__hidden_layer_sizes': [(32,)], 'clf__learning_rate_init': [0.01], 'clf__max_iter': [1000], 'clf__validation_fraction': [0.1], 'reducao': ['passthrough'], 'scaler': [RobustScaler()]}
```
**[REMOVED]**
```
(from line ~18)
    #dict_params = None

```
**[ADDED]**
```
18        dict_params = None
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 22/06/2026, 22:14:21*

**[REMOVED]**
```
(from line ~35)
    controller.run_data_analysis()
    #controller.run()

```
**[ADDED]**
```
35        #controller.run_data_analysis()
36        controller.run()
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 22/06/2026, 22:13:14*

**[ADDED]**
```
66                {
67                    "clf": [Perceptron(random_state=42, class_weight="balanced")],
68                    "clf__eta0": [0.1, 0.01, 1.0],
69                    "clf__penalty": ["l2", "l1", "elasticnet"],
70                    "scaler": scalers,
71                    "reducao": ["passthrough"],
72                },
73                 {
74                     "scaler": scalers,
75                     "reducao": reducoes,
76                     "clf": [MLPClassifier(random_state=31)],
77                     "clf__activation": [
78                         "tanh",
79                         "relu"
80                     ],
81                     "clf__hidden_layer_sizes": [
82                         (24,),
83                         (32,),
84                         (40,),
85                         #(48,),
86                         #(24, 12),
87                         #(32, 16)
88                     ],
89                     "clf__alpha": [
90                         0.00005,
91                         0.0001,
92                         0.0002,
93                         #0.0005,
94                         #0.01
95                     ],
96                     "clf__learning_rate_init": [
97                         #0.005,
98                         0.0075,
99                         0.01,
100                        0.015,
101                        #0.1
102                    ],
103                    "clf__early_stopping": [True],
104                    "clf__validation_fraction": [
105                        0.08, 
106                        0.10, 
107                        0.12, 
108                        #0.15
109                    ],
110                    "clf__max_iter": [
111                        500,
112                        1000,
113                        1500
114                    ],
115                    "clf__n_iter_no_change": [
116                        10, 
117                        15, 
118                        20
119                    ],
120                    "clf__tol": [
121                        0.0001, 
122                        0.00005
123                    ]
124                },
```
**[REMOVED]**
```
(from line ~126)
            #    "clf": [Perceptron(random_state=42, class_weight="balanced")],
            #    "clf__eta0": [0.1, 0.01, 1.0],
            #    "clf__penalty": ["l2", "l1", "elasticnet"],
            #    "scaler": scalers,
            #    "reducao": ["passthrough"],
            #},
            # {
            #     "scaler": scalers,
            #     "reducao": reducoes,
            #     "clf": [MLPClassifier(random_state=31)],
            #     "clf__activation": [
            #         "tanh",
            #         "relu"
            #     ],


            #     "clf__hidden_layer_sizes": [
            #         (24,),
            #         (32,),
            #         (40,),
            #         #(48,),
            #         #(24, 12),
            #         #(32, 16)
            #     ],

            #     "clf__alpha": [
            #         0.00005,
            #         0.0001,
            #         0.0002,
            #         #0.0005,
            #         #0.01
            #     ],

            #     "clf__learning_rate_init": [
            #         #0.005,
            #         0.0075,
            #         0.01,
            #         0.015,
            #         #0.1
            #     ],

            #     "clf__early_stopping": [True],
            #     "clf__validation_fraction": [
            #         0.08, 
            #         0.10, 
            #         0.12, 
            #         #0.15
            #     ],

            #     "clf__max_iter": [
            #         500,
            #         1000,
            #         1500
            #     ],

            #     "clf__n_iter_no_change": [
            #         10, 
            #         15, 
            #         20
            #     ],

            #     "clf__tol": [
            #         0.0001, 
            #         0.00005
            #     ]
            # },

            #{

```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 22/06/2026, 22:12:38*

**[REMOVED]**
```
(from line ~174)
            {
                 "clf": [KNeighborsClassifier()],
                 "clf__n_neighbors": [3, 5, 7, 9, 11, 13, 15, 17, 19],
                 "clf__weights": ["uniform", "distance"],
                 "clf__metric": ["euclidean", "manhattan"],
                 "scaler": scalers,
                 "reducao": reducoes,
            },

```
**[ADDED]**
```
175               #     "clf": [KNeighborsClassifier()],
176               #     "clf__n_neighbors": [3, 5, 7, 9, 11, 13, 15, 17, 19],
177               #     "clf__weights": ["uniform", "distance"],
178               #     "clf__metric": ["euclidean", "manhattan"],
179               #     "scaler": scalers,
180               #     "reducao": reducoes,
181               #},
182               #{
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 22/06/2026, 22:09:23*

**[REMOVED]**
```
(from line ~35)
    #controller.run_data_analysis()
    controller.run()

```
**[ADDED]**
```
35        controller.run_data_analysis()
36        #controller.run()
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 22/06/2026, 22:08:17*

**[REMOVED]**
```
(from line ~18)
    dict_params = None

```
**[ADDED]**
```
18        #dict_params = None
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 22/06/2026, 22:08:14*

**[REMOVED]**
```
(from line ~13)
    #dict_params = {'clf': [MLPClassifier(random_state=31)], 'clf__activation': ['tanh'], 'clf__alpha': [0.0001], 'clf__early_stopping': [True], 'clf__hidden_layer_sizes': [(32,)], 'clf__learning_rate_init': [0.01], 'clf__max_iter': [1000], 'clf__validation_fraction': [0.1], 'reducao': ['passthrough'], 'scaler': [RobustScaler()]}

```
**[ADDED]**
```
13        dict_params = {'clf': [MLPClassifier(random_state=31)], 'clf__activation': ['tanh'], 'clf__alpha': [0.0001], 'clf__early_stopping': [True], 'clf__hidden_layer_sizes': [(32,)], 'clf__learning_rate_init': [0.01], 'clf__max_iter': [1000], 'clf__validation_fraction': [0.1], 'reducao': ['passthrough'], 'scaler': [RobustScaler()]}
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 22/06/2026, 22:08:07*

**[REMOVED]**
```
(from line ~97)
        #rs = 777 # random_state do melhor modelo encontrado para o MLP
        rs = 732 # random_state do melhor modelo encontrado para o KNN

```
**[ADDED]**
```
97            rs = 777 # random_state do melhor modelo encontrado para o MLP
98            #rs = 732 # random_state do melhor modelo encontrado para o KNN
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 22/06/2026, 22:07:44*

**[REMOVED]**
```
(from line ~32)
        iterations=10,

```
**[ADDED]**
```
32            iterations=1,
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 22/06/2026, 22:07:39*

**[REMOVED]**
```
(from line ~53)
        random_states = [random.randint(1, 1000) for _ in range(self.iterations)]

```
**[ADDED]**
```
53            #random_states = [random.randint(1, 1000) for _ in range(self.iterations)]
```
**[REMOVED]**
```
(from line ~56)
        #random_states = [777]    # Random State para o melhor MLP 

```
**[ADDED]**
```
56            random_states = [777]    # Random State para o melhor MLP 
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 22/06/2026, 22:07:25*

**[REMOVED]**
```
(from line ~65)
            #X = self.data_handler.remove_feature(X, removed_features_knn)

```
**[ADDED]**
```
65                X = self.data_handler.remove_feature(X, removed_features_mlp)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 22/06/2026, 22:07:18*

**[REMOVED]**
```
(from line ~54)
        #removed_features_mlp = ["big_toe_x_iqr"]

```
**[ADDED]**
```
54            removed_features_mlp = ["big_toe_x_iqr"]
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 22/06/2026, 22:05:18*

**[REMOVED]**
```
(from line ~55)
        removed_features_knn = ["heel_x_iqr"]

```
**[ADDED]**
```
55            #removed_features_knn = ["heel_x_iqr"]
```
**[REMOVED]**
```
(from line ~65)
            X = self.data_handler.remove_feature(X, removed_features_knn)

```
**[ADDED]**
```
65                #X = self.data_handler.remove_feature(X, removed_features_knn)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 22/06/2026, 21:44:11*

**[REMOVED]**
```
(from line ~55)
        #removed_features_knn = ["heel_x_iqr"]

```
**[ADDED]**
```
55            removed_features_knn = ["heel_x_iqr"]
```
**[REMOVED]**
```
(from line ~65)
            #X = self.data_handler.remove_feature(X, removed_features_knn)

```
**[ADDED]**
```
65                X = self.data_handler.remove_feature(X, removed_features_knn)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 22/06/2026, 21:16:40*

**[REMOVED]**
```
(from line ~174)
            # {
            #     "clf": [KNeighborsClassifier()],
            #     "clf__n_neighbors": [3, 5, 7, 9, 11, 13, 15, 17, 19],
            #     "clf__weights": ["uniform", "distance"],
            #     "clf__metric": ["euclidean", "manhattan"],
            #     "scaler": scalers,
            #     "reducao": reducoes,
            # },

```
**[ADDED]**
```
174               {
175                    "clf": [KNeighborsClassifier()],
176                    "clf__n_neighbors": [3, 5, 7, 9, 11, 13, 15, 17, 19],
177                    "clf__weights": ["uniform", "distance"],
178                    "clf__metric": ["euclidean", "manhattan"],
179                    "scaler": scalers,
180                    "reducao": reducoes,
181               },
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 22/06/2026, 21:16:27*

**[REMOVED]**
```
(from line ~134)
            {
                "clf": [SVC(random_state=42, class_weight="balanced")],
                "clf__C": [0.1, 1, 5, 10, 50, 100],
                "clf__kernel": ["rbf", "poly"],
                "clf__gamma": ["scale", "auto"],
                "scaler": scalers,
                "reducao": reducoes,
            },

```
**[ADDED]**
```
135               #    "clf": [SVC(random_state=42, class_weight="balanced")],
136               #    "clf__C": [0.1, 1, 5, 10, 50, 100],
137               #    "clf__kernel": ["rbf", "poly"],
138               #    "clf__gamma": ["scale", "auto"],
139               #    "scaler": scalers,
140               #    "reducao": reducoes,
141               #},
142               #{
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 22/06/2026, 18:01:30*

**[ADDED]**
```
134               {
135                   "clf": [SVC(random_state=42, class_weight="balanced")],
136                   "clf__C": [0.1, 1, 5, 10, 50, 100],
137                   "clf__kernel": ["rbf", "poly"],
138                   "clf__gamma": ["scale", "auto"],
139                   "scaler": scalers,
140                   "reducao": reducoes,
141               },
```
**[REMOVED]**
```
(from line ~143)
            #    "clf": [SVC(random_state=42, class_weight="balanced")],
            #    "clf__C": [0.1, 1, 5, 10, 50, 100],
            #    "clf__kernel": ["rbf", "poly"],
            #    "clf__gamma": ["scale", "auto"],
            #    "scaler": scalers,
            #    "reducao": reducoes,
            #},
            #{

```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 22/06/2026, 18:01:08*

**[REMOVED]**
```
(from line ~174)
            {
                "clf": [KNeighborsClassifier()],
                "clf__n_neighbors": [3, 5, 7, 9, 11, 13, 15, 17, 19],
                "clf__weights": ["uniform", "distance"],
                "clf__metric": ["euclidean", "manhattan"],
                "scaler": scalers,
                "reducao": reducoes,
            },

```
**[ADDED]**
```
174               # {
175               #     "clf": [KNeighborsClassifier()],
176               #     "clf__n_neighbors": [3, 5, 7, 9, 11, 13, 15, 17, 19],
177               #     "clf__weights": ["uniform", "distance"],
178               #     "clf__metric": ["euclidean", "manhattan"],
179               #     "scaler": scalers,
180               #     "reducao": reducoes,
181               # },
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 22/06/2026, 18:00:21*

**[REMOVED]**
```
(from line ~36)
            #None,

```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 22/06/2026, 18:00:05*

**[REMOVED]**
```
(from line ~33)
            #PowerTransformer(method="yeo-johnson"),

```
**[ADDED]**
```
33                PowerTransformer(method="yeo-johnson"),
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 22/06/2026, 17:59:49*

**[REMOVED]**
```
(from line ~32)
        iterations=1,

```
**[ADDED]**
```
32            iterations=10,
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 22/06/2026, 17:59:39*

**[REMOVED]**
```
(from line ~65)
            X = self.data_handler.remove_feature(X, removed_features_knn)

```
**[ADDED]**
```
65                #X = self.data_handler.remove_feature(X, removed_features_knn)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 22/06/2026, 17:59:32*

**[REMOVED]**
```
(from line ~55)
        removed_features_knn = ["heel_x_iqr"]

```
**[ADDED]**
```
55            #removed_features_knn = ["heel_x_iqr"]
```
**[REMOVED]**
```
(from line ~57)
        random_states = [732] # Random State para o melhor KNN

```
**[ADDED]**
```
57            #random_states = [732] # Random State para o melhor KNN
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 22/06/2026, 17:56:20*

**[REMOVED]**
```
(from line ~35)
    controller.run_data_analysis()
    #controller.run()

```
**[ADDED]**
```
35        #controller.run_data_analysis()
36        controller.run()
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 22/06/2026, 17:56:14*

**[REMOVED]**
```
(from line ~32)
        iterations=10,

```
**[ADDED]**
```
32            iterations=1,
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 22/06/2026, 17:56:10*

**[REMOVED]**
```
(from line ~57)
        #random_states = [732] # Random State para o melhor KNN

```
**[ADDED]**
```
57            random_states = [732] # Random State para o melhor KNN
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 22/06/2026, 17:53:54*

**[REMOVED]**
```
(from line ~65)
            #X = self.data_handler.remove_feature(X, removed_features_mlp)

```
**[ADDED]**
```
65                X = self.data_handler.remove_feature(X, removed_features_knn)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 22/06/2026, 17:53:39*

**[REMOVED]**
```
(from line ~55)
        #removed_features_knn = 

```
**[ADDED]**
```
55            removed_features_knn = ["heel_x_iqr"]
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 22/06/2026, 17:46:04*

**[ADDED]**
```
57            #random_states = [732] # Random State para o melhor KNN
```
**[REMOVED]**
```
(from line ~97)
        rs = 777 # random_state do melhor modelo encontrado

```
**[ADDED]**
```
97            #rs = 777 # random_state do melhor modelo encontrado para o MLP
98            rs = 732 # random_state do melhor modelo encontrado para o KNN
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 22/06/2026, 17:45:06*

**[REMOVED]**
```
(from line ~18)
    dict_params = None

```
**[ADDED]**
```
18        #dict_params = None
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 22/06/2026, 17:44:59*

**[REMOVED]**
```
(from line ~35)
    #controller.run_data_analysis()
    controller.run()

```
**[ADDED]**
```
35        controller.run_data_analysis()
36        #controller.run()
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 22/06/2026, 17:44:03*

**[REMOVED]**
```
(from line ~6)
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler

```
**[ADDED]**
```
6     from sklearn.neighbors import KNeighborsClassifier
7     from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, Normalizer, QuantileTransformer
```
**[ADDED]**
```
12        # Parametros específicos para o MLP
```
**[ADDED]**
```
14        
15        #Parametros específicos para o KNN
16        dict_params = {'clf': [KNeighborsClassifier()], 'clf__metric': ['manhattan'], 'clf__n_neighbors': [9], 'clf__weights': ['uniform'], 'reducao': ['passthrough'], 'scaler': [Normalizer()]}
17    
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 22/06/2026, 17:41:07*

**[ADDED]**
```
55            #removed_features_knn = 
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 22/06/2026, 17:40:47*

**[REMOVED]**
```
(from line ~55)
        #random_states = [777]  

```
**[ADDED]**
```
55            #random_states = [777]    # Random State para o melhor MLP 
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 22/06/2026, 17:33:25*

**[REMOVED]**
```
(from line ~26)
        iterations=5,

```
**[ADDED]**
```
26            iterations=10,
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 22/06/2026, 17:31:56*

**[REMOVED]**
```
(from line ~54)
        removed_features_mlp = ["big_toe_x_iqr"]

```
**[ADDED]**
```
54            #removed_features_mlp = ["big_toe_x_iqr"]
```
**[REMOVED]**
```
(from line ~63)
            X = self.data_handler.remove_feature(X, removed_features_mlp)

```
**[ADDED]**
```
63                #X = self.data_handler.remove_feature(X, removed_features_mlp)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 22/06/2026, 17:31:34*

**[REMOVED]**
```
(from line ~36)
            None,

```
**[ADDED]**
```
36                #None,
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 22/06/2026, 17:31:32*

**[REMOVED]**
```
(from line ~27)
            #StandardScaler(),
            #RobustScaler(),
            #MinMaxScaler(),
            #MaxAbsScaler(),
            #QuantileTransformer(output_distribution="uniform", random_state=42),

```
**[ADDED]**
```
27                StandardScaler(),
28                RobustScaler(),
29                MinMaxScaler(),
30                MaxAbsScaler(),
31                QuantileTransformer(output_distribution="uniform", random_state=42),
```
**[REMOVED]**
```
(from line ~34)
            #Normalizer(norm="l2"),

```
**[ADDED]**
```
34                Normalizer(norm="l2"),
```
**[REMOVED]**
```
(from line ~38)
            RobustScaler(),

```
**[ADDED]**
```
38                #RobustScaler(),
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 22/06/2026, 17:30:57*

**[REMOVED]**
```
(from line ~74)
            {
                "scaler": scalers,
                "reducao": reducoes,
                "clf": [MLPClassifier(random_state=31)],
                "clf__activation": [
                    "tanh",
                    "relu"
                ],

```
**[ADDED]**
```
74                # {
75                #     "scaler": scalers,
76                #     "reducao": reducoes,
77                #     "clf": [MLPClassifier(random_state=31)],
78                #     "clf__activation": [
79                #         "tanh",
80                #         "relu"
81                #     ],
```
**[REMOVED]**
```
(from line ~84)
                "clf__hidden_layer_sizes": [
                    (24,),
                    (32,),
                    (40,),
                    #(48,),
                    #(24, 12),
                    #(32, 16)
                ],

```
**[ADDED]**
```
84                #     "clf__hidden_layer_sizes": [
85                #         (24,),
86                #         (32,),
87                #         (40,),
88                #         #(48,),
89                #         #(24, 12),
90                #         #(32, 16)
91                #     ],
```
**[REMOVED]**
```
(from line ~93)
                "clf__alpha": [
                    0.00005,
                    0.0001,
                    0.0002,
                    #0.0005,
                    #0.01
                ],

```
**[ADDED]**
```
93                #     "clf__alpha": [
94                #         0.00005,
95                #         0.0001,
96                #         0.0002,
97                #         #0.0005,
98                #         #0.01
99                #     ],
```
**[REMOVED]**
```
(from line ~101)
                "clf__learning_rate_init": [
                    #0.005,
                    0.0075,
                    0.01,
                    0.015,
                    #0.1
                ],

```
**[ADDED]**
```
101               #     "clf__learning_rate_init": [
102               #         #0.005,
103               #         0.0075,
104               #         0.01,
105               #         0.015,
106               #         #0.1
107               #     ],
```
**[REMOVED]**
```
(from line ~109)
                "clf__early_stopping": [True],
                "clf__validation_fraction": [
                    0.08, 
                    0.10, 
                    0.12, 
                    #0.15
                ],

```
**[ADDED]**
```
109               #     "clf__early_stopping": [True],
110               #     "clf__validation_fraction": [
111               #         0.08, 
112               #         0.10, 
113               #         0.12, 
114               #         #0.15
115               #     ],
```
**[REMOVED]**
```
(from line ~117)
                "clf__max_iter": [
                    500,
                    1000,
                    1500
                ],

```
**[ADDED]**
```
117               #     "clf__max_iter": [
118               #         500,
119               #         1000,
120               #         1500
121               #     ],
```
**[REMOVED]**
```
(from line ~123)
                "clf__n_iter_no_change": [
                    10, 
                    15, 
                    20
                ],

```
**[ADDED]**
```
123               #     "clf__n_iter_no_change": [
124               #         10, 
125               #         15, 
126               #         20
127               #     ],
```
**[REMOVED]**
```
(from line ~129)
                "clf__tol": [
                    0.0001, 
                    0.00005
                ]
            },

```
**[ADDED]**
```
129               #     "clf__tol": [
130               #         0.0001, 
131               #         0.00005
132               #     ]
133               # },
```
**[ADDED]**
```
175               {
176                   "clf": [KNeighborsClassifier()],
177                   "clf__n_neighbors": [3, 5, 7, 9, 11, 13, 15, 17, 19],
178                   "clf__weights": ["uniform", "distance"],
179                   "clf__metric": ["euclidean", "manhattan"],
180                   "scaler": scalers,
181                   "reducao": reducoes,
182               },
```
**[REMOVED]**
```
(from line ~184)
            #    "clf": [KNeighborsClassifier()],
            #    "clf__n_neighbors": [3, 5, 7, 9, 11, 13, 15, 17, 19],
            #    "clf__weights": ["uniform", "distance"],
            #    "clf__metric": ["euclidean", "manhattan"],
            #    "scaler": scalers,
            #    "reducao": reducoes,
            #},
            #{

```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 22/06/2026, 17:30:19*

**[REMOVED]**
```
(from line ~54)
        removed_features = ["big_toe_x_iqr"]

```
**[ADDED]**
```
54            removed_features_mlp = ["big_toe_x_iqr"]
```
**[REMOVED]**
```
(from line ~63)
            X = self.data_handler.remove_feature(X, removed_features)

```
**[ADDED]**
```
63                X = self.data_handler.remove_feature(X, removed_features_mlp)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 22/06/2026, 17:01:11*

**[REMOVED]**
```
(from line ~42)
            StandardScaler(),

```
**[ADDED]**
```
42                #StandardScaler(),
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 22/06/2026, 17:00:47*

**[REMOVED]**
```
(from line ~27)
            StandardScaler(),
            RobustScaler(),

```
**[ADDED]**
```
27                #StandardScaler(),
28                #RobustScaler(),
```
**[REMOVED]**
```
(from line ~38)
            #RobustScaler(),

```
**[ADDED]**
```
38                RobustScaler(),
```
**[REMOVED]**
```
(from line ~42)
            #StandardScaler(),

```
**[ADDED]**
```
42                StandardScaler(),
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 22/06/2026, 16:55:44*

**[REMOVED]**
```
(from line ~88)
                    (48,),
                    (24, 12),
                    (32, 16)

```
**[ADDED]**
```
88                        #(48,),
89                        #(24, 12),
90                        #(32, 16)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 22/06/2026, 16:55:42*

**[REMOVED]**
```
(from line ~88)
                    #(48,),
                    #(24, 12),
                    #(32, 16)

```
**[ADDED]**
```
88                        (48,),
89                        (24, 12),
90                        (32, 16)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 22/06/2026, 16:55:40*

**[ADDED]**
```
67                #{
68                #    "clf": [Perceptron(random_state=42, class_weight="balanced")],
69                #    "clf__eta0": [0.1, 0.01, 1.0],
70                #    "clf__penalty": ["l2", "l1", "elasticnet"],
71                #    "scaler": scalers,
72                #    "reducao": ["passthrough"],
73                #},
```
**[REMOVED]**
```
(from line ~75)
                "clf": [Perceptron(random_state=42, class_weight="balanced")],
                "clf__eta0": [0.1, 0.01, 1.0],
                "clf__penalty": ["l2", "l1", "elasticnet"],

```
**[REMOVED]**
```
(from line ~76)
                "reducao": ["passthrough"],
            },
            {
                "scaler": scalers,

```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 22/06/2026, 16:55:35*

**[REMOVED]**
```
(from line ~67)
            #{
            #    "clf": [Perceptron(random_state=42, class_weight="balanced")],
            #    "clf__eta0": [0.1, 0.01, 1.0],
            #    "clf__penalty": ["l2", "l1", "elasticnet"],
            #    "scaler": scalers,
            #    "reducao": ["passthrough"],
            #},
            #{
            #    "scaler": scalers,
            #    "reducao": reducoes,
            #    "clf": [MLPClassifier(random_state=31)],
            #    "clf__activation": [
            #        "tanh",
            #        "relu"
            #    ],
#
#
            #    "clf__hidden_layer_sizes": [
            #        (24,),
            #        (32,),
            #        (40,),
            #        #(48,),
            #        #(24, 12),
            #        #(32, 16)
            #    ],
#
            #    "clf__alpha": [
            #        0.00005,
            #        0.0001,
            #        0.0002,
            #        #0.0005,
            #        #0.01
            #    ],
#
            #    "clf__learning_rate_init": [
            #        #0.005,
            #        0.0075,
            #        0.01,
            #        0.015,
            #        #0.1
            #    ],
#
            #    "clf__early_stopping": [True],
            #    "clf__validation_fraction": [
            #        0.08, 
            #        0.10, 
            #        0.12, 
            #        #0.15
            #    ],
#
            #    "clf__max_iter": [
            #        500,
            #        1000,
            #        1500
            #    ],
#
            #    "clf__n_iter_no_change": [
            #        10, 
            #        15, 
            #        20
            #    ],
#
            #    "clf__tol": [
            #        0.0001, 
            #        0.00005
            #    ]
            #},

```
**[ADDED]**
```
67                {
68                    "clf": [Perceptron(random_state=42, class_weight="balanced")],
69                    "clf__eta0": [0.1, 0.01, 1.0],
70                    "clf__penalty": ["l2", "l1", "elasticnet"],
71                    "scaler": scalers,
72                    "reducao": ["passthrough"],
73                },
74                {
75                    "scaler": scalers,
76                    "reducao": reducoes,
77                    "clf": [MLPClassifier(random_state=31)],
78                    "clf__activation": [
79                        "tanh",
80                        "relu"
81                    ],
```
**[ADDED]**
```
83    
84                    "clf__hidden_layer_sizes": [
85                        (24,),
86                        (32,),
87                        (40,),
88                        #(48,),
89                        #(24, 12),
90                        #(32, 16)
91                    ],
92    
93                    "clf__alpha": [
94                        0.00005,
95                        0.0001,
96                        0.0002,
97                        #0.0005,
98                        #0.01
99                    ],
100   
101                   "clf__learning_rate_init": [
102                       #0.005,
103                       0.0075,
104                       0.01,
105                       0.015,
106                       #0.1
107                   ],
108   
109                   "clf__early_stopping": [True],
110                   "clf__validation_fraction": [
111                       0.08, 
112                       0.10, 
113                       0.12, 
114                       #0.15
115                   ],
116   
117                   "clf__max_iter": [
118                       500,
119                       1000,
120                       1500
121                   ],
122   
123                   "clf__n_iter_no_change": [
124                       10, 
125                       15, 
126                       20
127                   ],
128   
129                   "clf__tol": [
130                       0.0001, 
131                       0.00005
132                   ]
133               },
134   
```
**[REMOVED]**
```
(from line ~175)
            {
                "clf": [KNeighborsClassifier()],
                "clf__n_neighbors": [3, 5, 7, 9, 11, 13, 15, 17, 19],
                "clf__weights": ["uniform", "distance"],
                "clf__metric": ["euclidean", "manhattan"],
                "scaler": scalers,
                "reducao": reducoes,
            },

```
**[ADDED]**
```
176               #    "clf": [KNeighborsClassifier()],
177               #    "clf__n_neighbors": [3, 5, 7, 9, 11, 13, 15, 17, 19],
178               #    "clf__weights": ["uniform", "distance"],
179               #    "clf__metric": ["euclidean", "manhattan"],
180               #    "scaler": scalers,
181               #    "reducao": reducoes,
182               #},
183               #{
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 22/06/2026, 16:55:00*

**[REMOVED]**
```
(from line ~26)
        iterations=1,

```
**[ADDED]**
```
26            iterations=5,
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 22/06/2026, 16:54:30*

**[REMOVED]**
```
(from line ~12)
    #dict_params = None

```
**[ADDED]**
```
12        dict_params = None
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 22/06/2026, 16:54:25*

**[REMOVED]**
```
(from line ~11)
    dict_params = {'clf': [MLPClassifier(random_state=31)], 'clf__activation': ['tanh'], 'clf__alpha': [0.0001], 'clf__early_stopping': [True], 'clf__hidden_layer_sizes': [(32,)], 'clf__learning_rate_init': [0.01], 'clf__max_iter': [1000], 'clf__validation_fraction': [0.1], 'reducao': ['passthrough'], 'scaler': [RobustScaler()]}

```
**[ADDED]**
```
11        #dict_params = {'clf': [MLPClassifier(random_state=31)], 'clf__activation': ['tanh'], 'clf__alpha': [0.0001], 'clf__early_stopping': [True], 'clf__hidden_layer_sizes': [(32,)], 'clf__learning_rate_init': [0.01], 'clf__max_iter': [1000], 'clf__validation_fraction': [0.1], 'reducao': ['passthrough'], 'scaler': [RobustScaler()]}
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 22/06/2026, 16:54:20*

**[REMOVED]**
```
(from line ~63)
            #X = self.data_handler.remove_feature(X, removed_features)

```
**[ADDED]**
```
63                X = self.data_handler.remove_feature(X, removed_features)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 22/06/2026, 16:54:17*

**[REMOVED]**
```
(from line ~54)
        #removed_features = ["big_toe_x_iqr"]
        random_states = [777]  

```
**[ADDED]**
```
54            removed_features = ["big_toe_x_iqr"]
55            #random_states = [777]  
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 22/06/2026, 16:53:57*

**[REMOVED]**
```
(from line ~54)
        removed_features = ["big_toe_x_iqr"]

```
**[ADDED]**
```
54            #removed_features = ["big_toe_x_iqr"]
```
**[REMOVED]**
```
(from line ~63)
            X = self.data_handler.remove_feature(X, removed_features)

```
**[ADDED]**
```
63                #X = self.data_handler.remove_feature(X, removed_features)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 22/06/2026, 16:53:37*

**[REMOVED]**
```
(from line ~54)
        #removed_features = ["big_toe_x_iqr"]

```
**[ADDED]**
```
54            removed_features = ["big_toe_x_iqr"]
```
**[REMOVED]**
```
(from line ~63)
           #X = self.data_handler.remove_feature(X, removed_features)

```
**[ADDED]**
```
63                X = self.data_handler.remove_feature(X, removed_features)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 22/06/2026, 16:53:21*

**[REMOVED]**
```
(from line ~55)
        #random_states = [777]  

```
**[ADDED]**
```
55            random_states = [777]  
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 22/06/2026, 16:53:16*

**[REMOVED]**
```
(from line ~54)
        removed_features = ["big_toe_x_iqr"]

```
**[ADDED]**
```
54            #removed_features = ["big_toe_x_iqr"]
```
**[REMOVED]**
```
(from line ~63)
            X = self.data_handler.remove_feature(X, removed_features)

```
**[ADDED]**
```
63               #X = self.data_handler.remove_feature(X, removed_features)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 22/06/2026, 16:44:49*

**[REMOVED]**
```
(from line ~64)
            print(X)

```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 22/06/2026, 16:44:23*

**[REMOVED]**
```
(from line ~63)
            self.data_handler.remove_feature(X, removed_features)

```
**[ADDED]**
```
63                X = self.data_handler.remove_feature(X, removed_features)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 22/06/2026, 16:43:03*

**[REMOVED]**
```
(from line ~29)
    controller.run_data_analysis()
    #controller.run()

```
**[ADDED]**
```
29        #controller.run_data_analysis()
30        controller.run()
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 22/06/2026, 16:42:51*

**[ADDED]**
```
64                print(X)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/data_handler.py
*Saved at: 22/06/2026, 16:41:40*

**[REMOVED]**
```
(from line ~45)
    def remove_feature(self, X: pd.DataFrame, feature_name: str) -> pd.DataFrame:

```
**[ADDED]**
```
45        def remove_feature(self, X: pd.DataFrame, removed_features: list) -> pd.DataFrame:
```
**[REMOVED]**
```
(from line ~47)
        Remove uma feature específica do DataFrame.

```
**[ADDED]**
```
47            Remove uma ou mais features específicas do DataFrame.
```
**[REMOVED]**
```
(from line ~51)
            feature_name: Nome da feature a ser removida.

```
**[ADDED]**
```
51                removed_features: Lista de nomes das features a serem removidas.
```
**[REMOVED]**
```
(from line ~54)
            DataFrame com a feature removida.

```
**[ADDED]**
```
54                DataFrame com as features removidas.
```
**[REMOVED]**
```
(from line ~56)
        if feature_name in X.columns:
            return X.drop(columns=[feature_name])
        else:
            raise ValueError(f"Feature '{feature_name}' não encontrada no DataFrame.")

```
**[ADDED]**
```
56            return X.drop(columns=removed_features)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 22/06/2026, 16:41:08*

**[ADDED]**
```
54            removed_features = ["big_toe_x_iqr"]
```
**[REMOVED]**
```
(from line ~63)
            self.data_handler.remove_feature(X, "big_toe_x_iqr")

```
**[ADDED]**
```
63                self.data_handler.remove_feature(X, removed_features)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 16/06/2026, 10:24:51*

**[REMOVED]**
```
(from line ~94)
        rs = random.randint(1, 1000) # random_state do melhor modelo encontrado

```
**[ADDED]**
```
94            rs = 777 # random_state do melhor modelo encontrado
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 16/06/2026, 10:24:04*

**[REMOVED]**
```
(from line ~29)
    #controller.run_data_analysis()
    controller.run()

```
**[ADDED]**
```
29        controller.run_data_analysis()
30        #controller.run()
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 16/06/2026, 10:23:59*

**[REMOVED]**
```
(from line ~11)
    #dict_params = {'clf': [MLPClassifier(random_state=31)], 'clf__activation': ['tanh'], 'clf__alpha': [0.0001], 'clf__early_stopping': [True], 'clf__hidden_layer_sizes': [(32,)], 'clf__learning_rate_init': [0.01], 'clf__max_iter': [1000], 'clf__validation_fraction': [0.1], 'reducao': ['passthrough'], 'scaler': [RobustScaler()]}
    dict_params = None

```
**[ADDED]**
```
11        dict_params = {'clf': [MLPClassifier(random_state=31)], 'clf__activation': ['tanh'], 'clf__alpha': [0.0001], 'clf__early_stopping': [True], 'clf__hidden_layer_sizes': [(32,)], 'clf__learning_rate_init': [0.01], 'clf__max_iter': [1000], 'clf__validation_fraction': [0.1], 'reducao': ['passthrough'], 'scaler': [RobustScaler()]}
12        #dict_params = None
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 16/06/2026, 00:56:55*

**[REMOVED]**
```
(from line ~177)
                "clf__n_neighbors": [3, 5, 7],

```
**[ADDED]**
```
177                   "clf__n_neighbors": [3, 5, 7, 9, 11, 13, 15, 17, 19],
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 16/06/2026, 00:56:01*

**[REMOVED]**
```
(from line ~177)
                "clf__n_neighbors": [5, 7, 9],

```
**[ADDED]**
```
177                   "clf__n_neighbors": [3, 5, 7],
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 16/06/2026, 00:55:13*

**[REMOVED]**
```
(from line ~107)
        baseline_score = model.score(X_val, y_val)s

```
**[ADDED]**
```
107           baseline_score = model.score(X_val, y_val)
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 16/06/2026, 00:54:56*

**[REMOVED]**
```
(from line ~177)
                "clf__n_neighbors": [1, 3, 5, 7, 9, 11],

```
**[ADDED]**
```
177                   "clf__n_neighbors": [5, 7, 9],
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 16/06/2026, 00:54:44*

**[REMOVED]**
```
(from line ~135)
            {
                "clf": [SVC(random_state=42, class_weight="balanced")],
                "clf__C": [0.1, 1, 5, 10, 50, 100],
                "clf__kernel": ["rbf", "poly"],
                "clf__gamma": ["scale", "auto"],
                "scaler": scalers,
                "reducao": reducoes,
            },

```
**[ADDED]**
```
136               #    "clf": [SVC(random_state=42, class_weight="balanced")],
137               #    "clf__C": [0.1, 1, 5, 10, 50, 100],
138               #    "clf__kernel": ["rbf", "poly"],
139               #    "clf__gamma": ["scale", "auto"],
140               #    "scaler": scalers,
141               #    "reducao": reducoes,
142               #},
143               #{
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 16/06/2026, 00:54:31*

**[REMOVED]**
```
(from line ~107)
        baseline_score = model.score(X_val, y_val)

```
**[ADDED]**
```
107           baseline_score = model.score(X_val, y_val)s
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 16/06/2026, 00:54:30*

**[REMOVED]**
```
(from line ~94)
        rs = 777 # random_state do melhor modelo encontrado

```
**[ADDED]**
```
94            rs = random.randint(1, 1000) # random_state do melhor modelo encontrado
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 16/06/2026, 00:54:18*

**[REMOVED]**
```
(from line ~74)
            {
                "scaler": scalers,
                "reducao": reducoes,
                "clf": [MLPClassifier(random_state=31)],
                "clf__activation": [
                    "tanh",
                    "relu"
                ],

```
**[ADDED]**
```
74                #{
75                #    "scaler": scalers,
76                #    "reducao": reducoes,
77                #    "clf": [MLPClassifier(random_state=31)],
78                #    "clf__activation": [
79                #        "tanh",
80                #        "relu"
81                #    ],
82    #
83    #
84                #    "clf__hidden_layer_sizes": [
85                #        (24,),
86                #        (32,),
87                #        (40,),
88                #        #(48,),
89                #        #(24, 12),
90                #        #(32, 16)
91                #    ],
92    #
93                #    "clf__alpha": [
94                #        0.00005,
95                #        0.0001,
96                #        0.0002,
97                #        #0.0005,
98                #        #0.01
99                #    ],
100   #
101               #    "clf__learning_rate_init": [
102               #        #0.005,
103               #        0.0075,
104               #        0.01,
105               #        0.015,
106               #        #0.1
107               #    ],
108   #
109               #    "clf__early_stopping": [True],
110               #    "clf__validation_fraction": [
111               #        0.08, 
112               #        0.10, 
113               #        0.12, 
114               #        #0.15
115               #    ],
116   #
117               #    "clf__max_iter": [
118               #        500,
119               #        1000,
120               #        1500
121               #    ],
122   #
123               #    "clf__n_iter_no_change": [
124               #        10, 
125               #        15, 
126               #        20
127               #    ],
128   #
129               #    "clf__tol": [
130               #        0.0001, 
131               #        0.00005
132               #    ]
133               #},
```
**[REMOVED]**
```
(from line ~135)

                "clf__hidden_layer_sizes": [
                    (24,),
                    (32,),
                    (40,),
                    #(48,),
                    #(24, 12),
                    #(32, 16)
                ],

                "clf__alpha": [
                    0.00005,
                    0.0001,
                    0.0002,
                    #0.0005,
                    #0.01
                ],

                "clf__learning_rate_init": [
                    #0.005,
                    0.0075,
                    0.01,
                    0.015,
                    #0.1
                ],

                "clf__early_stopping": [True],
                "clf__validation_fraction": [
                    0.08, 
                    0.10, 
                    0.12, 
                    #0.15
                ],

                "clf__max_iter": [
                    500,
                    1000,
                    1500
                ],

                "clf__n_iter_no_change": [
                    10, 
                    15, 
                    20
                ],

                "clf__tol": [
                    0.0001, 
                    0.00005
                ]
            },


```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 15/06/2026, 23:26:08*

**[REMOVED]**
```
(from line ~9)
# TODO Permutation_importane para achar as features mais importantes


```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/excel_geter.py
*Saved at: 15/06/2026, 23:04:43*

**[REMOVED]**
```
(from line ~10)
    X = df_estatistico.iloc[:, 2:].values

```
**[ADDED]**
```
10        X = df_estatistico.iloc[:, 2:]
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 15/06/2026, 23:03:25*

**[REMOVED]**
```
(from line ~31)
    controller.run_data_analysis()

```
**[ADDED]**
```
31        #controller.run_data_analysis()
32        controller.run()
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 15/06/2026, 23:03:11*

**[REMOVED]**
```
(from line ~182)
            #},

```
**[ADDED]**
```
182               },
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 15/06/2026, 23:03:01*

**[REMOVED]**
```
(from line ~175)
            #{
            #    "clf": [KNeighborsClassifier()],
            #    "clf__n_neighbors": [1, 3, 5, 7, 9, 11],
            #    "clf__weights": ["uniform", "distance"],
            #    "clf__metric": ["euclidean", "manhattan"],
            #    "scaler": scalers,
            #    "reducao": reducoes,

```
**[ADDED]**
```
175               {
176                   "clf": [KNeighborsClassifier()],
177                   "clf__n_neighbors": [1, 3, 5, 7, 9, 11],
178                   "clf__weights": ["uniform", "distance"],
179                   "clf__metric": ["euclidean", "manhattan"],
180                   "scaler": scalers,
181                   "reducao": reducoes,
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 15/06/2026, 23:02:39*

**[ADDED]**
```
135               {
136                   "clf": [SVC(random_state=42, class_weight="balanced")],
137                   "clf__C": [0.1, 1, 5, 10, 50, 100],
138                   "clf__kernel": ["rbf", "poly"],
139                   "clf__gamma": ["scale", "auto"],
140                   "scaler": scalers,
141                   "reducao": reducoes,
142               },
```
**[REMOVED]**
```
(from line ~144)
            #    "clf": [SVC(random_state=42, class_weight="balanced")],
            #    "clf__C": [0.1, 1, 5, 10, 50, 100],
            #    "clf__kernel": ["rbf", "poly"],
            #    "clf__gamma": ["scale", "auto"],
            #    "scaler": scalers,
            #    "reducao": reducoes,
            #},
            #{

```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 15/06/2026, 23:01:05*

**[ADDED]**
```
67                #{
68                #    "clf": [Perceptron(random_state=42, class_weight="balanced")],
69                #    "clf__eta0": [0.1, 0.01, 1.0],
70                #    "clf__penalty": ["l2", "l1", "elasticnet"],
71                #    "scaler": scalers,
72                #    "reducao": ["passthrough"],
73                #},
```
**[REMOVED]**
```
(from line ~75)
                "clf": [Perceptron(random_state=42, class_weight="balanced")],
                "clf__eta0": [0.1, 0.01, 1.0],
                "clf__penalty": ["l2", "l1", "elasticnet"],

```
**[REMOVED]**
```
(from line ~76)
                "reducao": ["passthrough"],
            },
            {
                "scaler": scalers,

```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 15/06/2026, 23:00:53*

**[REMOVED]**
```
(from line ~29)
            MinMaxScaler(),
            MaxAbsScaler(),
            QuantileTransformer(output_distribution="uniform", random_state=42),
            QuantileTransformer(output_distribution="normal", random_state=42),
            PowerTransformer(method="yeo-johnson"),
            Normalizer(norm="l2"),

```
**[ADDED]**
```
29                #MinMaxScaler(),
30                #MaxAbsScaler(),
31                #QuantileTransformer(output_distribution="uniform", random_state=42),
32                #QuantileTransformer(output_distribution="normal", random_state=42),
33                #PowerTransformer(method="yeo-johnson"),
34                #Normalizer(norm="l2"),
35                #None,
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 15/06/2026, 23:00:29*

**[REMOVED]**
```
(from line ~50)
            PCA(n_components=0.99, random_state=31),
            SelectKBest(score_func=f_classif, k="all")

```
**[ADDED]**
```
50                #PCA(n_components=0.99, random_state=31),
51                #SelectKBest(score_func=f_classif, k="all")
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 15/06/2026, 23:00:12*

**[REMOVED]**
```
(from line ~37)
            RobustScaler(),
            RobustScaler(quantile_range=(20, 80)),
            RobustScaler(quantile_range=(10, 90)),
            RobustScaler(quantile_range=(30, 70)),
            StandardScaler(),

```
**[ADDED]**
```
37                #RobustScaler(),
38                #RobustScaler(quantile_range=(20, 80)),
39                #RobustScaler(quantile_range=(10, 90)),
40                #RobustScaler(quantile_range=(30, 70)),
41                #StandardScaler(),
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 15/06/2026, 22:59:59*

**[REMOVED]**
```
(from line ~39)
            #RobustScaler(quantile_range=(10, 90)),
            #RobustScaler(quantile_range=(30, 70)),

```
**[ADDED]**
```
39                RobustScaler(quantile_range=(10, 90)),
40                RobustScaler(quantile_range=(30, 70)),
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 15/06/2026, 22:59:54*

**[REMOVED]**
```
(from line ~27)
            #StandardScaler(),
            #RobustScaler(),
            #MinMaxScaler(),
            #MaxAbsScaler(),
            #QuantileTransformer(output_distribution="uniform", random_state=42),
            #QuantileTransformer(output_distribution="normal", random_state=42),
            #PowerTransformer(method="yeo-johnson"),
            #Normalizer(norm="l2"),
            #None,

```
**[ADDED]**
```
27                StandardScaler(),
28                RobustScaler(),
29                MinMaxScaler(),
30                MaxAbsScaler(),
31                QuantileTransformer(output_distribution="uniform", random_state=42),
32                QuantileTransformer(output_distribution="normal", random_state=42),
33                PowerTransformer(method="yeo-johnson"),
34                Normalizer(norm="l2"),
35                None,
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/model_config.py
*Saved at: 15/06/2026, 22:59:45*

**[REMOVED]**
```
(from line ~66)
            #{
            #    "clf": [Perceptron(random_state=42, class_weight="balanced")],
            #    "clf__eta0": [0.1, 0.01, 1.0],
            #    "clf__penalty": ["l2", "l1", "elasticnet"],
            #    "scaler": scalers,
            #    "reducao": ["passthrough"],
            #},

```
**[ADDED]**
```
67                    "clf": [Perceptron(random_state=42, class_weight="balanced")],
68                    "clf__eta0": [0.1, 0.01, 1.0],
69                    "clf__penalty": ["l2", "l1", "elasticnet"],
```
**[ADDED]**
```
71                    "reducao": ["passthrough"],
72                },
73                {
74                    "scaler": scalers,
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 15/06/2026, 22:59:15*

**[REMOVED]**
```
(from line ~28)
        iterations=10,

```
**[ADDED]**
```
28            iterations=1,
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 15/06/2026, 22:58:55*

**[REMOVED]**
```
(from line ~13)
    dict_params = {'clf': [MLPClassifier(random_state=31)], 'clf__activation': ['tanh'], 'clf__alpha': [0.0001], 'clf__early_stopping': [True], 'clf__hidden_layer_sizes': [(32,)], 'clf__learning_rate_init': [0.01], 'clf__max_iter': [1000], 'clf__validation_fraction': [0.1], 'reducao': ['passthrough'], 'scaler': [RobustScaler()]}
    #dict_params = None

```
**[ADDED]**
```
13        #dict_params = {'clf': [MLPClassifier(random_state=31)], 'clf__activation': ['tanh'], 'clf__alpha': [0.0001], 'clf__early_stopping': [True], 'clf__hidden_layer_sizes': [(32,)], 'clf__learning_rate_init': [0.01], 'clf__max_iter': [1000], 'clf__validation_fraction': [0.1], 'reducao': ['passthrough'], 'scaler': [RobustScaler()]}
14        dict_params = None
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 15/06/2026, 22:58:01*

**[REMOVED]**
```
(from line ~62)
            

```
**[ADDED]**
```
62                self.data_handler.remove_feature(X, "big_toe_x_iqr")
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 15/06/2026, 22:56:43*

**[ADDED]**
```
62                
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/models/data_handler.py
*Saved at: 15/06/2026, 22:56:13*

**[ADDED]**
```
45        def remove_feature(self, X: pd.DataFrame, feature_name: str) -> pd.DataFrame:
46            """
47            Remove uma feature específica do DataFrame.
48    
49            Args:
50                X: DataFrame de features.
51                feature_name: Nome da feature a ser removida.
52    
53            Returns:
54                DataFrame com a feature removida.
55            """
56            if feature_name in X.columns:
57                return X.drop(columns=[feature_name])
58            else:
59                raise ValueError(f"Feature '{feature_name}' não encontrada no DataFrame.")
60    
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 15/06/2026, 22:54:33*

**[REMOVED]**
```
(from line ~50)
    def run(self, ) -> None:

```
**[ADDED]**
```
50        def run(self) -> None:
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/requirements.txt
*Saved at: 15/06/2026, 22:38:36*

**[ADDED]**
```
13    seaborn>=0.11.0
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 15/06/2026, 22:34:08*

**[REMOVED]**
```
(from line ~124)
        # Relatório de Importância

```
**[ADDED]**
```
124           # Relatório de Importância de Features
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 15/06/2026, 22:34:04*

**[ADDED]**
```
124           # Relatório de Importância
```
**[ADDED]**
```
126           
127           # Matriz de Confusão
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 15/06/2026, 22:32:32*

**[ADDED]**
```
125           AdvancedVisualizations.plot_confusion_matrix(y_val, model.predict(X_val_scaled), class_names=["Classe 0", "Classe 1"], dataset_name="Pé frontal esquerdo - 150 amostras - 2 classes")
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/views/advanced_visualizations.py
*Saved at: 15/06/2026, 22:30:33*

**[ADDED]**
```
17        def plot_confusion_matrix(
18            y_true: np.ndarray,
19            y_pred: np.ndarray,
20            class_names: List[str] = None,
21            dataset_name: str = "Dataset"
22        ) -> None:
23            """
24            Plota a matriz de confusão com anotações.
25    
26            Args:
27                y_true: Array com os labels verdadeiros.
28                y_pred: Array com os labels previstos.
29                class_names: Nomes das classes para os rótulos dos eixos.
30                dataset_name: Nome do dataset para o título.
31            """
32            from sklearn.metrics import confusion_matrix
33            import seaborn as sns
34    
35            cm = confusion_matrix(y_true, y_pred)
36            plt.figure(figsize=(6, 5))
37            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
38                        xticklabels=class_names, yticklabels=class_names)
39            plt.xlabel('Predito')
40            plt.ylabel('Verdadeiro')
41            plt.title(f'Matriz de Confusão - {dataset_name}', fontsize=14, fontweight='bold')
42            plt.tight_layout()
43            plt.show()
44    
45        @staticmethod
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 15/06/2026, 18:16:34*

**[REMOVED]**
```
(from line ~178)
            class_names=["Classe 0", "Classe 1", "Classe 2"],

```
**[ADDED]**
```
178               class_names=["Classe 0", "Classe 1"],
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/views/advanced_visualizations.py
*Saved at: 15/06/2026, 18:15:54*

**[ADDED]**
```
150       
```
**[ADDED]**
```
152   
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 15/06/2026, 18:15:27*

**[REMOVED]**
```
(from line ~178)
            class_names=["Classe 0", "Classe 1"],

```
**[ADDED]**
```
178               class_names=["Classe 0", "Classe 1", "Classe 2"],
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 15/06/2026, 18:14:54*

**[REMOVED]**
```
(from line ~151)
        print("\n[1/4] Gerando comparação de importância de features...")

```
**[ADDED]**
```
151           print("\n Gerando comparação de importância de features...")
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 15/06/2026, 18:14:50*

**[REMOVED]**
```
(from line ~173)
        print("\n[2/4] Gerando plots 2D das top features...")

```
**[ADDED]**
```
173           print("\nGerando plots 2D das top features...")
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 15/06/2026, 18:13:58*

**[REMOVED]**
```
(from line ~178)
            class_names=["Classe 0", "Classe 1", "Classe 2"],

```
**[ADDED]**
```
178               class_names=["Classe 0", "Classe 1"],
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 15/06/2026, 18:12:08*

**[REMOVED]**
```
(from line ~182)
        # PCA 2D com Features de Influência Positiva
        print("\n[3/4] Gerando PCA com features de influência positiva...")
        # Máscara para features com coeficientes positivos na Regressão Logística
        positive_mask_lr = lr_coefficients > 0
        
        AdvancedVisualizations.plot_pca_positive_influence(
            X=X_full_df,
            y=y_full,
            feature_names=feature_names,
            positive_mask=positive_mask_lr,
            class_names=["Classe 0", "Classe 1", "Classe 2"],
            dataset_name="Pé frontal esquerdo - 150 amostras - 2 classes"
        )
        

```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 15/06/2026, 18:11:55*

**[REMOVED]**
```
(from line ~178)
            class_names=["Classe 1", "Classe 1"],

```
**[ADDED]**
```
178               class_names=["Classe 0", "Classe 1", "Classe 2"],
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 15/06/2026, 18:11:52*

**[ADDED]**
```
182           # PCA 2D com Features de Influência Positiva
183           print("\n[3/4] Gerando PCA com features de influência positiva...")
184           # Máscara para features com coeficientes positivos na Regressão Logística
185           positive_mask_lr = lr_coefficients > 0
186           
187           AdvancedVisualizations.plot_pca_positive_influence(
188               X=X_full_df,
189               y=y_full,
190               feature_names=feature_names,
191               positive_mask=positive_mask_lr,
192               class_names=["Classe 0", "Classe 1", "Classe 2"],
193               dataset_name="Pé frontal esquerdo - 150 amostras - 2 classes"
194           )
195           
```
**[ADDED]**
```
198   
199   
200   
201   
202               
203   
204   
205   
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 15/06/2026, 18:10:21*

**[REMOVED]**
```
(from line ~184)




            




```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 15/06/2026, 18:07:32*

**[REMOVED]**
```
(from line ~182)
        # PCA 2D com Features de Influência Positiva
        print("\n[3/4] Gerando PCA com features de influência positiva...")
        # Máscara para features com coeficientes positivos na Regressão Logística
        positive_mask_lr = lr_coefficients > 0
        
        AdvancedVisualizations.plot_pca_positive_influence(
            X=X_full_df,
            y=y_full,
            feature_names=feature_names,
            positive_mask=positive_mask_lr,
            class_names=["Classe 0", "Classe 1"],
            dataset_name="Pé frontal esquerdo - 150 amostras - 2 classes"
        )
        

```
**[REMOVED]**
```
(from line ~184)
    

```
**[ADDED]**
```
187   
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/views/advanced_visualizations.py
*Saved at: 15/06/2026, 18:07:24*

**[REMOVED]**
```
(from line ~150)
    @staticmethod
    def plot_pca_positive_influence(
        X: pd.DataFrame,
        y: np.ndarray,
        feature_names: List[str],
        positive_mask: np.ndarray,
        class_names: List[str] = None,
        dataset_name: str = "Dataset"
    ) -> None:
        """
        Aplica PCA 2D apenas nas features com influência positiva e plota o resultado.

```
**[REMOVED]**
```
(from line ~151)
        Args:
            X: DataFrame com as features.
            y: Array com os labels.
            feature_names: Lista de nomes das features.
            positive_mask: Máscara booleana indicando features com influência positiva.
            class_names: Nomes das classes para legenda.
            dataset_name: Nome do dataset para o título.
        """
        # Filtrar apenas features com influência positiva
        positive_features = [feature_names[i] for i in range(len(feature_names)) if positive_mask[i]]
        
        if len(positive_features) == 0:
            print("Nenhuma feature com influência positiva encontrada.")
            return
        
        X_positive = X[positive_features].values

        # Escalar os dados antes do PCA
        scaler = StandardScaler()
        X_positive_scaled = scaler.fit_transform(X_positive)

        # Aplicar PCA para reduzir para 2 componentes
        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(X_positive_scaled)

        # Criar o gráfico
        plt.figure(figsize=(10, 8))
        colors = plt.cm.Set1(np.linspace(0, 1, len(np.unique(y))))

        for class_idx, class_val in enumerate(np.unique(y)):
            mask = y == class_val
            label = class_names[class_idx] if class_names is not None else f'Classe {class_val}'
            plt.scatter(X_pca[mask, 0], X_pca[mask, 1], 
                       c=[colors[class_idx]], label=label, alpha=0.7, edgecolors='k', s=80)

        plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.2%} variância)', fontsize=12)
        plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.2%} variância)', fontsize=12)
        plt.title(f'PCA 2D - Features com Influência Positiva\n({len(positive_features)} features: {", ".join(positive_features)})', 
                  fontsize=13, fontweight='bold')
        plt.legend(loc='best', fontsize=10)
        plt.grid(True, linestyle=':', alpha=0.6)
        plt.tight_layout()
        plt.show()

        # Imprimir informações do PCA
        print(f"\n{'='*60}")
        print(f"PCA - Features com Influência Positiva")
        print(f"{'='*60}")
        print(f"Features utilizadas: {positive_features}")
        print(f"Variância explicada por PC1: {pca.explained_variance_ratio_[0]:.2%}")
        print(f"Variância explicada por PC2: {pca.explained_variance_ratio_[1]:.2%}")
        print(f"Variância total explicada: {sum(pca.explained_variance_ratio_):.2%}")
        print(f"{'='*60}\n")



```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/views/advanced_visualizations.py
*Saved at: 15/06/2026, 18:06:41*

**[ADDED]**
```
179           # Escalar os dados antes do PCA
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/views/advanced_visualizations.py
*Saved at: 15/06/2026, 18:06:33*

**[REMOVED]**
```
(from line ~179)
        # Padronizar os dados antes do PCA

```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 15/06/2026, 18:02:55*

**[ADDED]**
```
198       
```
**[REMOVED]**
```
(from line ~202)


```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 15/06/2026, 18:02:41*

**[REMOVED]**
```
(from line ~192)
            class_names=["Classe 0", "Classe 1", "Classe 2"],

```
**[ADDED]**
```
192               class_names=["Classe 0", "Classe 1"],
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 15/06/2026, 18:02:37*

**[REMOVED]**
```
(from line ~178)
            class_names=["Classe 0", "Classe 1", "Classe 2"],

```
**[ADDED]**
```
178               class_names=["Classe 1", "Classe 1"],
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 15/06/2026, 18:02:21*

**[REMOVED]**
```
(from line ~179)
            dataset_name="Dataset Iris"

```
**[ADDED]**
```
179               dataset_name="Pé frontal esquerdo - 150 amostras - 2 classes"
```
**[REMOVED]**
```
(from line ~193)
            dataset_name="Dataset Iris"

```
**[ADDED]**
```
193               dataset_name="Pé frontal esquerdo - 150 amostras - 2 classes"
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 15/06/2026, 18:01:37*

**[REMOVED]**
```
(from line ~187)
        # Alternativamente, pode-se usar threshold de importância do RF
        # threshold_rf = np.percentile(rf_feature_importances, 50)
        # positive_mask_rf = rf_feature_importances >= threshold_rf
        

```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 15/06/2026, 18:01:26*

**[REMOVED]**
```
(from line ~160)
        # 2. Identificar Top 2 features de cada método

```
**[ADDED]**
```
160           # Identificar Top 2 features de cada método
```
**[REMOVED]**
```
(from line ~172)
        # 3. Plots 2D com as Duas Melhores Features de Cada Método

```
**[ADDED]**
```
172           # Plots 2D com as Duas Melhores Features de Cada Método
```
**[REMOVED]**
```
(from line ~182)
        # 4. PCA 2D com Features de Influência Positiva

```
**[ADDED]**
```
182           # PCA 2D com Features de Influência Positiva
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/views/advanced_visualizations.py
*Saved at: 15/06/2026, 17:58:42*

**[REMOVED]**
```
(from line ~53)
        # 3. Logistic Regression Coefficients

```
**[ADDED]**
```
53            # Logistic Regression Coefficients
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/views/advanced_visualizations.py
*Saved at: 15/06/2026, 17:58:39*

**[REMOVED]**
```
(from line ~37)
        # 1. Permutation Importance

```
**[ADDED]**
```
37            # Permutation Importance
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/views/advanced_visualizations.py
*Saved at: 15/06/2026, 17:58:37*

**[REMOVED]**
```
(from line ~46)
        # 2. Random Forest Feature Importances

```
**[ADDED]**
```
46            # Random Forest Feature Importances
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 15/06/2026, 17:57:27*

**[REMOVED]**
```
(from line ~157)
            dataset_name="Dataset Iris"

```
**[ADDED]**
```
157               dataset_name="Pé frontal esquerdo - 150 amostras - 2 classes"
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 15/06/2026, 17:49:56*

**[REMOVED]**
```
(from line ~141)
        # Extrair importâncias

```
**[ADDED]**
```
141           # Extrair importâncias da árcore
```
**[REMOVED]**
```
(from line ~144)
        # Para Regressão Logística multiclasse: média dos valores absolutos dos coeficientes

```
**[ADDED]**
```
144           # Para Regressão Logística eu peguei a média dos valores absolutos dos coeficientes
```
**[REMOVED]**
```
(from line ~150)
        # 1. Comparação de Importância de Features com Gráficos

```
**[ADDED]**
```
150           # Comparação de Importância de Features com Gráficos
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 15/06/2026, 17:43:31*

**[REMOVED]**
```
(from line ~126)
        # ============================================================
        # NOVAS FUNCIONALIDADES DE ANÁLISE E VISUALIZAÇÃO
        # ============================================================
        print("\n--- Gerando Visualizações Avançadas ---")

```
**[ADDED]**
```
126     
127           print("\n--- Gerando Visualizações Detalhadas ---")
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/views/advanced_visualizations.py
*Saved at: 15/06/2026, 17:41:59*

**[REMOVED]**
```
(from line ~341)
        else:  # BOM AJUSTE

```
**[ADDED]**
```
341           else: 
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/views/advanced_visualizations.py
*Saved at: 15/06/2026, 17:41:44*

**[ADDED]**
```
321               print(f"Diferença:           {(resultados['f1_treino'] - resultados['f1_teste']):.2%}")
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/views/advanced_visualizations.py
*Saved at: 15/06/2026, 17:40:06*

**[REMOVED]**
```
(from line ~322)
        print(f"\n>>> DIAGNÓSTICO: {diagnostico}")

```
**[ADDED]**
```
322           print(f"\nDIAGNÓSTICO: {diagnostico}")
```
**[REMOVED]**
```
(from line ~325)
            print("\n⚠️  O modelo memorizou os dados de treino e não generaliza bem.")

```
**[ADDED]**
```
325               print("\n O modelo memorizou os dados de treino e não generaliza bem.")
```
**[REMOVED]**
```
(from line ~333)
            print("\n⚠️  O modelo não conseguiu aprender padrões suficientes.")

```
**[ADDED]**
```
333               print("\n O modelo não conseguiu aprender padrões suficientes.")
```
**[REMOVED]**
```
(from line ~341)
            print("\n✓ O modelo apresentou bom equilíbrio entre aprendizado e generalização.")

```
**[ADDED]**
```
341               print("\n O modelo apresentou bom equilíbrio entre aprendizado e generalização.")
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/controllers/training_controller.py
*Saved at: 15/06/2026, 17:28:24*

**[REMOVED]**
```
(from line ~16)
from sklearn.model_selection import train_test_split

```

---

