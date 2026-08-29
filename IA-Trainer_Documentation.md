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

