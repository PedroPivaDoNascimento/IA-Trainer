### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/ml_interface/views.py
*Saved at: 28/08/2026, 15:56:17*

**[ADDED]**
```
9     import numpy as np
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/ml_interface/views.py
*Saved at: 28/08/2026, 15:55:11*

**[REMOVED]**
```
(from line ~12)
from django.views.decorators.http import require_POST

```
**[ADDED]**
```
12    from django.views.decorators.http import require_POST, require_GET
```
**[REMOVED]**
```
(from line ~29)
    (Mantida por compatibilidade, embora não seja mais usada na lógica automática)

```
**[ADDED]**
```
29        Nota: Com a nova regra (última coluna = target), esta view pode ser menos utilizada,
30        mas mantida para possíveis validações futuras ou exibição de preview.
```
**[REMOVED]**
```
(from line ~59)
    Regra de Negócio: A última coluna é sempre o Target (y), as demais são Features (X).

```
**[ADDED]**
```
59        Regra de Negócio: A última coluna do Excel é sempre o Target (y).
```
**[REMOVED]**
```
(from line ~98)
                    # REGRA AUTOMÁTICA: Última coluna = Target, Resto = Features

```
**[ADDED]**
```
98                        # REGRA AUTOMÁTICA: Última coluna é Target, resto é Feature
```
**[REMOVED]**
```
(from line ~101)
                        raise ValueError("O arquivo deve ter pelo menos 2 colunas (uma feature e uma target).")

```
**[ADDED]**
```
101                           raise ValueError("O arquivo deve ter pelo menos 2 colunas (1 feature e 1 target).")
```
**[REMOVED]**
```
(from line ~107)
                    logger.info(f"Target detectada: {target_column}")

```
**[ADDED]**
```
107                       logger.info(f"Target detectado: {target_column}")
```
**[REMOVED]**
```
(from line ~113)
                    # Tratamento básico de valores faltantes (opcional, mas recomendado)
                    # Se houver NaNs, o treino falhará. Aqui preenchemos com a média/moda se necessário.
                    # Para simplicidade, assumimos dados limpos ou levantamos erro.
                    if pd.isnull(X).any() or pd.isnull(y).any():
                         # Estratégia simples: remover linhas com NaN
                         df_clean = df.dropna()
                         X = df_clean[feature_columns].values
                         y = df_clean[target_column].values
                         logger.warning("Linhas com valores nulos foram removidas.")


```
**[ADDED]**
```
113                       # Tratamento básico de tipos para evitar erros no sklearn
114                       # Converte y para numérico se for categórico
115                       if not np.issubdtype(y.dtype, np.number):
116                           from sklearn.preprocessing import LabelEncoder
117                           le = LabelEncoder()
118                           y = le.fit_transform(y)
119                           logger.info(f"Target codificado com LabelEncoder. Classes: {le.classes_}")
120                       
```
**[REMOVED]**
```
(from line ~122)
                    # Nota: stratify=y pode falhar se y tiver classes com apenas 1 exemplo após dropna.
                    # Adicionamos um try-except para fallback sem stratify se necessário.
                    try:
                        X_train, X_test, y_train, y_test = train_test_split(
                            X, y, 
                            test_size=0.2, 
                            random_state=random_state, 
                            stratify=y
                        )
                    except ValueError:
                        logger.warning("Stratify falhou (classes minoritárias pequenas). Tentando sem stratify.")
                        X_train, X_test, y_train, y_test = train_test_split(
                            X, y, 
                            test_size=0.2, 
                            random_state=random_state
                        )

```
**[ADDED]**
```
122                       X_train, X_test, y_train, y_test = train_test_split(
123                           X, y, 
124                           test_size=0.2, 
125                           random_state=random_state, 
126                           stratify=y if len(np.unique(y)) > 1 else None # Evita erro se só houver 1 classe
127                       )
```
**[REMOVED]**
```
(from line ~173)
                context['error_message'] = f"Erro durante o treinamento: {str(e)}\n\n{traceback.format_exc()}"
                logger.error(traceback.format_exc())

```
**[ADDED]**
```
173                   context['error_message'] = f"Erro durante o treinamento: {str(e)}\n\nDetalhes: {traceback.format_exc()}"
```
**[REMOVED]**
```
(from line ~178)
                # Tenta pegar o label legível, senão usa o nome do campo
                field_obj = form.fields.get(field_name)
                label = field_obj.label if field_obj and hasattr(field_obj, 'label') else field_name.replace('_', ' ').title()
                

```
**[ADDED]**
```
178                   field_label = form.fields.get(field_name, {}).label if hasattr(form.fields.get(field_name), 'label') else field_name
```
**[REMOVED]**
```
(from line ~180)
                    error_details.append(f"<strong>{label}:</strong> {error}")

```
**[ADDED]**
```
180                       error_details.append(f"<strong>{field_label}:</strong> {error}")
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/ml_interface/utils/dynamic_trainer.py
*Saved at: 28/08/2026, 15:54:40*

