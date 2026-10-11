### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 11/10/2026, 19:01:58*

**[REMOVED]**
```
(from line ~20)
    dict_params = {'clf': RandomForestRegressor(random_state=42), 'clf__ccp_alpha': 0.01, 'clf__criterion': 'squared_error', 'clf__max_depth': None, 'clf__min_samples_split': 5, 'clf__n_estimators': 145, 'reducao': 'passthrough', 'scaler': None}

```
**[ADDED]**
```
20        dict_params = {'clf': [RandomForestRegressor(random_state=42)], 'clf__ccp_alpha': [0.01], 'clf__criterion': ['squared_error'], 'clf__max_depth': [None], 'clf__min_samples_split': [5], 'clf__n_estimators': [145], 'reducao': ['passthrough'], 'scaler': [None]}
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 11/10/2026, 19:01:36*

**[REMOVED]**
```
(from line ~25)
    DATA_PATH = "./planilhas/Machine learning ganhos de forca (10RM-POS).xlsx"

```
**[ADDED]**
```
25        DATA_PATH = "./planilhas/Machine learning ganhos de forca (FIM POS).xlsx"
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 11/10/2026, 19:00:43*

**[ADDED]**
```
4     from sklearn.ensemble import RandomForestRegressor
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 11/10/2026, 19:00:38*

**[REMOVED]**
```
(from line ~19)
    dict_params = {'clf': [Ridge()], 'clf__alpha': [0.01], 'reducao': [PCA(n_components=0.98, random_state=31)], 'scaler': [StandardScaler()]}

```
**[ADDED]**
```
19        dict_params = {'clf': RandomForestRegressor(random_state=42), 'clf__ccp_alpha': 0.01, 'clf__criterion': 'squared_error', 'clf__max_depth': None, 'clf__min_samples_split': 5, 'clf__n_estimators': 145, 'reducao': 'passthrough', 'scaler': None}
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 11/10/2026, 18:58:40*

**[REMOVED]**
```
(from line ~19)
    dict_params = {'clf': [LinearRegression()], 'reducao': [PCA(n_components=0.95, random_state=31)], 'scaler': [StandardScaler(with_mean=False)]}

```
**[ADDED]**
```
19        dict_params = {'clf': [Ridge()], 'clf__alpha': [0.01], 'reducao': [PCA(n_components=0.98, random_state=31)], 'scaler': [StandardScaler()]}
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 11/10/2026, 18:58:08*

**[REMOVED]**
```
(from line ~24)
    DATA_PATH = "./planilhas/Machine learning ganhos de forca (1RM-POS).xlsx"

```
**[ADDED]**
```
24        DATA_PATH = "./planilhas/Machine learning ganhos de forca (10RM-POS).xlsx"
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 11/10/2026, 18:56:54*

**[REMOVED]**
```
(from line ~4)
from statistics import LinearRegression

```
**[ADDED]**
```
4     from sklearn.linear_model import LinearRegression
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 11/10/2026, 18:55:36*

**[REMOVED]**
```
(from line ~19)
    dict_params = {'clf': [LinearRegression(0,0)], 'reducao': [PCA(n_components=0.95, random_state=31)], 'scaler': [StandardScaler(with_mean=False)]}

```
**[ADDED]**
```
19        dict_params = {'clf': [LinearRegression()], 'reducao': [PCA(n_components=0.95, random_state=31)], 'scaler': [StandardScaler(with_mean=False)]}
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 11/10/2026, 18:55:20*

**[REMOVED]**
```
(from line ~19)
    dict_params = {'clf': [LinearRegression()], 'reducao': [PCA(n_components=0.95, random_state=31)], 'scaler': [StandardScaler(with_mean=False)]}

```
**[ADDED]**
```
19        dict_params = {'clf': [LinearRegression(0,0)], 'reducao': [PCA(n_components=0.95, random_state=31)], 'scaler': [StandardScaler(with_mean=False)]}
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 11/10/2026, 18:49:52*

**[REMOVED]**
```
(from line ~19)
    dict_params = {'clf': LinearRegression(), 'reducao': PCA(n_components=0.95, random_state=31), 'scaler': StandardScaler(with_mean=False)}

```
**[ADDED]**
```
19        dict_params = {'clf': [LinearRegression()], 'reducao': [PCA(n_components=0.95, random_state=31)], 'scaler': [StandardScaler(with_mean=False)]}
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 11/10/2026, 18:49:30*

**[ADDED]**
```
4     from statistics import LinearRegression
5     
6     from sklearn.decomposition import PCA
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 11/10/2026, 18:49:21*

**[REMOVED]**
```
(from line ~16)
    dict_params = {'clf': [Ridge()], 'clf__alpha': [0.3], 'clf__fit_intercept': [True], 'reducao': ['passthrough'], 'scaler': [StandardScaler()]}

```
**[ADDED]**
```
16        dict_params = {'clf': LinearRegression(), 'reducao': PCA(n_components=0.95, random_state=31), 'scaler': StandardScaler(with_mean=False)}
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 11/10/2026, 18:48:51*

**[REMOVED]**
```
(from line ~21)
    DATA_PATH = "./planilhas/Machine learning ganhos de forca (MT-POS).xlsx"

```
**[ADDED]**
```
21        DATA_PATH = "./planilhas/Machine learning ganhos de forca (1RM-POS).xlsx"
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 11/10/2026, 18:43:55*

**[REMOVED]**
```
(from line ~16)
    dict_params = {'clf': Ridge(), 'clf__alpha': 0.3, 'clf__fit_intercept': True, 'reducao': 'passthrough', 'scaler': StandardScaler()}

```
**[ADDED]**
```
16        dict_params = {'clf': [Ridge()], 'clf__alpha': [0.3], 'clf__fit_intercept': [True], 'reducao': ['passthrough'], 'scaler': [StandardScaler()]}
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 11/10/2026, 18:42:54*

**[REMOVED]**
```
(from line ~33)
    #controller.run_data_analysis()
    controller.run()

```
**[ADDED]**
```
33        controller.run_data_analysis()
34        #controller.run()
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 11/10/2026, 18:42:38*

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
*Saved at: 11/10/2026, 18:41:27*

**[ADDED]**
```
4     from sklearn.linear_model import Ridge
5     
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 11/10/2026, 18:41:19*

**[REMOVED]**
```
(from line ~12)
    # Parametros específicos para o MLP
    #dict_params = {'clf': [MLPClassifier(random_state=31)], 'clf__activation': ['tanh'], 'clf__alpha': [0.0001], 'clf__early_stopping': [True], 'clf__hidden_layer_sizes': [(32,)], 'clf__learning_rate_init': [0.01], 'clf__max_iter': [1000], 'clf__validation_fraction': [0.1], 'reducao': ['passthrough'], 'scaler': [RobustScaler()]}

```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/src/main.py
*Saved at: 11/10/2026, 18:41:06*

**[REMOVED]**
```
(from line ~16)
    #dict_params = {'clf': [KNeighborsClassifier()], 'clf__metric': ['euclidean'], 'clf__n_neighbors': [5], 'clf__weights': ['uniform'], 'reducao': ['passthrough'], 'scaler': [PowerTransformer()]}

```
**[ADDED]**
```
16        dict_params = {'clf': Ridge(), 'clf__alpha': 0.3, 'clf__fit_intercept': True, 'reducao': 'passthrough', 'scaler': StandardScaler()}
```

---