**[REMOVED]**
```
(from line ~2)
Módulo adaptado para treinamento de ML com configuração dinâmica via Django.
Recebe parâmetros de validação cruzada e random_state para reprodutibilidade.

```
**[ADDED]**
```
2     Módulo responsável pelo treinamento dinâmico de modelos de ML.
3     Constrói Pipelines e Param Grids baseados em configuração JSON.
```
**[REMOVED]**
```
(from line ~5)
from typing import Any, Dict, List

```
**[ADDED]**
```
5     import os
6     import joblib
```
**[REMOVED]**
```
(from line ~10)
from sklearn.preprocessing import StandardScaler

```
**[ADDED]**
```
10    from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
```
**[REMOVED]**
```
(from line ~12)
from sklearn.svm import SVC

```
**[REMOVED]**
```
(from line ~13)
import joblib
import os
from django.conf import settings

```
**[ADDED]**
```
13    from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
14    from sklearn.linear_model import LogisticRegression
15    from sklearn.svm import SVC
16    from sklearn.neural_network import MLPClassifier
17    from sklearn.metrics import make_scorer, f1_score, accuracy_score, precision_score, recall_score
```
**[REMOVED]**
```
(from line ~19)


```
**[REMOVED]**
```
(from line ~21)
    Treinador dinâmico que constrói pipelines baseados em configuração JSON.
    Aceita cv (folds) e random_state para controle total da validação cruzada.

```
**[ADDED]**
```
21        Classe que gerencia a construção dinâmica do Pipeline e treinamento com GridSearchCV.
```
**[REMOVED]**
```
(from line ~24)
    # Mapeamento de nomes de classes para imports do scikit-learn
    SCALERS = {
        'StandardScaler': StandardScaler,
        'RobustScaler': lambda **kwargs: __import__('sklearn.preprocessing', fromlist=['RobustScaler']).RobustScaler(**kwargs),
        'MinMaxScaler': lambda **kwargs: __import__('sklearn.preprocessing', fromlist=['MinMaxScaler']).MinMaxScaler(**kwargs),
        'MaxAbsScaler': lambda **kwargs: __import__('sklearn.preprocessing', fromlist=['MaxAbsScaler']).MaxAbsScaler(**kwargs),
        'QuantileTransformer': lambda **kwargs: __import__('sklearn.preprocessing', fromlist=['QuantileTransformer']).QuantileTransformer(**kwargs),
        'PowerTransformer': lambda **kwargs: __import__('sklearn.preprocessing', fromlist=['PowerTransformer']).PowerTransformer(**kwargs),
        'Normalizer': lambda **kwargs: __import__('sklearn.preprocessing', fromlist=['Normalizer']).Normalizer(**kwargs),
    }
    
    REDUCERS = {
        'PCA': PCA,
        'SelectKBest': lambda **kwargs: __import__('sklearn.feature_selection', fromlist=['SelectKBest', 'f_classif']).SelectKBest(score_func=f_classif, **kwargs),
    }
    
    CLASSIFIERS = {
        'MLPClassifier': lambda **kwargs: __import__('sklearn.neural_network', fromlist=['MLPClassifier']).MLPClassifier(**kwargs),
        'RandomForestClassifier': lambda **kwargs: __import__('sklearn.ensemble', fromlist=['RandomForestClassifier']).RandomForestClassifier(**kwargs),
        'SVC': lambda **kwargs: __import__('sklearn.svm', fromlist=['SVC']).SVC(**kwargs),
        'LinearSVC': lambda **kwargs: __import__('sklearn.svm', fromlist=['LinearSVC']).LinearSVC(**kwargs),
        'KNeighborsClassifier': lambda **kwargs: __import__('sklearn.neighbors', fromlist=['KNeighborsClassifier']).KNeighborsClassifier(**kwargs),
        'LogisticRegression': lambda **kwargs: __import__('sklearn.linear_model', fromlist=['LogisticRegression']).LogisticRegression(**kwargs),
        'GradientBoostingClassifier': lambda **kwargs: __import__('sklearn.ensemble', fromlist=['GradientBoostingClassifier']).GradientBoostingClassifier(**kwargs),
        'ExtraTreesClassifier': lambda **kwargs: __import__('sklearn.ensemble', fromlist=['ExtraTreesClassifier']).ExtraTreesClassifier(**kwargs),
        'RidgeClassifier': lambda **kwargs: __import__('sklearn.linear_model', fromlist=['RidgeClassifier']).RidgeClassifier(**kwargs),
        'Perceptron': lambda **kwargs: __import__('sklearn.linear_model', fromlist=['Perceptron']).Perceptron(**kwargs),
    }
    
    def __init__(self, metric_focus: str = 'f1_score'):
        """
        Inicializa o treinador.
        
        Args:
            metric_focus: Métrica alvo para otimização no GridSearchCV.
        """

```
**[ADDED]**
```
24        def __init__(self, metric_focus='f1_score'):
```
**[REMOVED]**
```
(from line ~26)
        self.scoring = {
            'accuracy': 'accuracy',
            'precision': 'precision',
            'recall': 'recall',
            'f1_score': 'f1',
            'roc_auc': 'roc_auc'

```
**[ADDED]**
```
26            self.save_dir = os.path.join('media', 'modelos_treinados')
27            os.makedirs(self.save_dir, exist_ok=True)
28            
29            # Mapeamento de Scalers
30            self.scalers_map = {
31                'StandardScaler': StandardScaler,
32                'MinMaxScaler': MinMaxScaler,
33                'RobustScaler': RobustScaler
```
**[REMOVED]**
```
(from line ~35)
        self.refit_metric = self.scoring.get(metric_focus, 'f1')
    
    def _create_instance(self, class_name: str, params: Dict = None):
        """Cria uma instância de uma classe scikit-learn."""
        params = params or {}

```
**[REMOVED]**
```
(from line ~36)
        # Tenta encontrar nas mappings
        all_mappings = {**self.SCALERS, **self.REDUCERS, **self.CLASSIFIERS}

```
**[ADDED]**
```
36            # Mapeamento de Redutores (PCA e SelectKBest)
37            self.reducers_map = {
38                'PCA': PCA,
39                'SelectKBest': SelectKBest
40            }
```
**[REMOVED]**
```
(from line ~42)
        if class_name in all_mappings:
            factory = all_mappings[class_name]
            try:
                return factory(**params)
            except Exception as e:
                print(f"Erro ao criar instância de {class_name}: {e}")
                raise
        
        # Fallback: tenta importar diretamente
        raise ValueError(f"Classe não encontrada: {class_name}")
    
    def build_pipeline_and_grid(self, config: Dict, random_state: int):

```
**[ADDED]**
```
42            # Mapeamento de Classificadores
43            self.classifiers_map = {
44                'RandomForestClassifier': RandomForestClassifier,
45                'MLPClassifier': MLPClassifier,
46                'SVC': SVC,
47                'LogisticRegression': LogisticRegression,
48                'GradientBoostingClassifier': GradientBoostingClassifier
49            }
50    
51        def build_pipeline(self, config):
```
**[REMOVED]**
```
(from line ~53)
        Constrói o Pipeline e o param_grid dinamicamente a partir da configuração JSON.
        
        Args:
            config: Dicionário com configuração do scaler, pca e classifier.
            random_state: Semente aleatória para reprodutibilidade.
            
        Returns:
            Tuple (pipeline, param_grid)

```
**[ADDED]**
```
53            Constrói o Pipeline do scikit-learn baseado na configuração JSON.
```
**[REMOVED]**
```
(from line ~55)
        # Extrai configurações
        scaler_config = config.get('scaler', {'class': 'StandardScaler', 'params': {}})
        pca_config = config.get('pca', {'enabled': False})
        classifier_config = config.get('classifier')
        
        if not classifier_config:
            raise ValueError("Configuração do classifier é obrigatória.")
        
        # Cria steps do pipeline

```
**[REMOVED]**
```
(from line ~56)
        param_grid = {}

```
**[REMOVED]**
```
(from line ~57)
        # Step 1: Scaler
        scaler_class = scaler_config.get('class', 'StandardScaler')

```
**[ADDED]**
```
57            # 1. Adicionar Scaler (Sempre presente)
58            scaler_config = config.get('scaler', {})
59            scaler_name = scaler_config.get('class', 'StandardScaler')
```
**[REMOVED]**
```
(from line ~61)
        scaler_instance = self._create_instance(scaler_class, scaler_params)
        steps.append(('scaler', scaler_instance))

```
**[REMOVED]**
```
(from line ~62)
        # Adiciona parâmetros do scaler ao grid (se houver params_grid)
        scaler_grid = scaler_config.get('params_grid', {})
        for param_name, values in scaler_grid.items():
            param_grid[f'scaler__{param_name}'] = values
        
        # Step 2: PCA (opcional)

```
**[ADDED]**
```
62            if scaler_name in self.scalers_map:
63                steps.append(('scaler', self.scalers_map[scaler_name](**scaler_params)))
64            else:
65                # Fallback para StandardScaler se nome inválido
66                steps.append(('scaler', StandardScaler()))
67                
68            # 2. Adicionar Redutor de Dimensionalidade (Opcional)
69            pca_config = config.get('pca', {})
```
**[REMOVED]**
```
(from line ~71)
            pca_class = pca_config.get('class', 'PCA')
            pca_params = pca_config.get('params', {})
            # Garante random_state no PCA se aplicável
            if 'random_state' not in pca_params and pca_class == 'PCA':
                pca_params['random_state'] = random_state
            pca_instance = self._create_instance(pca_class, pca_params)
            steps.append(('pca', pca_instance))

```
**[ADDED]**
```
71                reducer_name = pca_config.get('class', 'PCA')
72                reducer_params = pca_config.get('params', {})
```
**[REMOVED]**
```
(from line ~74)
            # Adiciona parâmetros do PCA ao grid
            pca_grid = pca_config.get('params_grid', {})
            for param_name, values in pca_grid.items():
                param_grid[f'pca__{param_name}'] = values
        else:
            # Passthrough - não faz redução
            steps.append(('pca', 'passthrough'))

```
**[ADDED]**
```
74                if reducer_name in self.reducers_map:
75                    steps.append(('pca', self.reducers_map[reducer_name](**reducer_params)))
76                else:
77                    steps.append(('pca', PCA(**reducer_params)))
```
**[REMOVED]**
```
(from line ~79)
        # Step 3: Classifier
        classifier_class = classifier_config.get('class')
        classifier_params = classifier_config.get('params', {})
        # Garante random_state no classifier se aplicável
        if 'random_state' not in classifier_params and classifier_class in ['MLPClassifier', 'RandomForestClassifier', 'SVC', 'LinearSVC', 'ExtraTreesClassifier', 'GradientBoostingClassifier', 'LogisticRegression', 'RidgeClassifier', 'Perceptron']:
            classifier_params['random_state'] = random_state
        classifier_instance = self._create_instance(classifier_class, classifier_params)
        steps.append(('classifier', classifier_instance))

```
**[ADDED]**
```
79            # 3. Adicionar Classificador
80            clf_config = config.get('classifier', {})
81            clf_name = clf_config.get('class', 'RandomForestClassifier')
82            # Params vazios aqui, pois serão injetados pelo GridSearch
```
**[REMOVED]**
```
(from line ~84)
        # Adiciona parâmetros do classifier ao grid
        classifier_grid = classifier_config.get('params_grid', {})
        for param_name, values in classifier_grid.items():
            param_grid[f'classifier__{param_name}'] = values
        
        # Cria o pipeline
        pipeline = Pipeline(steps)
        
        return pipeline, param_grid
    
    def train(
        self, 
        X_train: np.ndarray, 
        y_train: np.ndarray, 
        config: Dict, 
        cv_folds: int = 5, 
        random_state: int = 42
    ):

```
**[ADDED]**
```
84            if clf_name in self.classifiers_map:
85                steps.append(('classifier', self.classifiers_map[clf_name]()))
86            else:
87                steps.append(('classifier', RandomForestClassifier()))
88                
89            return Pipeline(steps)
90    
91        def build_param_grid(self, config):
```
**[REMOVED]**
```
(from line ~93)
        Executa o GridSearchCV com configuração dinâmica.

```
**[ADDED]**
```
93            Constrói o dicionário param_grid para o GridSearchCV.
94            Usa a notação de prefixos (ex: scaler__param).
95            """
96            param_grid = {}
```
**[REMOVED]**
```
(from line ~98)
        Args:
            X_train: Features de treino.
            y_train: Labels de treino.
            config: Configuração JSON do pipeline.
            cv_folds: Número de folds para validação cruzada.
            random_state: Semente aleatória para StratifiedKFold e reprodutibilidade.

```
**[ADDED]**
```
98            # Scaler Params
99            scaler_config = config.get('scaler', {})
100           scaler_params_grid = scaler_config.get('params_grid', {})
101           for param, values in scaler_params_grid.items():
102               param_grid[f'scaler__{param}'] = values
```
**[REMOVED]**
```
(from line ~104)
        Returns:
            Objeto GridSearchCV treinado.

```
**[ADDED]**
```
104           # PCA Params (se enabled)
105           pca_config = config.get('pca', {})
106           if pca_config.get('enabled', False):
107               pca_params_grid = pca_config.get('params_grid', {})
108               for param, values in pca_params_grid.items():
109                   param_grid[f'pca__{param}'] = values
110           else:
111               # Se não estiver habilitado mas houver params no grid, podemos ignorar ou forçar None
112               # Aqui vamos ignorar para simplificar
113               pass
114               
115           # Classifier Params
116           clf_config = config.get('classifier', {})
117           clf_params_grid = clf_config.get('params_grid', {})
118           for param, values in clf_params_grid.items():
119               param_grid[f'classifier__{param}'] = values
120               
121           return param_grid
122   
123       def train(self, X_train, y_train, config, cv_folds=5, random_state=42):
```
**[REMOVED]**
```
(from line ~125)
        # Constrói pipeline e grid dinamicamente
        pipeline, param_grid = self.build_pipeline_and_grid(config, random_state)

```
**[ADDED]**
```
125           Executa o treinamento com GridSearchCV.
126           """
127           pipeline = self.build_pipeline(config)
128           param_grid = self.build_param_grid(config)
```
**[REMOVED]**
```
(from line ~130)
        # Cria StratifiedKFold com random_state controlado
        cv = StratifiedKFold(
            n_splits=cv_folds,
            shuffle=True,
            random_state=random_state
        )

```
**[ADDED]**
```
130           # Configuração de Métricas Múltiplas
131           scoring = {
132               'accuracy': make_scorer(accuracy_score),
133               'precision': make_scorer(precision_score, average='weighted'),
134               'recall': make_scorer(recall_score, average='weighted'),
135               'f1': make_scorer(f1_score, average='weighted')
136           }
```
**[REMOVED]**
```
(from line ~138)
        # Cria GridSearchCV
        grid = GridSearchCV(

```
**[ADDED]**
```
138           # Validação Cruzada Estratificada com Random State Controlado
139           cv_strategy = StratifiedKFold(n_splits=cv_folds, shuffle=True, random_state=random_state)
140           
141           # Instanciação do GridSearchCV
142           # CORREÇÃO AQUI: refit='f1' é obrigatório quando scoring é um dict
143           grid_search = GridSearchCV(
```
**[REMOVED]**
```
(from line ~146)
            cv=cv,
            n_jobs=-1,  # Usa todos os cores disponíveis
            scoring=self.scoring,
            refit=self.refit_metric,

```
**[ADDED]**
```
146               scoring=scoring,
147               cv=cv_strategy,
148               refit='f1',  # Define qual métrica usar para escolher o best_estimator_
149               n_jobs=-1,   # Usa todos os núcleos da CPU
```
**[REMOVED]**
```
(from line ~151)
            error_score='raise'  # Falha rápido se houver erro

```
**[ADDED]**
```
151               error_score='raise' # Falha rápido se houver erro nos params
```
**[REMOVED]**
```
(from line ~154)
        # Executa o fit
        grid.fit(X_train, y_train)

```
**[ADDED]**
```
154           print("Iniciando GridSearchCV...")
155           grid_search.fit(X_train, y_train)
156           print("Treinamento concluído.")
```
**[REMOVED]**
```
(from line ~158)
        return grid
    
    def save_model(self, grid_search: Any, model_name: str):

```
**[ADDED]**
```
158           return grid_search
159   
160       def save_model(self, model_object, filename):
```
**[REMOVED]**
```
(from line ~162)
        Salva o melhor modelo encontrado.
        
        Args:
            grid_search: GridSearchCV treinado.
            model_name: Nome do arquivo .pkl.

```
**[ADDED]**
```
162           Salva o modelo treinado em disco.
```
**[REMOVED]**
```
(from line ~164)
        modelos_dir = os.path.join(settings.MEDIA_ROOT, 'modelos_treinados')
        os.makedirs(modelos_dir, exist_ok=True)
        
        file_path = os.path.join(modelos_dir, model_name)
        joblib.dump(grid_search.best_estimator_, file_path)
        
        return file_path

```
**[ADDED]**
```
164           filepath = os.path.join(self.save_dir, filename)
165           joblib.dump(model_object, filepath)
166           print(f"Modelo salvo em: {filepath}")
167           return filepath
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/ml_interface/templates/ml_interface/train.html
*Saved at: 28/08/2026, 15:46:06*

**[REMOVED]**
```
(from line ~1)
--- ml_interface/templates/ml_interface/train.html (原始)

```
**[ADDED]**
```
1     <!-- ml_interface/templates/ml_interface/train.html -->
```
**[REMOVED]**
```
(from line ~7)
    <title>IA-Trainer - Interface Web Django</title>

    <!-- Bootstrap 5 CSS -->

```
**[ADDED]**
```
7         <title>IA-Trainer | Treinamento de Modelos</title>
```
**[REMOVED]**
```
(from line ~9)
    <!-- Bootstrap Icons -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css" rel="stylesheet">


```
**[REMOVED]**
```
(from line ~10)
        body {
            background-color: #f8f9fa;

```
**[ADDED]**
```
10            body { background-color: #f8f9fa; }
11            .card { box-shadow: 0 4px 6px rgba(0,0,0,0.1); border: none; margin-bottom: 20px; }
12            .card-header { background-color: #0d6efd; color: white; font-weight: bold; }
13            .loading-overlay {
14                position: fixed; top: 0; left: 0; width: 100%; height: 100%;
15                background: rgba(255, 255, 255, 0.9); z-index: 9999;
16                display: none; justify-content: center; align-items: center; flex-direction: column;
```
**[REMOVED]**
```
(from line ~18)
        .container {
            max-width: 1200px;
            margin-top: 30px;
            margin-bottom: 50px;
        }
        .card {
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border: none;
            margin-bottom: 20px;
        }
        .card-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            font-weight: bold;
        }
        .form-label {
            font-weight: 500;
            color: #495057;
        }
        .help-text {
            font-size: 0.85rem;
            color: #6c757d;
        }

        /* Overlay de carregamento */
        #loading-overlay {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(255, 255, 255, 0.9);
            z-index: 9999;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }
        #loading-overlay.active {
            display: flex;
        }
        .spinner-border-lg {
            width: 5rem;
            height: 5rem;
        }
        .loading-text {
            margin-top: 20px;
            font-size: 1.2rem;
            color: #667eea;
            font-weight: bold;
        }

        /* Resultados */
        .result-card {
            background-color: #e8f5e9;
            border-left: 5px solid #4caf50;
        }
        .error-card {
            background-color: #ffebee;
            border-left: 5px solid #f44336;
        }
        .param-badge {
            background-color: #667eea;
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
            margin: 3px;
            display: inline-block;
        }

        /* Botão de exemplo JSON */
        .btn-example {
            font-size: 0.8rem;
            margin-top: 5px;
        }

```
**[ADDED]**
```
18            .spinner-border { width: 3rem; height: 3rem; }
19            .json-example-btn { font-size: 0.85rem; }
20            textarea { font-family: 'Courier New', monospace; font-size: 0.9rem; }
21            .alert-info { font-size: 0.9rem; }
```
**[REMOVED]**
```
(from line ~26)
<!-- Overlay de Carregamento -->
<div id="loading-overlay">
    <div class="spinner-border text-primary spinner-border-lg" role="status">
        <span class="visually-hidden">Processando...</span>
    </div>
    <div class="loading-text">
        <i class="bi bi-cpu-fill"></i> Treinando Modelo...
    </div>
    <p class="text-muted mt-2">Isso pode levar alguns minutos dependendo dos dados e hiperparâmetros.</p>
</div>

```
**[ADDED]**
```
26    <div class="container py-5">
27        <div class="row justify-content-center">
28            <div class="col-lg-10">
29                <h2 class="text-center mb-4">🤖 IA-Trainer: Treinamento Automático</h2>
30                
31                <!-- Alerta de Regra Automática -->
32                <div class="alert alert-info">
33                    <strong>ℹ️ Regra de Colunas:</strong> O sistema considera automaticamente a <strong>última coluna</strong> do seu Excel como <em>Target (y)</em> e todas as <strong>demais colunas</strong> como <em>Features (X)</em>. Certifique-se que seu arquivo esteja nessa ordem.
34                </div>
```
**[REMOVED]**
```
(from line ~36)
<div class="container">
    <h1 class="text-center mb-4">
        <i class="bi bi-robot"></i> IA-Trainer - Interface Web
    </h1>

    {% if error_message %}
    <div class="alert alert-danger alert-dismissible fade show" role="alert">
        <i class="bi bi-exclamation-triangle-fill"></i>
        <strong>Erro:</strong> {{ error_message|linebreaks }}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
    {% endif %}

    {% if training_result %}
    <div class="card result-card mb-4">
        <div class="card-header">
            <i class="bi bi-check-circle-fill"></i> Treinamento Concluído com Sucesso!
        </div>
        <div class="card-body">
            <div class="row">
                <div class="col-md-6">
                    <h5><i class="bi bi-graph-up"></i> Métricas</h5>
                    <ul class="list-group list-group-flush">
                        <li class="list-group-item d-flex justify-content-between">
                            <span>Acurácia (Treino):</span>
                            <strong>{{ training_result.train_accuracy|floatformat:4 }}</strong>
                        </li>
                        <li class="list-group-item d-flex justify-content-between">
                            <span>Acurácia (Teste):</span>
                            <strong>{{ training_result.test_accuracy|floatformat:4 }}</strong>
                        </li>
                        <li class="list-group-item d-flex justify-content-between">
                            <span>Melhor Score CV:</span>
                            <strong>{{ training_result.best_cv_score|floatformat:4 }}</strong>
                        </li>
                        <li class="list-group-item d-flex justify-content-between">
                            <span>Folds:</span>
                            <strong>{{ training_result.cv_folds_used }}</strong>
                        </li>
                        <li class="list-group-item d-flex justify-content-between">
                            <span>Random State:</span>
                            <strong>{{ training_result.random_state_used }}</strong>
                        </li>
                        <li class="list-group-item d-flex justify-content-between">
                            <span>Combinações Testadas:</span>
                            <strong>{{ training_result.n_combinations }}</strong>
                        </li>
                    </ul>
                </div>
                <div class="col-md-6">
                    <h5><i class="bi bi-sliders"></i> Melhores Hiperparâmetros</h5>
                    <div class="border rounded p-3 bg-white" style="max-height: 300px; overflow-y: auto;">
                        {% for key, value in training_result.best_params.items %}
                        <span class="param-badge">{{ key }}: {{ value }}</span>
                        {% endfor %}
                    </div>

                    <hr>

                    <h5><i class="bi bi-download"></i> Download do Modelo</h5>
                    <a href="{% url 'download_model' training_result.model_filename %}" class="btn btn-success w-100">
                        <i class="bi bi-file-earmark-arrow-down"></i> Baixar {{ training_result.model_filename }}
                    </a>
                </div>

```
**[ADDED]**
```
36                {% if error_message %}
37                <div class="alert alert-danger alert-dismissible fade show" role="alert">
38                    {{ error_message|safe }}
39                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
```
**[REMOVED]**
```
(from line ~41)
        </div>
    </div>
    {% endif %}

```
**[ADDED]**
```
41                {% endif %}
```
**[REMOVED]**
```
(from line ~43)
    <form method="post" enctype="multipart/form-data" id="training-form">
        {% csrf_token %}

        <!-- Upload e Seleção de Colunas -->
        <div class="card">
            <div class="card-header">
                <i class="bi bi-file-earmark-spreadsheet"></i> 1. Dados e Colunas

```
**[ADDED]**
```
43                {% if training_result %}
44                <div class="alert alert-success">
45                    <h4>✅ Treinamento Concluído!</h4>
46                    <p><strong>Acurácia (Treino):</strong> {{ training_result.train_accuracy|floatformat:4 }}</p>
47                    <p><strong>Acurácia (Teste):</strong> {{ training_result.test_accuracy|floatformat:4 }}</p>
48                    <p><strong>Melhor Score (CV):</strong> {{ training_result.best_cv_score|floatformat:4 }}</p>
49                    <p><strong>Parâmetros:</strong> {{ training_result.best_params }}</p>
50                    <hr>
51                    <a href="{% url 'download_model' training_result.model_filename %}" class="btn btn-success">📥 Baixar Modelo (.pkl)</a>
```
**[REMOVED]**
```
(from line ~53)
            <div class="card-body">
                <div class="mb-3">
                    <label for="{{ form.excel_file.id_for_label }}" class="form-label">
                        {{ form.excel_file.label }}
                    </label>
                    {{ form.excel_file }}
                    <small class="help-text d-block">{{ form.excel_file.help_text }}</small>
                    {% if form.excel_file.errors %}
                        <div class="text-danger">{{ form.excel_file.errors }}</div>
                    {% endif %}
                </div>

```
**[ADDED]**
```
53                {% endif %}
```
**[REMOVED]**
```
(from line ~55)
                <div class="row">
                    <div class="col-md-6">

```
**[ADDED]**
```
55                <form method="post" enctype="multipart/form-data" id="trainForm">
56                    {% csrf_token %}
57                    
58                    <!-- Upload -->
59                    <div class="card">
60                        <div class="card-header">1. Dados</div>
61                        <div class="card-body">
```
**[REMOVED]**
```
(from line ~63)
                            <label for="{{ form.feature_columns.id_for_label }}" class="form-label">
                                {{ form.feature_columns.label }}
                            </label>
                            {{ form.feature_columns }}
                            <small class="help-text d-block">{{ form.feature_columns.help_text }}</small>
                            {% if form.feature_columns.errors %}
                                <div class="text-danger">{{ form.feature_columns.errors }}</div>
                            {% endif %}

```
**[ADDED]**
```
63                                <label for="excel_file" class="form-label">Arquivo Excel (.xlsx)</label>
64                                <input type="file" class="form-control" id="excel_file" name="excel_file" accept=".xlsx" required>
```
**[REMOVED]**
```
(from line ~67)
                    <div class="col-md-6">
                        <div class="mb-3">
                            <label for="{{ form.target_column.id_for_label }}" class="form-label">
                                {{ form.target_column.label }}
                            </label>
                            {{ form.target_column }}
                            <small class="help-text d-block">{{ form.target_column.help_text }}</small>
                            {% if form.target_column.errors %}
                                <div class="text-danger">{{ form.target_column.errors }}</div>
                            {% endif %}
                        </div>
                    </div>

```
**[REMOVED]**
```
(from line ~68)
            </div>
        </div>

```
**[REMOVED]**
```
(from line ~69)
        <!-- Validação Cruzada e Reprodutibilidade -->
        <div class="card">
            <div class="card-header">
                <i class="bi bi-shuffle"></i> 2. Validação Cruzada e Reprodutibilidade
            </div>
            <div class="card-body">
                <div class="row">
                    <div class="col-md-6">
                        <div class="mb-3">
                            <label for="{{ form.cv_folds.id_for_label }}" class="form-label">
                                {{ form.cv_folds.label }}
                            </label>
                            {{ form.cv_folds }}
                            <small class="help-text d-block">{{ form.cv_folds.help_text }}</small>
                            {% if form.cv_folds.errors %}
                                <div class="text-danger">{{ form.cv_folds.errors }}</div>
                            {% endif %}

```
**[ADDED]**
```
69                    <!-- Configurações Globais -->
70                    <div class="card">
71                        <div class="card-header">2. Validação e Reprodutibilidade</div>
72                        <div class="card-body row">
73                            <div class="col-md-6 mb-3">
74                                <label for="cv_folds" class="form-label">Folds (Validação Cruzada)</label>
75                                <input type="number" class="form-control" id="cv_folds" name="cv_folds" value="5" min="2" max="20" required>
```
**[REMOVED]**
```
(from line ~77)
                    </div>
                    <div class="col-md-6">
                        <div class="mb-3">
                            <label for="{{ form.random_state.id_for_label }}" class="form-label">
                                {{ form.random_state.label }}
                            </label>
                            {{ form.random_state }}
                            <small class="help-text d-block">{{ form.random_state.help_text }}</small>
                            {% if form.random_state.errors %}
                                <div class="text-danger">{{ form.random_state.errors }}</div>
                            {% endif %}

```
**[ADDED]**
```
77                            <div class="col-md-6 mb-3">
78                                <label for="random_state" class="form-label">Random State (Semente)</label>
79                                <input type="number" class="form-control" id="random_state" name="random_state" value="42" required>
```
**[REMOVED]**
```
(from line ~83)
            </div>
        </div>

```
**[REMOVED]**
```
(from line ~84)
        <!-- Configuração de Hiperparâmetros -->
        <div class="card">
            <div class="card-header">
                <i class="bi bi-gear-fill"></i> 3. Configuração de Hiperparâmetros (JSON)
            </div>
            <div class="card-body">
                <div class="mb-3">
                    <label for="{{ form.hyperparameters_json.id_for_label }}" class="form-label">
                        {{ form.hyperparameters_json.label }}
                    </label>
                    {{ form.hyperparameters_json }}
                    <small class="help-text d-block">{{ form.hyperparameters_json.help_text }}</small>
                    {% if form.hyperparameters_json.errors %}
                        <div class="text-danger">{{ form.hyperparameters_json.errors }}</div>
                    {% endif %}

                    <button type="button" class="btn btn-outline-secondary btn-example" id="btn-fill-example">
                        <i class="bi bi-magic"></i> Preencher Exemplo
                    </button>
                </div>
            </div>
        </div>

        <!-- Botão de Submit -->
        <div class="d-grid gap-2">
            <button type="submit" class="btn btn-primary btn-lg" id="btn-submit">
                <i class="bi bi-play-fill"></i> Iniciar Treinamento
            </button>
        </div>
    </form>
</div>

<!-- Bootstrap 5 JS Bundle -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const excelInput = document.getElementById('{{ form.excel_file.id_for_label }}');
    const featureSelect = document.getElementById('{{ form.feature_columns.id_for_label }}');
    const targetSelect = document.getElementById('{{ form.target_column.id_for_label }}');
    const loadingOverlay = document.getElementById('loading-overlay');
    const trainingForm = document.getElementById('training-form');
    const btnSubmit = document.getElementById('btn-submit');
    const btnExample = document.getElementById('btn-fill-example');
    const hyperparamsTextarea = document.getElementById('{{ form.hyperparameters_json.id_for_label }}');

    // Exemplo de configuração JSON
    const exampleJson = `{

```
**[ADDED]**
```
84                    <!-- Hiperparâmetros JSON -->
85                    <div class="card">
86                        <div class="card-header">3. Configuração do Pipeline (JSON)</div>
87                        <div class="card-body">
88                            <div class="d-flex justify-content-end mb-2">
89                                <button type="button" class="btn btn-sm btn-outline-secondary json-example-btn" onclick="fillExample()">Preencher Exemplo</button>
90                            </div>
91                            <div class="mb-3">
92                                <label for="hyperparameters_json" class="form-label">Hiperparâmetros</label>
93                                <textarea class="form-control" id="hyperparameters_json" name="hyperparameters_json" rows="12" required>{
```
**[REMOVED]**
```
(from line ~101)
        "params": {
            "n_components": 0.95
        }

```
**[ADDED]**
```
101           "params": {"n_components": 0.95}
```
**[REMOVED]**
```
(from line ~107)
            "hidden_layer_sizes": [(24,), (32,)],

```
**[ADDED]**
```
107               "hidden_layer_sizes": [[24], [32]],
```
**[REMOVED]**
```
(from line ~109)
            "learning_rate_init": [0.01, 0.015],

```
**[REMOVED]**
```
(from line ~112)
}`;

    // Botão de exemplo JSON
    btnExample.addEventListener('click', function() {
        hyperparamsTextarea.value = exampleJson;
    });

    // Extrair colunas ao fazer upload do Excel
    excelInput.addEventListener('change', function() {
        if (this.files && this.files[0]) {
            const formData = new FormData();
            formData.append('excel_file', this.files[0]);

            fetch('{% url "extract_columns" %}?excel_file=' + encodeURIComponent(this.files[0].name), {
                method: 'GET',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    populateSelects(data.columns);
                } else {
                    alert('Erro ao extrair colunas: ' + data.error);
                }
            })
            .catch(error => {
                console.error('Erro:', error);
                // Fallback: tentar extrair via AJAX com o arquivo
                extractColumnsAjax(this.files[0]);
            });
        }
    });

    // Função alternativa para extrair colunas via POST com arquivo
    function extractColumnsAjax(file) {
        const formData = new FormData();
        formData.append('excel_file', file);

        fetch('{% url "extract_columns" %}', {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': getCookie('csrftoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                populateSelects(data.columns);
            } else {
                alert('Erro ao extrair colunas: ' + data.error);
            }
        })
        .catch(error => {
            console.error('Erro:', error);
            alert('Não foi possível extrair as colunas automaticamente. Selecione manualmente.');
        });
    }

    function populateSelects(columns) {
        // Limpa opções existentes
        featureSelect.innerHTML = '';
        targetSelect.innerHTML = '';

        // Adiciona novas opções
        columns.forEach(col => {
            const optionFeature = document.createElement('option');
            optionFeature.value = col;
            optionFeature.textContent = col;
            featureSelect.appendChild(optionFeature);

            const optionTarget = document.createElement('option');
            optionTarget.value = col;
            optionTarget.textContent = col;
            targetSelect.appendChild(optionTarget);
        });

        // Seleciona automaticamente a última coluna como target (comum em datasets)
        if (columns.length > 0) {
            targetSelect.value = columns[columns.length - 1];
        }
    }

    // Submit do formulário com overlay
    trainingForm.addEventListener('submit', function(e) {
        // Valida se há colunas selecionadas
        if (featureSelect.selectedOptions.length === 0) {
            e.preventDefault();
            alert('Por favor, selecione pelo menos uma coluna feature.');
            return;
        }

        if (!targetSelect.value) {
            e.preventDefault();
            alert('Por favor, selecione uma coluna target.');
            return;
        }

        // Mostra overlay e desabilita formulário
        loadingOverlay.classList.add('active');
        btnSubmit.disabled = true;
        btnSubmit.innerHTML = '<i class="bi bi-hourglass-split"></i> Processando...';

        // Permite o submit continuar
        // e.preventDefault() NÃO é chamado aqui
    });

    // Função para pegar CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
</script>

</body>
</html>


+++ ml_interface/templates/ml_interface/train.html (修改后)
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IA-Trainer - Interface Web Django</title>

    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Bootstrap Icons -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css" rel="stylesheet">

    <style>
        body {
            background-color: #f8f9fa;
        }
        .container {
            max-width: 1200px;
            margin-top: 30px;
            margin-bottom: 50px;
        }
        .card {
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border: none;
            margin-bottom: 20px;
        }
        .card-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            font-weight: bold;
        }
        .form-label {
            font-weight: 500;
            color: #495057;
        }
        .help-text {
            font-size: 0.85rem;
            color: #6c757d;
        }

        /* Overlay de carregamento */
        #loading-overlay {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(255, 255, 255, 0.9);
            z-index: 9999;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }
        #loading-overlay.active {
            display: flex;
        }
        .spinner-border-lg {
            width: 5rem;
            height: 5rem;
        }
        .loading-text {
            margin-top: 20px;
            font-size: 1.2rem;
            color: #667eea;
            font-weight: bold;
        }

        /* Resultados */
        .result-card {
            background-color: #e8f5e9;
            border-left: 5px solid #4caf50;
        }
        .error-card {
            background-color: #ffebee;
            border-left: 5px solid #f44336;
        }
        .param-badge {
            background-color: #667eea;
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
            margin: 3px;
            display: inline-block;
        }

        /* Botão de exemplo JSON */
        .btn-example {
            font-size: 0.8rem;
            margin-top: 5px;
        }
    </style>
</head>
<body>

<!-- Overlay de Carregamento -->
<div id="loading-overlay">
    <div class="spinner-border text-primary spinner-border-lg" role="status">
        <span class="visually-hidden">Processando...</span>
    </div>
    <div class="loading-text">
        <i class="bi bi-cpu-fill"></i> Treinando Modelo...
    </div>
    <p class="text-muted mt-2">Isso pode levar alguns minutos dependendo dos dados e hiperparâmetros.</p>
</div>

<div class="container">
    <h1 class="text-center mb-4">
        <i class="bi bi-robot"></i> IA-Trainer - Interface Web
    </h1>

    {% if error_message %}
    <div class="alert alert-danger alert-dismissible fade show" role="alert">
        <i class="bi bi-exclamation-triangle-fill"></i>
        <strong>Erro:</strong> {{ error_message|linebreaks }}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
    {% endif %}

    {% if training_result %}
    <div class="card result-card mb-4">
        <div class="card-header">
            <i class="bi bi-check-circle-fill"></i> Treinamento Concluído com Sucesso!
        </div>
        <div class="card-body">
            <div class="row">
                <div class="col-md-6">
                    <h5><i class="bi bi-graph-up"></i> Métricas</h5>
                    <ul class="list-group list-group-flush">
                        <li class="list-group-item d-flex justify-content-between">
                            <span>Acurácia (Treino):</span>
                            <strong>{{ training_result.train_accuracy|floatformat:4 }}</strong>
                        </li>
                        <li class="list-group-item d-flex justify-content-between">
                            <span>Acurácia (Teste):</span>
                            <strong>{{ training_result.test_accuracy|floatformat:4 }}</strong>
                        </li>
                        <li class="list-group-item d-flex justify-content-between">
                            <span>Melhor Score CV:</span>
                            <strong>{{ training_result.best_cv_score|floatformat:4 }}</strong>
                        </li>
                        <li class="list-group-item d-flex justify-content-between">
                            <span>Folds:</span>
                            <strong>{{ training_result.cv_folds_used }}</strong>
                        </li>
                        <li class="list-group-item d-flex justify-content-between">
                            <span>Random State:</span>
                            <strong>{{ training_result.random_state_used }}</strong>
                        </li>
                        <li class="list-group-item d-flex justify-content-between">
                            <span>Combinações Testadas:</span>
                            <strong>{{ training_result.n_combinations }}</strong>
                        </li>
                        <li class="list-group-item d-flex justify-content-between">
                            <span>Amostras:</span>
                            <strong>{{ training_result.n_samples }}</strong>
                        </li>
                        <li class="list-group-item d-flex justify-content-between">
                            <span>Features:</span>
                            <strong>{{ training_result.n_features }}</strong>
                        </li>
                    </ul>
                    <div class="mt-3">
                        <small><strong>Features:</strong> {{ training_result.feature_columns|join:", " }}</small><br>
                        <small><strong>Target:</strong> {{ training_result.target_column }}</small>

```
**[ADDED]**
```
112   }</textarea>
113                               <div class="form-text">Defina scaler, pca (opcional) e classifier. Use listas [] em vez de tuplas ().</div>
114                           </div>
```
**[REMOVED]**
```
(from line ~117)
                <div class="col-md-6">
                    <h5><i class="bi bi-sliders"></i> Melhores Hiperparâmetros</h5>
                    <div class="border rounded p-3 bg-white" style="max-height: 300px; overflow-y: auto;">
                        {% for key, value in training_result.best_params.items %}
                        <span class="param-badge">{{ key }}: {{ value }}</span>
                        {% endfor %}
                    </div>

```
**[REMOVED]**
```
(from line ~118)
                    <hr>

                    <h5><i class="bi bi-download"></i> Download do Modelo</h5>
                    <a href="{% url 'download_model' training_result.model_filename %}" class="btn btn-success w-100">
                        <i class="bi bi-file-earmark-arrow-down"></i> Baixar {{ training_result.model_filename }}
                    </a>

```
**[ADDED]**
```
118                   <div class="d-grid gap-2">
119                       <button type="submit" class="btn btn-primary btn-lg">🚀 Iniciar Treinamento</button>
```
**[REMOVED]**
```
(from line ~121)
            </div>

```
**[ADDED]**
```
121               </form>
```
**[REMOVED]**
```
(from line ~124)
    {% endif %}

```
**[ADDED]**
```
124   </div>
```
**[REMOVED]**
```
(from line ~126)
    <form method="post" enctype="multipart/form-data" id="training-form">
        {% csrf_token %}

        <!-- Upload do Arquivo Excel -->
        <div class="card">
            <div class="card-header">
                <i class="bi bi-file-earmark-spreadsheet"></i> 1. Upload do Arquivo Excel
            </div>
            <div class="card-body">
                <div class="mb-3">
                    <label for="{{ form.excel_file.id_for_label }}" class="form-label">
                        {{ form.excel_file.label }}
                    </label>
                    {{ form.excel_file }}
                    <small class="help-text d-block">{{ form.excel_file.help_text }}</small>
                    {% if form.excel_file.errors %}
                        <div class="text-danger">{{ form.excel_file.errors }}</div>
                    {% endif %}
                </div>

                <div class="alert alert-info">
                    <i class="bi bi-info-circle-fill"></i>
                    <strong>Regra Automática:</strong> A última coluna do seu arquivo Excel será usada como <strong>Target (y)</strong>,
                    e todas as colunas anteriores serão usadas como <strong>Features (X)</strong>.
                </div>
            </div>
        </div>

        <!-- Validação Cruzada e Reprodutibilidade -->
        <div class="card">
            <div class="card-header">
                <i class="bi bi-shuffle"></i> 2. Validação Cruzada e Reprodutibilidade
            </div>
            <div class="card-body">
                <div class="row">
                    <div class="col-md-6">
                        <div class="mb-3">
                            <label for="{{ form.cv_folds.id_for_label }}" class="form-label">
                                {{ form.cv_folds.label }}
                            </label>
                            {{ form.cv_folds }}
                            <small class="help-text d-block">{{ form.cv_folds.help_text }}</small>
                            {% if form.cv_folds.errors %}
                                <div class="text-danger">{{ form.cv_folds.errors }}</div>
                            {% endif %}
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="mb-3">
                            <label for="{{ form.random_state.id_for_label }}" class="form-label">
                                {{ form.random_state.label }}
                            </label>
                            {{ form.random_state }}
                            <small class="help-text d-block">{{ form.random_state.help_text }}</small>
                            {% if form.random_state.errors %}
                                <div class="text-danger">{{ form.random_state.errors }}</div>
                            {% endif %}
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Configuração de Hiperparâmetros -->
        <div class="card">
            <div class="card-header">
                <i class="bi bi-gear-fill"></i> 3. Configuração de Hiperparâmetros (JSON)
            </div>
            <div class="card-body">
                <div class="mb-3">
                    <label for="{{ form.hyperparameters_json.id_for_label }}" class="form-label">
                        {{ form.hyperparameters_json.label }}
                    </label>
                    {{ form.hyperparameters_json }}
                    <small class="help-text d-block">{{ form.hyperparameters_json.help_text }}</small>
                    {% if form.hyperparameters_json.errors %}
                        <div class="text-danger">{{ form.hyperparameters_json.errors }}</div>
                    {% endif %}

                    <button type="button" class="btn btn-outline-secondary btn-example" id="btn-fill-example">
                        <i class="bi bi-magic"></i> Preencher Exemplo
                    </button>
                </div>
            </div>
        </div>

        <!-- Botão de Submit -->
        <div class="d-grid gap-2">
            <button type="submit" class="btn btn-primary btn-lg" id="btn-submit">
                <i class="bi bi-play-fill"></i> Iniciar Treinamento
            </button>
        </div>
    </form>

```
**[ADDED]**
```
126   <!-- Overlay de Loading -->
127   <div class="loading-overlay" id="loadingOverlay">
128       <div class="spinner-border text-primary" role="status"></div>
129       <h5 class="mt-3">Processando...</h5>
130       <p class="text-muted">O treinamento pode levar alguns minutos.</p>
```
**[REMOVED]**
```
(from line ~133)
<!-- Bootstrap 5 JS Bundle -->

```
**[REMOVED]**
```
(from line ~134)


```
**[REMOVED]**
```
(from line ~135)
document.addEventListener('DOMContentLoaded', function() {
    const loadingOverlay = document.getElementById('loading-overlay');
    const trainingForm = document.getElementById('training-form');
    const btnSubmit = document.getElementById('btn-submit');
    const btnExample = document.getElementById('btn-fill-example');
    const hyperparamsTextarea = document.getElementById('{{ form.hyperparameters_json.id_for_label }}');

    // Exemplo de configuração JSON (CORRIGIDO: usa listas em vez de tuplas)
    const exampleJson = `{

```
**[ADDED]**
```
135       // Função para preencher exemplo
136       function fillExample() {
137           const example = `{
```
**[REMOVED]**
```
(from line ~145)
        "params": {
            "n_components": 0.95
        }

```
**[ADDED]**
```
145           "params": {"n_components": 0.95}
```
**[REMOVED]**
```
(from line ~153)
            "learning_rate_init": [0.01, 0.015],

```
**[ADDED]**
```
157           document.getElementById('hyperparameters_json').value = example;
158       }
```
**[REMOVED]**
```
(from line ~160)
    // Botão de exemplo JSON
    btnExample.addEventListener('click', function() {
        hyperparamsTextarea.value = exampleJson;
    });

```
**[ADDED]**
```
160       // Gerenciamento do Loading Overlay
161       document.getElementById('trainForm').addEventListener('submit', function(e) {
162           // Validação simples de JSON antes de enviar
163           const jsonField = document.getElementById('hyperparameters_json');
164           try {
165               JSON.parse(jsonField.value);
166           } catch (e) {
167               e.preventDefault();
168               alert('Erro: O campo de hiperparâmetros contém um JSON inválido.');
169               return;
170           }
```
**[REMOVED]**
```
(from line ~172)
    // Submit do formulário com overlay
    trainingForm.addEventListener('submit', function(e) {
        // Mostra overlay e desabilita formulário
        loadingOverlay.classList.add('active');
        btnSubmit.disabled = true;
        btnSubmit.innerHTML = '<i class="bi bi-hourglass-split"></i> Processando...';

        // Permite o submit continuar (não chama e.preventDefault())

```
**[ADDED]**
```
172           // Mostra overlay e desabilita botão
173           document.getElementById('loadingOverlay').style.display = 'flex';
174           const submitBtn = this.querySelector('button[type="submit"]');
175           submitBtn.disabled = true;
176           submitBtn.innerText = 'Treinando...';
```
**[REMOVED]**
```
(from line ~178)

    // Função utilitária para pegar CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});

```
**[REMOVED]**
```
(from line ~181)
</html>

```
**[ADDED]**
```
181   </html>
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/ml_interface/views.py
*Saved at: 28/08/2026, 15:42:03*

**[REMOVED]**
```
(from line ~1)
--- ml_interface/views.py (原始)

```
**[REMOVED]**
```
(from line ~8)
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.http import require_POST, require_GET
from django.core.files.storage import default_storage

import pandas as pd
from sklearn.model_selection import train_test_split

from .forms import TrainingForm
from .utils.cleanup import cleanup_old_models
from .utils.dynamic_trainer import DynamicTrainer


@require_GET
def extract_columns(request):
    """
    View AJAX para extrair colunas de um arquivo Excel enviado.
    Usada para popular dinamicamente os selects de features e target.
    """
    if request.method == 'GET' and request.FILES.get('excel_file'):
        try:
            excel_file = request.FILES['excel_file']

            # Lê apenas as primeiras linhas para pegar os cabeçalhos
            df = pd.read_excel(excel_file, nrows=5)
            columns = df.columns.tolist()

            return JsonResponse({
                'success': True,
                'columns': columns
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=400)

    return JsonResponse({
        'success': False,
        'error': 'Nenhum arquivo enviado'
    }, status=400)


def train_view(request):
    """
    View principal que renderiza o formulário e processa o treinamento.
    """
    form = TrainingForm()
    context = {
        'form': form,
        'training_result': None,
        'error_message': None
    }

    if request.method == 'POST':
        form = TrainingForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                # 1. Cleanup dos modelos antigos
                cleanup_old_models()

                # 2. Extrai dados do formulário
                excel_file = request.FILES['excel_file']
                feature_columns = form.cleaned_data['feature_columns']
                target_column = form.cleaned_data['target_column']
                cv_folds = form.cleaned_data['cv_folds']
                random_state = form.cleaned_data['random_state']
                hyperparams_json = form.cleaned_data['hyperparameters_json']

                # 3. Parse da configuração JSON
                config = json.loads(hyperparams_json)

                # 4. Salva arquivo temporariamente e carrega dados
                with tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx') as tmp_file:
                    for chunk in excel_file.chunks():
                        tmp_file.write(chunk)
                    tmp_path = tmp_file.name

                try:
                    # Carrega o DataFrame
                    df = pd.read_excel(tmp_path)

                    # Separa features e target
                    X = df[feature_columns].values
                    y = df[target_column].values

                    # 5. Split dos dados com random_state controlado
                    X_train, X_test, y_train, y_test = train_test_split(
                        X, y,
                        test_size=0.2,
                        random_state=random_state,
                        stratify=y
                    )

                    # 6. Treina o modelo
                    trainer = DynamicTrainer(metric_focus='f1_score')
                    grid_search = trainer.train(
                        X_train=X_train,
                        y_train=y_train,
                        config=config,
                        cv_folds=cv_folds,
                        random_state=random_state
                    )

                    # 7. Avalia no conjunto de teste
                    train_score = grid_search.score(X_train, y_train)
                    test_score = grid_search.score(X_test, y_test)
                    best_params = grid_search.best_params_
                    best_cv_score = grid_search.best_score_

                    # 8. Salva o modelo
                    model_filename = f"modelo_treinado_rs{random_state}.pkl"
                    model_path = trainer.save_model(grid_search, model_filename)

                    # Prepara resultado
                    context['training_result'] = {
                        'success': True,
                        'model_path': model_path,
                        'model_filename': model_filename,
                        'train_accuracy': float(train_score),
                        'test_accuracy': float(test_score),
                        'best_cv_score': float(best_cv_score),
                        'best_params': best_params,
                        'cv_folds_used': cv_folds,
                        'random_state_used': random_state,
                        'n_combinations': len(grid_search.cv_results_['params']),
                    }

                finally:
                    # Remove arquivo temporário
                    if os.path.exists(tmp_path):
                        os.remove(tmp_path)

            except json.JSONDecodeError as e:
                context['error_message'] = f"Erro ao parsear JSON de hiperparâmetros: {str(e)}"
            except Exception as e:
                context['error_message'] = f"Erro durante o treinamento: {str(e)}\n\n{traceback.format_exc()}"
        else:
            context['error_message'] = "Erro de validação no formulário. Verifique os campos."

    return render(request, 'ml_interface/train.html', context)


def download_model(request, filename):
    """
    View para download do modelo treinado.
    """
    from django.http import FileResponse, Http404

    model_path = os.path.join(settings.MEDIA_ROOT, 'modelos_treinados', filename)

    if os.path.exists(model_path):
        response = FileResponse(open(model_path, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response
    else:
        raise Http404("Modelo não encontrado.")


+++ ml_interface/views.py (修改后)
"""
Views para a interface de treinamento de ML.
"""
import json
import os
import tempfile
import traceback

```
**[REMOVED]**
```
(from line ~12)
from django.views.decorators.http import require_POST, require_GET

```
**[ADDED]**
```
12    from django.views.decorators.http import require_POST
```
**[REMOVED]**
```
(from line ~29)
    Usada para popular dinamicamente os selects de features e target.

```
**[ADDED]**
```
29        (Mantida por compatibilidade, embora não seja mais usada na lógica automática)
```
**[REMOVED]**
```
(from line ~33)


```
**[ADDED]**
```
33            
```
**[REMOVED]**
```
(from line ~39)


```
**[ADDED]**
```
39            
```
**[REMOVED]**
```
(from line ~43)


```
**[ADDED]**
```
43            
```
**[REMOVED]**
```
(from line ~58)
    Regra: Última coluna do Excel é sempre o Target (y), demais são Features (X).

```
**[ADDED]**
```
58        Regra de Negócio: A última coluna é sempre o Target (y), as demais são Features (X).
```
**[REMOVED]**
```
(from line ~66)


```
**[ADDED]**
```
66        
```
**[REMOVED]**
```
(from line ~69)


```
**[ADDED]**
```
69            
```
**[REMOVED]**
```
(from line ~74)


```
**[ADDED]**
```
74                    
```
**[REMOVED]**
```
(from line ~80)


```
**[ADDED]**
```
80                    
```
**[REMOVED]**
```
(from line ~82)
                config = json.loads(hyperparams_json)


```
**[ADDED]**
```
82                    try:
83                        config = json.loads(hyperparams_json)
84                    except json.JSONDecodeError as e:
85                        raise ValueError(f"JSON inválido: {str(e)}")
86                    
```
**[REMOVED]**
```
(from line ~92)


```
**[ADDED]**
```
92                    
```
**[REMOVED]**
```
(from line ~96)

                    # REGRA AUTOMÁTICA: Última coluna = target, demais = features

```
**[ADDED]**
```
96                        
97                        # REGRA AUTOMÁTICA: Última coluna = Target, Resto = Features
```
**[ADDED]**
```
99                        if len(all_columns) < 2:
100                           raise ValueError("O arquivo deve ter pelo menos 2 colunas (uma feature e uma target).")
101                       
```
**[REMOVED]**
```
(from line ~104)

                    logger.info(f"Colunas features (automáticas): {feature_columns}")
                    logger.info(f"Coluna target (automática): {target_column}")


```
**[ADDED]**
```
104                       
105                       logger.info(f"Features detectadas: {feature_columns}")
106                       logger.info(f"Target detectada: {target_column}")
107                       
```
**[ADDED]**
```
111                       
112                       # Tratamento básico de valores faltantes (opcional, mas recomendado)
113                       # Se houver NaNs, o treino falhará. Aqui preenchemos com a média/moda se necessário.
114                       # Para simplicidade, assumimos dados limpos ou levantamos erro.
115                       if pd.isnull(X).any() or pd.isnull(y).any():
116                            # Estratégia simples: remover linhas com NaN
117                            df_clean = df.dropna()
118                            X = df_clean[feature_columns].values
119                            y = df_clean[target_column].values
120                            logger.warning("Linhas com valores nulos foram removidas.")
```
**[REMOVED]**
```
(from line ~123)
                    X_train, X_test, y_train, y_test = train_test_split(
                        X, y,
                        test_size=0.2,
                        random_state=random_state,
                        stratify=y
                    )


```
**[ADDED]**
```
123                       # Nota: stratify=y pode falhar se y tiver classes com apenas 1 exemplo após dropna.
124                       # Adicionamos um try-except para fallback sem stratify se necessário.
125                       try:
126                           X_train, X_test, y_train, y_test = train_test_split(
127                               X, y, 
128                               test_size=0.2, 
129                               random_state=random_state, 
130                               stratify=y
131                           )
132                       except ValueError:
133                           logger.warning("Stratify falhou (classes minoritárias pequenas). Tentando sem stratify.")
134                           X_train, X_test, y_train, y_test = train_test_split(
135                               X, y, 
136                               test_size=0.2, 
137                               random_state=random_state
138                           )
139                       
```
**[REMOVED]**
```
(from line ~149)


```
**[ADDED]**
```
149                       
```
**[REMOVED]**
```
(from line ~155)


```
**[ADDED]**
```
155                       
```
**[REMOVED]**
```
(from line ~159)


```
**[ADDED]**
```
159                       
```
**[REMOVED]**
```
(from line ~172)
                        'feature_columns': feature_columns,
                        'target_column': target_column,
                        'n_samples': len(df),
                        'n_features': len(feature_columns),

```
**[ADDED]**
```
172                           'features_used': feature_columns,
173                           'target_used': target_column
```
**[REMOVED]**
```
(from line ~175)


```
**[ADDED]**
```
175                       
```
**[REMOVED]**
```
(from line ~180)

            except json.JSONDecodeError as e:
                context['error_message'] = f"Erro ao parsear JSON de hiperparâmetros: {str(e)}"

```
**[ADDED]**
```
180                   
181               except ValueError as ve:
182                   context['error_message'] = f"Erro de Dados/Configuração: {str(ve)}"
```
**[ADDED]**
```
185                   logger.error(traceback.format_exc())
```
**[REMOVED]**
```
(from line ~190)
                field_label = form.fields.get(field_name, {}).label if hasattr(form.fields.get(field_name), 'label') else field_name

```
**[ADDED]**
```
190                   # Tenta pegar o label legível, senão usa o nome do campo
191                   field_obj = form.fields.get(field_name)
192                   label = field_obj.label if field_obj and hasattr(field_obj, 'label') else field_name.replace('_', ' ').title()
193                   
```
**[REMOVED]**
```
(from line ~195)
                    error_details.append(f"<strong>{field_label}:</strong> {error}")


```
**[ADDED]**
```
195                       error_details.append(f"<strong>{label}:</strong> {error}")
196               
```
**[REMOVED]**
```
(from line ~199)


```
**[ADDED]**
```
199               
```
**[REMOVED]**
```
(from line ~202)


```
**[ADDED]**
```
202       
```
**[REMOVED]**
```
(from line ~211)


```
**[ADDED]**
```
211       
```
**[REMOVED]**
```
(from line ~213)


```
**[ADDED]**
```
213       
```
**[REMOVED]**
```
(from line ~219)
        raise Http404("Modelo não encontrado.")

```
**[ADDED]**
```
219           raise Http404("Modelo não encontrado.")
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/ml_interface/views.py
*Saved at: 28/08/2026, 15:39:34*

**[ADDED]**
```
1     --- ml_interface/views.py (原始)
```
**[ADDED]**
```
9     from django.shortcuts import render, redirect
10    from django.http import JsonResponse
11    from django.conf import settings
12    from django.views.decorators.http import require_POST, require_GET
13    from django.core.files.storage import default_storage
14    
15    import pandas as pd
16    from sklearn.model_selection import train_test_split
17    
18    from .forms import TrainingForm
19    from .utils.cleanup import cleanup_old_models
20    from .utils.dynamic_trainer import DynamicTrainer
21    
22    
23    @require_GET
24    def extract_columns(request):
25        """
26        View AJAX para extrair colunas de um arquivo Excel enviado.
27        Usada para popular dinamicamente os selects de features e target.
28        """
29        if request.method == 'GET' and request.FILES.get('excel_file'):
30            try:
31                excel_file = request.FILES['excel_file']
32    
33                # Lê apenas as primeiras linhas para pegar os cabeçalhos
34                df = pd.read_excel(excel_file, nrows=5)
35                columns = df.columns.tolist()
36    
37                return JsonResponse({
38                    'success': True,
39                    'columns': columns
40                })
41            except Exception as e:
42                return JsonResponse({
43                    'success': False,
44                    'error': str(e)
45                }, status=400)
46    
47        return JsonResponse({
48            'success': False,
49            'error': 'Nenhum arquivo enviado'
50        }, status=400)
51    
52    
53    def train_view(request):
54        """
55        View principal que renderiza o formulário e processa o treinamento.
56        """
57        form = TrainingForm()
58        context = {
59            'form': form,
60            'training_result': None,
61            'error_message': None
62        }
63    
64        if request.method == 'POST':
65            form = TrainingForm(request.POST, request.FILES)
66    
67            if form.is_valid():
68                try:
69                    # 1. Cleanup dos modelos antigos
70                    cleanup_old_models()
71    
72                    # 2. Extrai dados do formulário
73                    excel_file = request.FILES['excel_file']
74                    feature_columns = form.cleaned_data['feature_columns']
75                    target_column = form.cleaned_data['target_column']
76                    cv_folds = form.cleaned_data['cv_folds']
77                    random_state = form.cleaned_data['random_state']
78                    hyperparams_json = form.cleaned_data['hyperparameters_json']
79    
80                    # 3. Parse da configuração JSON
81                    config = json.loads(hyperparams_json)
82    
83                    # 4. Salva arquivo temporariamente e carrega dados
84                    with tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx') as tmp_file:
85                        for chunk in excel_file.chunks():
86                            tmp_file.write(chunk)
87                        tmp_path = tmp_file.name
88    
89                    try:
90                        # Carrega o DataFrame
91                        df = pd.read_excel(tmp_path)
92    
93                        # Separa features e target
94                        X = df[feature_columns].values
95                        y = df[target_column].values
96    
97                        # 5. Split dos dados com random_state controlado
98                        X_train, X_test, y_train, y_test = train_test_split(
99                            X, y,
100                           test_size=0.2,
101                           random_state=random_state,
102                           stratify=y
103                       )
104   
105                       # 6. Treina o modelo
106                       trainer = DynamicTrainer(metric_focus='f1_score')
107                       grid_search = trainer.train(
108                           X_train=X_train,
109                           y_train=y_train,
110                           config=config,
111                           cv_folds=cv_folds,
112                           random_state=random_state
113                       )
114   
115                       # 7. Avalia no conjunto de teste
116                       train_score = grid_search.score(X_train, y_train)
117                       test_score = grid_search.score(X_test, y_test)
118                       best_params = grid_search.best_params_
119                       best_cv_score = grid_search.best_score_
120   
121                       # 8. Salva o modelo
122                       model_filename = f"modelo_treinado_rs{random_state}.pkl"
123                       model_path = trainer.save_model(grid_search, model_filename)
124   
125                       # Prepara resultado
126                       context['training_result'] = {
127                           'success': True,
128                           'model_path': model_path,
129                           'model_filename': model_filename,
130                           'train_accuracy': float(train_score),
131                           'test_accuracy': float(test_score),
132                           'best_cv_score': float(best_cv_score),
133                           'best_params': best_params,
134                           'cv_folds_used': cv_folds,
135                           'random_state_used': random_state,
136                           'n_combinations': len(grid_search.cv_results_['params']),
137                       }
138   
139                   finally:
140                       # Remove arquivo temporário
141                       if os.path.exists(tmp_path):
142                           os.remove(tmp_path)
143   
144               except json.JSONDecodeError as e:
145                   context['error_message'] = f"Erro ao parsear JSON de hiperparâmetros: {str(e)}"
146               except Exception as e:
147                   context['error_message'] = f"Erro durante o treinamento: {str(e)}\n\n{traceback.format_exc()}"
148           else:
149               context['error_message'] = "Erro de validação no formulário. Verifique os campos."
150   
151       return render(request, 'ml_interface/train.html', context)
152   
153   
154   def download_model(request, filename):
155       """
156       View para download do modelo treinado.
157       """
158       from django.http import FileResponse, Http404
159   
160       model_path = os.path.join(settings.MEDIA_ROOT, 'modelos_treinados', filename)
161   
162       if os.path.exists(model_path):
163           response = FileResponse(open(model_path, 'rb'))
164           response['Content-Disposition'] = f'attachment; filename="{filename}"'
165           return response
166       else:
167           raise Http404("Modelo não encontrado.")
168   
169   
170   +++ ml_interface/views.py (修改后)
171   """
172   Views para a interface de treinamento de ML.
173   """
174   import json
175   import os
176   import tempfile
177   import traceback
```
**[REMOVED]**
```
(from line ~203)
        

```
**[ADDED]**
```
203   
```
**[REMOVED]**
```
(from line ~209)
        

```
**[ADDED]**
```
209   
```
**[REMOVED]**
```
(from line ~213)
        

```
**[ADDED]**
```
213   
```
**[ADDED]**
```
228       Regra: Última coluna do Excel é sempre o Target (y), demais são Features (X).
```
**[REMOVED]**
```
(from line ~236)
    

```
**[ADDED]**
```
236   
```
**[REMOVED]**
```
(from line ~239)
        

```
**[ADDED]**
```
239   
```
**[REMOVED]**
```
(from line ~244)
                

```
**[ADDED]**
```
244   
```
**[REMOVED]**
```
(from line ~247)
                feature_columns = form.cleaned_data['feature_columns']
                target_column = form.cleaned_data['target_column']

```
**[REMOVED]**
```
(from line ~250)
                

```
**[ADDED]**
```
250   
```
**[REMOVED]**
```
(from line ~253)
                

```
**[ADDED]**
```
253   
```
**[REMOVED]**
```
(from line ~259)
                

```
**[ADDED]**
```
259   
```
**[REMOVED]**
```
(from line ~263)
                    

```
**[ADDED]**
```
263   
264                       # REGRA AUTOMÁTICA: Última coluna = target, demais = features
265                       all_columns = df.columns.tolist()
266                       feature_columns = all_columns[:-1]  # Todas exceto a última
267                       target_column = all_columns[-1]      # Última coluna
268   
269                       logger.info(f"Colunas features (automáticas): {feature_columns}")
270                       logger.info(f"Coluna target (automática): {target_column}")
271   
```
**[REMOVED]**
```
(from line ~275)
                    

```
**[ADDED]**
```
275   
```
**[REMOVED]**
```
(from line ~278)
                        X, y, 
                        test_size=0.2, 
                        random_state=random_state, 

```
**[ADDED]**
```
278                           X, y,
279                           test_size=0.2,
280                           random_state=random_state,
```
**[REMOVED]**
```
(from line ~283)
                    

```
**[ADDED]**
```
283   
```
**[REMOVED]**
```
(from line ~293)
                    

```
**[ADDED]**
```
293   
```
**[REMOVED]**
```
(from line ~299)
                    

```
**[ADDED]**
```
299   
```
**[REMOVED]**
```
(from line ~303)
                    

```
**[ADDED]**
```
303   
```
**[ADDED]**
```
316                           'feature_columns': feature_columns,
317                           'target_column': target_column,
318                           'n_samples': len(df),
319                           'n_features': len(feature_columns),
```
**[REMOVED]**
```
(from line ~321)
                    

```
**[ADDED]**
```
321   
```
**[REMOVED]**
```
(from line ~326)
                

```
**[ADDED]**
```
326   
```
**[REMOVED]**
```
(from line ~338)
            

```
**[ADDED]**
```
338   
```
**[REMOVED]**
```
(from line ~341)
            

```
**[ADDED]**
```
341   
```
**[REMOVED]**
```
(from line ~344)
    

```
**[ADDED]**
```
344   
```
**[REMOVED]**
```
(from line ~353)
    

```
**[ADDED]**
```
353   
```
**[REMOVED]**
```
(from line ~355)
    

```
**[ADDED]**
```
355   
```
**[REMOVED]**
```
(from line ~361)
        raise Http404("Modelo não encontrado.")
```
**[ADDED]**
```
361           raise Http404("Modelo não encontrado.")
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/ml_interface/templates/ml_interface/train.html
*Saved at: 28/08/2026, 15:39:12*

**[ADDED]**
```
1     --- ml_interface/templates/ml_interface/train.html (原始)
```
**[REMOVED]**
```
(from line ~8)
    

```
**[ADDED]**
```
8     
```
**[REMOVED]**
```
(from line ~13)
    

```
**[ADDED]**
```
13    
```
**[REMOVED]**
```
(from line ~41)
        

```
**[ADDED]**
```
41    
```
**[REMOVED]**
```
(from line ~69)
        

```
**[ADDED]**
```
69    
```
**[REMOVED]**
```
(from line ~87)
        

```
**[ADDED]**
```
87    
```
**[REMOVED]**
```
(from line ~112)
    

```
**[ADDED]**
```
112   
```
**[REMOVED]**
```
(from line ~115)
        <i class="bi bi-exclamation-triangle-fill"></i> 

```
**[ADDED]**
```
115           <i class="bi bi-exclamation-triangle-fill"></i>
```
**[REMOVED]**
```
(from line ~120)
    

```
**[ADDED]**
```
120   
```
**[REMOVED]**
```
(from line ~164)
                    

```
**[ADDED]**
```
164   
```
**[REMOVED]**
```
(from line ~166)
                    

```
**[ADDED]**
```
166   
```
**[REMOVED]**
```
(from line ~176)
    

```
**[ADDED]**
```
176   
```
**[REMOVED]**
```
(from line ~179)
        

```
**[ADDED]**
```
179   
```
**[REMOVED]**
```
(from line ~196)
                

```
**[ADDED]**
```
196   
```
**[REMOVED]**
```
(from line ~225)
        

```
**[ADDED]**
```
225   
```
**[REMOVED]**
```
(from line ~260)
        

```
**[ADDED]**
```
260   
```
**[REMOVED]**
```
(from line ~276)
                    

```
**[ADDED]**
```
276   
```
**[REMOVED]**
```
(from line ~283)
        

```
**[ADDED]**
```
283   
```
**[REMOVED]**
```
(from line ~306)
    

```
**[ADDED]**
```
306   
```
**[REMOVED]**
```
(from line ~331)
    

```
**[ADDED]**
```
331   
```
**[REMOVED]**
```
(from line ~336)
    

```
**[ADDED]**
```
336   
```
**[REMOVED]**
```
(from line ~340)
            extractColumnsAjax(this.files[0]);

```
**[ADDED]**
```
340               const formData = new FormData();
341               formData.append('excel_file', this.files[0]);
342   
343               fetch('{% url "extract_columns" %}?excel_file=' + encodeURIComponent(this.files[0].name), {
344                   method: 'GET',
345                   headers: {
346                       'X-Requested-With': 'XMLHttpRequest'
347                   }
348               })
349               .then(response => response.json())
350               .then(data => {
351                   if (data.success) {
352                       populateSelects(data.columns);
353                   } else {
354                       alert('Erro ao extrair colunas: ' + data.error);
355                   }
356               })
357               .catch(error => {
358                   console.error('Erro:', error);
359                   // Fallback: tentar extrair via AJAX com o arquivo
360                   extractColumnsAjax(this.files[0]);
361               });
```
**[REMOVED]**
```
(from line ~364)
    

```
**[ADDED]**
```
364   
```
**[REMOVED]**
```
(from line ~369)
        

```
**[ADDED]**
```
369   
```
**[REMOVED]**
```
(from line ~378)
        .then(response => {
            if (!response.ok) {
                throw new Error('Erro HTTP: ' + response.status);
            }
            return response.json();
        })

```
**[ADDED]**
```
378           .then(response => response.json())
```
**[REMOVED]**
```
(from line ~388)
            alert('Não foi possível extrair as colunas automaticamente. Selecione manualmente após enviar o formulário.');        

```
**[ADDED]**
```
388               alert('Não foi possível extrair as colunas automaticamente. Selecione manualmente.');
```
**[REMOVED]**
```
(from line ~391)
    

```
**[ADDED]**
```
391   
```
**[REMOVED]**
```
(from line ~396)
        

```
**[ADDED]**
```
396   
```
**[REMOVED]**
```
(from line ~403)
            

```
**[ADDED]**
```
403   
```
**[REMOVED]**
```
(from line ~409)
        

```
**[ADDED]**
```
409   
```
**[REMOVED]**
```
(from line ~415)
    

```
**[ADDED]**
```
415   
```
**[REMOVED]**
```
(from line ~424)
        

```
**[ADDED]**
```
424   
```
**[REMOVED]**
```
(from line ~430)
        

```
**[ADDED]**
```
430   
```
**[REMOVED]**
```
(from line ~435)
        

```
**[ADDED]**
```
435   
```
**[REMOVED]**
```
(from line ~439)
    

```
**[ADDED]**
```
439   
```
**[ADDED]**
```
460   
461   
462   +++ ml_interface/templates/ml_interface/train.html (修改后)
463   <!DOCTYPE html>
464   <html lang="pt-br">
465   <head>
466       <meta charset="UTF-8">
467       <meta name="viewport" content="width=device-width, initial-scale=1.0">
468       <title>IA-Trainer - Interface Web Django</title>
469   
470       <!-- Bootstrap 5 CSS -->
471       <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
472       <!-- Bootstrap Icons -->
473       <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css" rel="stylesheet">
474   
475       <style>
476           body {
477               background-color: #f8f9fa;
478           }
479           .container {
480               max-width: 1200px;
481               margin-top: 30px;
482               margin-bottom: 50px;
483           }
484           .card {
485               box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
486               border: none;
487               margin-bottom: 20px;
488           }
489           .card-header {
490               background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
491               color: white;
492               font-weight: bold;
493           }
494           .form-label {
495               font-weight: 500;
496               color: #495057;
497           }
498           .help-text {
499               font-size: 0.85rem;
500               color: #6c757d;
501           }
502   
503           /* Overlay de carregamento */
504           #loading-overlay {
505               display: none;
506               position: fixed;
507               top: 0;
508               left: 0;
509               width: 100%;
510               height: 100%;
511               background-color: rgba(255, 255, 255, 0.9);
512               z-index: 9999;
513               justify-content: center;
514               align-items: center;
515               flex-direction: column;
516           }
517           #loading-overlay.active {
518               display: flex;
519           }
520           .spinner-border-lg {
521               width: 5rem;
522               height: 5rem;
523           }
524           .loading-text {
525               margin-top: 20px;
526               font-size: 1.2rem;
527               color: #667eea;
528               font-weight: bold;
529           }
530   
531           /* Resultados */
532           .result-card {
533               background-color: #e8f5e9;
534               border-left: 5px solid #4caf50;
535           }
536           .error-card {
537               background-color: #ffebee;
538               border-left: 5px solid #f44336;
539           }
540           .param-badge {
541               background-color: #667eea;
542               color: white;
543               padding: 5px 10px;
544               border-radius: 5px;
545               margin: 3px;
546               display: inline-block;
547           }
548   
549           /* Botão de exemplo JSON */
550           .btn-example {
551               font-size: 0.8rem;
552               margin-top: 5px;
553           }
554       </style>
555   </head>
556   <body>
557   
558   <!-- Overlay de Carregamento -->
559   <div id="loading-overlay">
560       <div class="spinner-border text-primary spinner-border-lg" role="status">
561           <span class="visually-hidden">Processando...</span>
562       </div>
563       <div class="loading-text">
564           <i class="bi bi-cpu-fill"></i> Treinando Modelo...
565       </div>
566       <p class="text-muted mt-2">Isso pode levar alguns minutos dependendo dos dados e hiperparâmetros.</p>
567   </div>
568   
569   <div class="container">
570       <h1 class="text-center mb-4">
571           <i class="bi bi-robot"></i> IA-Trainer - Interface Web
572       </h1>
573   
574       {% if error_message %}
575       <div class="alert alert-danger alert-dismissible fade show" role="alert">
576           <i class="bi bi-exclamation-triangle-fill"></i>
577           <strong>Erro:</strong> {{ error_message|linebreaks }}
578           <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
579       </div>
580       {% endif %}
581   
582       {% if training_result %}
583       <div class="card result-card mb-4">
584           <div class="card-header">
585               <i class="bi bi-check-circle-fill"></i> Treinamento Concluído com Sucesso!
586           </div>
587           <div class="card-body">
588               <div class="row">
589                   <div class="col-md-6">
590                       <h5><i class="bi bi-graph-up"></i> Métricas</h5>
591                       <ul class="list-group list-group-flush">
592                           <li class="list-group-item d-flex justify-content-between">
593                               <span>Acurácia (Treino):</span>
594                               <strong>{{ training_result.train_accuracy|floatformat:4 }}</strong>
595                           </li>
596                           <li class="list-group-item d-flex justify-content-between">
597                               <span>Acurácia (Teste):</span>
598                               <strong>{{ training_result.test_accuracy|floatformat:4 }}</strong>
599                           </li>
600                           <li class="list-group-item d-flex justify-content-between">
601                               <span>Melhor Score CV:</span>
602                               <strong>{{ training_result.best_cv_score|floatformat:4 }}</strong>
603                           </li>
604                           <li class="list-group-item d-flex justify-content-between">
605                               <span>Folds:</span>
606                               <strong>{{ training_result.cv_folds_used }}</strong>
607                           </li>
608                           <li class="list-group-item d-flex justify-content-between">
609                               <span>Random State:</span>
610                               <strong>{{ training_result.random_state_used }}</strong>
611                           </li>
612                           <li class="list-group-item d-flex justify-content-between">
613                               <span>Combinações Testadas:</span>
614                               <strong>{{ training_result.n_combinations }}</strong>
615                           </li>
616                           <li class="list-group-item d-flex justify-content-between">
617                               <span>Amostras:</span>
618                               <strong>{{ training_result.n_samples }}</strong>
619                           </li>
620                           <li class="list-group-item d-flex justify-content-between">
621                               <span>Features:</span>
622                               <strong>{{ training_result.n_features }}</strong>
623                           </li>
624                       </ul>
625                       <div class="mt-3">
626                           <small><strong>Features:</strong> {{ training_result.feature_columns|join:", " }}</small><br>
627                           <small><strong>Target:</strong> {{ training_result.target_column }}</small>
628                       </div>
629                   </div>
630                   <div class="col-md-6">
631                       <h5><i class="bi bi-sliders"></i> Melhores Hiperparâmetros</h5>
632                       <div class="border rounded p-3 bg-white" style="max-height: 300px; overflow-y: auto;">
633                           {% for key, value in training_result.best_params.items %}
634                           <span class="param-badge">{{ key }}: {{ value }}</span>
635                           {% endfor %}
636                       </div>
637   
638                       <hr>
639   
640                       <h5><i class="bi bi-download"></i> Download do Modelo</h5>
641                       <a href="{% url 'download_model' training_result.model_filename %}" class="btn btn-success w-100">
642                           <i class="bi bi-file-earmark-arrow-down"></i> Baixar {{ training_result.model_filename }}
643                       </a>
644                   </div>
645               </div>
646           </div>
647       </div>
648       {% endif %}
649   
650       <form method="post" enctype="multipart/form-data" id="training-form">
651           {% csrf_token %}
652   
653           <!-- Upload do Arquivo Excel -->
654           <div class="card">
655               <div class="card-header">
656                   <i class="bi bi-file-earmark-spreadsheet"></i> 1. Upload do Arquivo Excel
657               </div>
658               <div class="card-body">
659                   <div class="mb-3">
660                       <label for="{{ form.excel_file.id_for_label }}" class="form-label">
661                           {{ form.excel_file.label }}
662                       </label>
663                       {{ form.excel_file }}
664                       <small class="help-text d-block">{{ form.excel_file.help_text }}</small>
665                       {% if form.excel_file.errors %}
666                           <div class="text-danger">{{ form.excel_file.errors }}</div>
667                       {% endif %}
668                   </div>
669   
670                   <div class="alert alert-info">
671                       <i class="bi bi-info-circle-fill"></i>
672                       <strong>Regra Automática:</strong> A última coluna do seu arquivo Excel será usada como <strong>Target (y)</strong>,
673                       e todas as colunas anteriores serão usadas como <strong>Features (X)</strong>.
674                   </div>
675               </div>
676           </div>
677   
678           <!-- Validação Cruzada e Reprodutibilidade -->
679           <div class="card">
680               <div class="card-header">
681                   <i class="bi bi-shuffle"></i> 2. Validação Cruzada e Reprodutibilidade
682               </div>
683               <div class="card-body">
684                   <div class="row">
685                       <div class="col-md-6">
686                           <div class="mb-3">
687                               <label for="{{ form.cv_folds.id_for_label }}" class="form-label">
688                                   {{ form.cv_folds.label }}
689                               </label>
690                               {{ form.cv_folds }}
691                               <small class="help-text d-block">{{ form.cv_folds.help_text }}</small>
692                               {% if form.cv_folds.errors %}
693                                   <div class="text-danger">{{ form.cv_folds.errors }}</div>
694                               {% endif %}
695                           </div>
696                       </div>
697                       <div class="col-md-6">
698                           <div class="mb-3">
699                               <label for="{{ form.random_state.id_for_label }}" class="form-label">
700                                   {{ form.random_state.label }}
701                               </label>
702                               {{ form.random_state }}
703                               <small class="help-text d-block">{{ form.random_state.help_text }}</small>
704                               {% if form.random_state.errors %}
705                                   <div class="text-danger">{{ form.random_state.errors }}</div>
706                               {% endif %}
707                           </div>
708                       </div>
709                   </div>
710               </div>
711           </div>
712   
713           <!-- Configuração de Hiperparâmetros -->
714           <div class="card">
715               <div class="card-header">
716                   <i class="bi bi-gear-fill"></i> 3. Configuração de Hiperparâmetros (JSON)
717               </div>
718               <div class="card-body">
719                   <div class="mb-3">
720                       <label for="{{ form.hyperparameters_json.id_for_label }}" class="form-label">
721                           {{ form.hyperparameters_json.label }}
722                       </label>
723                       {{ form.hyperparameters_json }}
724                       <small class="help-text d-block">{{ form.hyperparameters_json.help_text }}</small>
725                       {% if form.hyperparameters_json.errors %}
726                           <div class="text-danger">{{ form.hyperparameters_json.errors }}</div>
727                       {% endif %}
728   
729                       <button type="button" class="btn btn-outline-secondary btn-example" id="btn-fill-example">
730                           <i class="bi bi-magic"></i> Preencher Exemplo
731                       </button>
732                   </div>
733               </div>
734           </div>
735   
736           <!-- Botão de Submit -->
737           <div class="d-grid gap-2">
738               <button type="submit" class="btn btn-primary btn-lg" id="btn-submit">
739                   <i class="bi bi-play-fill"></i> Iniciar Treinamento
740               </button>
741           </div>
742       </form>
743   </div>
744   
745   <!-- Bootstrap 5 JS Bundle -->
746   <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
747   
748   <script>
749   document.addEventListener('DOMContentLoaded', function() {
750       const loadingOverlay = document.getElementById('loading-overlay');
751       const trainingForm = document.getElementById('training-form');
752       const btnSubmit = document.getElementById('btn-submit');
753       const btnExample = document.getElementById('btn-fill-example');
754       const hyperparamsTextarea = document.getElementById('{{ form.hyperparameters_json.id_for_label }}');
755   
756       // Exemplo de configuração JSON (CORRIGIDO: usa listas em vez de tuplas)
757       const exampleJson = `{
758       "scaler": {
759           "class": "StandardScaler",
760           "params": {}
761       },
762       "pca": {
763           "enabled": false,
764           "class": "PCA",
765           "params": {
766               "n_components": 0.95
767           }
768       },
769       "classifier": {
770           "class": "MLPClassifier",
771           "params_grid": {
772               "activation": ["tanh", "relu"],
773               "hidden_layer_sizes": [[24], [32]],
774               "alpha": [0.0001, 0.0005],
775               "learning_rate_init": [0.01, 0.015],
776               "max_iter": [500, 1000]
777           }
778       }
779   }`;
780   
781       // Botão de exemplo JSON
782       btnExample.addEventListener('click', function() {
783           hyperparamsTextarea.value = exampleJson;
784       });
785   
786       // Submit do formulário com overlay
787       trainingForm.addEventListener('submit', function(e) {
788           // Mostra overlay e desabilita formulário
789           loadingOverlay.classList.add('active');
790           btnSubmit.disabled = true;
791           btnSubmit.innerHTML = '<i class="bi bi-hourglass-split"></i> Processando...';
792   
793           // Permite o submit continuar (não chama e.preventDefault())
794       });
795   
796       // Função utilitária para pegar CSRF token
797       function getCookie(name) {
798           let cookieValue = null;
799           if (document.cookie && document.cookie !== '') {
800               const cookies = document.cookie.split(';');
801               for (let i = 0; i < cookies.length; i++) {
802                   const cookie = cookies[i].trim();
803                   if (cookie.substring(0, name.length + 1) === (name + '=')) {
804                       cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
805                       break;
806                   }
807               }
808           }
809           return cookieValue;
810       }
811   });
812   </script>
813   
814   </body>
815   </html>
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/ml_interface/forms.py
*Saved at: 28/08/2026, 15:38:43*

**[REMOVED]**
```
(from line ~106)
        return json_data
    
    def set_column_choices(self, columns):
        """
        Define as opções de colunas dinamicamente.
        
        Args:
            columns: Lista de nomes de colunas do Excel.
        """
        choices = [(col, col) for col in columns]
        self.fields['feature_columns'].choices = choices
        self.fields['target_column'].choices = choices

```
**[ADDED]**
```
106           return json_data
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/ml_interface/forms.py
*Saved at: 28/08/2026, 15:38:21*

**[REMOVED]**
```
(from line ~74)
            "hidden_layer_sizes": [(24,), (32,)],

```
**[ADDED]**
```
74                "hidden_layer_sizes": [[24], [32]],
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/ml_interface/forms.py
*Saved at: 28/08/2026, 15:36:44*

**[REMOVED]**
```
(from line ~21)
        help_text="Upload de um único arquivo Excel contendo features e target."

```
**[ADDED]**
```
21            help_text="Upload de um único arquivo Excel. A ÚLTIMA coluna será usada como Target (y), todas as anteriores como Features (X)."
```
**[REMOVED]**
```
(from line ~24)
    # Seleção de colunas (serão populadas dinamicamente via JS)
    feature_columns = forms.MultipleChoiceField(
        label="Colunas Features (X)",
        choices=[],
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control',
            'size': '10'
        }),
        help_text="Selecione múltiplas colunas para usar como features."
    )
    
    target_column = forms.ChoiceField(
        label="Coluna Target (y)",
        choices=[],
        widget=forms.Select(attrs={
            'class': 'form-control'
        }),
        help_text="Selecione a coluna que contém os rótulos/classes."
    )
    

```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/ml_interface/views.py
*Saved at: 28/08/2026, 14:41:13*

**[ADDED]**
```
8     import logging
```
**[ADDED]**
```
22    logger = logging.getLogger(__name__)
```
**[ADDED]**
```
24    
```
**[REMOVED]**
```
(from line ~33)


```
**[ADDED]**
```
33            
```
**[REMOVED]**
```
(from line ~39)


```
**[ADDED]**
```
39            
```
**[REMOVED]**
```
(from line ~43)


```
**[ADDED]**
```
43            
```
**[REMOVED]**
```
(from line ~151)
            context['error_message'] = "Erro de validação no formulário. Verifique os campos."

```
**[ADDED]**
```
151               # Mostrar erros de validação detalhados para o usuário
152               error_details = []
153               for field_name, field_errors in form.errors.items():
154                   field_label = form.fields.get(field_name, {}).label if hasattr(form.fields.get(field_name), 'label') else field_name
155                   for error in field_errors:
156                       error_details.append(f"<strong>{field_label}:</strong> {error}")
157               
158               if not error_details:
159                   error_details.append("Verifique todos os campos do formulário.")
160               
161               context['error_message'] = '<br><br>'.join(error_details)
162               logger.error(f"Erros de validação do formulário: {form.errors}")
```
**[REMOVED]**
```
(from line ~180)
        raise Http404("Modelo não encontrado.")

```
**[ADDED]**
```
180           raise Http404("Modelo não encontrado.")
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/ml_interface/views.py
*Saved at: 28/08/2026, 14:26:33*

**[REMOVED]**
```
(from line ~28)
    if request.method == 'GET' and request.FILES.get('excel_file'):
        try:
            excel_file = request.FILES['excel_file']
            
            # Lê apenas as primeiras linhas para pegar os cabeçalhos
            df = pd.read_excel(excel_file, nrows=5)
            columns = df.columns.tolist()
            

```
**[ADDED]**
```
28        try:
29            excel_file = request.FILES.get('excel_file')
30    
31            if not excel_file:
```
**[REMOVED]**
```
(from line ~33)
                'success': True,
                'columns': columns
            })
        except Exception as e:
            return JsonResponse({

```
**[REMOVED]**
```
(from line ~34)
                'error': str(e)

```
**[ADDED]**
```
34                    'error': 'Nenhum arquivo enviado'
```
**[REMOVED]**
```
(from line ~36)
    
    return JsonResponse({
        'success': False,
        'error': 'Nenhum arquivo enviado'
    }, status=400)

```
**[ADDED]**
```
37            # Lê apenas as primeiras linhas para pegar os cabeçalhos
38            df = pd.read_excel(excel_file, nrows=5)
39            columns = df.columns.tolist()
```
**[ADDED]**
```
41            return JsonResponse({
42                'success': True,
43                'columns': columns
44            })
45        except Exception as e:
46            return JsonResponse({
47                'success': False,
48                'error': str(e)
49            }, status=400)
50    
51    
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/ml_interface/views.py
*Saved at: 28/08/2026, 14:25:37*

**[REMOVED]**
```
(from line ~22)
@require_GET

```
**[ADDED]**
```
22    @require_POST
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/ml_interface/templates/ml_interface/train.html
*Saved at: 28/08/2026, 14:25:08*

**[REMOVED]**
```
(from line ~371)
            alert('Não foi possível extrair as colunas automaticamente. Selecione manualmente após enviar o formulário.');        });

```
**[ADDED]**
```
371               alert('Não foi possível extrair as colunas automaticamente. Selecione manualmente após enviar o formulário.');        
372           });
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/ml_interface/templates/ml_interface/train.html
*Saved at: 28/08/2026, 14:24:52*

**[REMOVED]**
```
(from line ~371)
            alert('Não foi possível extrair as colunas automaticamente. Selecione manualmente.');
        });

```
**[ADDED]**
```
371               alert('Não foi possível extrair as colunas automaticamente. Selecione manualmente após enviar o formulário.');        });
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/ml_interface/templates/ml_interface/train.html
*Saved at: 28/08/2026, 14:24:36*

**[REMOVED]**
```
(from line ~356)
        .then(response => response.json())

```
**[ADDED]**
```
356           .then(response => {
357               if (!response.ok) {
358                   throw new Error('Erro HTTP: ' + response.status);
359               }
360               return response.json();
361           })
```

---

### 📄 /home/piva/Documentos/Programação/Python/IA-Trainer/ml_interface/templates/ml_interface/train.html
*Saved at: 28/08/2026, 14:22:49*

**[REMOVED]**
```
(from line ~339)
            const formData = new FormData();
            formData.append('excel_file', this.files[0]);
            
            fetch('{% url "extract_columns" %}?excel_file=' + encodeURIComponent(this.files[0].name), {
                method: 'GET',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    populateSelects(data.columns);
                } else {
                    alert('Erro ao extrair colunas: ' + data.error);
                }
            })
            .catch(error => {
                console.error('Erro:', error);
                // Fallback: tentar extrair via AJAX com o arquivo
                extractColumnsAjax(this.files[0]);
            });

```
**[ADDED]**
```
339               extractColumnsAjax(this.files[0]);
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

