# Documentação: Transformação do IA-Trainer em Interface Web Django

## 📋 Visão Geral

Este documento descreve a transformação do script original de ML (IA-Trainer) em uma interface web robusta utilizando Django, permitindo controle total sobre o pipeline de Machine Learning através de uma interface gráfica.

---

## 1. Passo a Passo de Setup do Django

### 1.1 Ambiente Virtual e Instalação de Dependências

```bash
# Criar ambiente virtual (opcional mas recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instalar dependências
pip install django scikit-learn pandas openpyxl joblib matplotlib seaborn numpy

# Ou usar o arquivo requirements_django.txt
pip install -r requirements_django.txt
```

### 1.2 Criação do Projeto e App

```bash
# Criar projeto Django na raiz do workspace
django-admin startproject ml_project .

# Criar app para a interface de ML
python manage.py startapp ml_interface
```

### 1.3 Configurações no `settings.py`

Adicionar/modificar as seguintes configurações:

```python
import os

# Adicionar app nas INSTALLED_APPS
INSTALLED_APPS = [
    # ... apps padrão ...
    'ml_interface',
]

# Configurar MEDIA para uploads de modelos
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Limites de upload (importante para Excel grandes)
DATA_UPLOAD_MAX_MEMORY_SIZE = 52428800  # 50MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 52428800  # 50MB

# Hosts permitidos (em produção, altere para seu domínio)
ALLOWED_HOSTS = ['*']
```

---

## 2. Adaptação do Código Fonte Existente (IA-Trainer)

### 2.1 Arquivos Originais que Foram Adaptados

| Arquivo Original | Adaptação Realizada |
|-----------------|---------------------|
| `src/models/data_handler.py` | Já suportava `random_state` no `train_test_split` |
| `src/models/trainer.py` | Foi criado `dynamic_trainer.py` com configuração dinâmica |
| `src/models/model_config.py` | Substituído por configuração via JSON no frontend |
| `src/controllers/training_controller.py` | Lógica movida para `views.py` do Django |

### 2.2 Novo Módulo: `dynamic_trainer.py`

Este módulo foi criado para substituir a configuração fixa do `model_config.py`:

**Principais características:**

1. **Recebe `random_state` e aplica no `train_test_split`:**
   ```python
   X_train, X_test, y_train, y_test = train_test_split(
       X, y, 
       test_size=0.2, 
       random_state=random_state,  # Controlado pelo usuário
       stratify=y
   )
   ```

2. **Recebe número de `cv` (folds) e `random_state` para o `StratifiedKFold`:**
   ```python
   cv = StratifiedKFold(
       n_splits=cv_folds,  # Definido pelo usuário (ex: 3, 5, 10)
       shuffle=True,
       random_state=random_state  # Mesmo random_state global
   )
   ```

3. **Constrói Pipeline dinâmico com notação de prefixos:**
   ```python
   # Exemplo de param_grid gerado:
   param_grid = {
       'scaler__with_mean': [True, False],
       'pca__n_components': [0.95, 0.99],
       'classifier__n_estimators': [100, 300, 500],
       'classifier__max_depth': [None, 10, 20]
   }
   ```

---

## 3. Estrutura de Arquivos Criados

### 3.1 Utilitários

#### `/workspace/ml_interface/utils/cleanup.py`
```python
"""
Remove todos os arquivos .pkl da pasta antes de novo treinamento.
"""
def cleanup_old_models():
    modelos_dir = os.path.join(settings.MEDIA_ROOT, 'modelos_treinados')
    pkl_files = glob.glob(os.path.join(modelos_dir, '*.pkl'))
    for file_path in pkl_files:
        os.remove(file_path)
```

#### `/workspace/ml_interface/utils/dynamic_trainer.py`
Classe `DynamicTrainer` que:
- Mapeia classes do scikit-learn por nome (string)
- Constrói Pipeline dinamicamente
- Gera `param_grid` usando notação de prefixos (`step__param`)
- Aceita `cv_folds` e `random_state` como parâmetros

### 3.2 Forms

#### `/workspace/ml_interface/forms.py`
```python
class TrainingForm(forms.Form):
    excel_file = forms.FileField(...)  # Upload único
    feature_columns = forms.MultipleChoiceField(...)  # Múltipla escolha
    target_column = forms.ChoiceField(...)  # Target
    cv_folds = forms.IntegerField(min_value=2, max_value=20)  # Folds
    random_state = forms.IntegerField(min_value=0, max_value=10000)  # Seed
    hyperparameters_json = forms.CharField(widget=forms.Textarea)  # JSON
```

### 3.3 Views

#### `/workspace/ml_interface/views.py`

**Views implementadas:**

1. **`extract_columns(request)`** - AJAX para extrair colunas do Excel
2. **`train_view(request)`** - View principal de treinamento
3. **`download_model(request, filename)`** - Download do modelo .pkl

**Fluxo da view `train_view`:**
```python
1. Valida formulário
2. Chama cleanup_old_models() ← Remove .pkl antigos
3. Salva Excel temporariamente
4. Extrai features (X) e target (y)
5. Aplica train_test_split com random_state controlado
6. Constrói Pipeline + param_grid dinamicamente
7. Executa GridSearchCV com StratifiedKFold(random_state=rs)
8. Avalia nos dados de teste
9. Salva modelo em media/modelos_treinados/
10. Retorna resultados para template
```

### 3.4 URLs

#### `/workspace/ml_interface/urls.py`
```python
urlpatterns = [
    path('', views.train_view, name='train'),
    path('extract-columns/', views.extract_columns, name='extract_columns'),
    path('download/<str:filename>/', views.download_model, name='download_model'),
]
```

#### `/workspace/ml_project/urls.py` (projeto principal)
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ml_interface.urls')),  # Inclui urls do app
]

# Serve media files em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### 3.5 Templates

#### `/workspace/ml_interface/templates/ml_interface/train.html`

**Recursos do template:**

1. **Overlay de carregamento** com spinner Bootstrap
2. **Formulário dividido em cards**:
   - Dados e Colunas
   - Validação Cruzada e Reprodutibilidade
   - Configuração de Hiperparâmetros (JSON)
3. **JavaScript para:**
   - Extrair colunas via AJAX após upload
   - Preencher exemplo de JSON automaticamente
   - Mostrar overlay e desabilitar botão no submit
4. **Exibição de resultados** com métricas e download

---

## 4. Exemplo de Configuração JSON

O usuário deve preencher o campo de hiperparâmetros com JSON neste formato:

```json
{
    "scaler": {
        "class": "StandardScaler",
        "params": {}
    },
    "pca": {
        "enabled": false,
        "class": "PCA",
        "params": {
            "n_components": 0.95
        }
    },
    "classifier": {
        "class": "MLPClassifier",
        "params_grid": {
            "activation": ["tanh", "relu"],
            "hidden_layer_sizes": [(24,), (32,)],
            "alpha": [0.0001, 0.0005],
            "learning_rate_init": [0.01, 0.015],
            "max_iter": [500, 1000]
        }
    }
}
```

### Classes Disponíveis

**Scalers:**
- `StandardScaler`, `RobustScaler`, `MinMaxScaler`, `MaxAbsScaler`
- `QuantileTransformer`, `PowerTransformer`, `Normalizer`

**Redução de Dimensionalidade:**
- `PCA`, `SelectKBest`

**Classificadores:**
- `MLPClassifier`, `RandomForestClassifier`, `SVC`, `LinearSVC`
- `KNeighborsClassifier`, `LogisticRegression`, `GradientBoostingClassifier`
- `ExtraTreesClassifier`, `RidgeClassifier`, `Perceptron`

---

## 5. Como Rodar e Testar

### 5.1 Iniciar Servidor de Desenvolvimento

```bash
cd /workspace
python manage.py runserver 0.0.0.0:8000
```

Acesse: `http://localhost:8000`

### 5.2 Fluxo de Teste

1. **Upload do Excel:** Selecione um arquivo `.xlsx` ou `.xls`
2. **Seleção de Colunas:** 
   - O JS tentará extrair colunas automaticamente
   - Selecione múltiplas features (segure Ctrl/Cmd)
   - Selecione o target (última coluna é sugerida)
3. **Validação Cruzada:** Defina número de folds (ex: 5)
4. **Reprodutibilidade:** Defina random_state (ex: 42)
5. **Hiperparâmetros:** 
   - Clique em "Preencher Exemplo" para ver formato
   - Edite conforme necessário
6. **Treinar:** Clique em "Iniciar Treinamento"
7. **Aguardar:** Overlay aparecerá com spinner
8. **Resultado:** Métricas exibidas + link para download

---

## 6. Avisos Críticos e Considerações

### 6.1 Timeout de Requisições HTTP

**Problema:** GridSearchCV com muitos hiperparâmetros pode exceder o timeout padrão.

**Soluções:**

1. **Para desenvolvimento (servidor Django):**
   ```bash
   # O servidor de desenvolvimento não tem timeout rígido
   # Mas pode ser interrompido pelo navegador (geralmente 2-5 min)
   python manage.py runserver --noreload
   ```

2. **Para produção (Gunicorn/uWSGI):**
   ```bash
   # Gunicorn com timeout aumentado
   gunicorn ml_project.wsgi:application --timeout 300 --workers 2
   ```

3. **Recomendação de UX:**
   - Use grids de hiperparâmetros menores inicialmente
   - Teste com poucos folds (3-5) primeiro
   - Considere usar `n_jobs=-1` para paralelizar (já configurado)

### 6.2 Limites de Upload

Configurado em `settings.py`:
```python
DATA_UPLOAD_MAX_MEMORY_SIZE = 52428800  # 50MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 52428800  # 50MB
```

Para arquivos maiores, ajuste esses valores ou use upload em chunks.

### 6.3 Reprodutibilidade Garantida

O mesmo `random_state` é usado em:
1. ✅ `train_test_split(random_state=rs)`
2. ✅ `StratifiedKFold(random_state=rs)`
3. ✅ Classificadores que suportam `random_state` (MLP, RF, SVC, etc.)
4. ✅ PCA (quando habilitado)

Isso garante que execuções idênticas produzam resultados idênticos.

### 6.4 Gerenciamento de Modelos `.pkl`

**Regra obrigatória implementada:**
- Antes de cada treinamento, `cleanup_old_models()` remove TODOS os `.pkl` da pasta `media/modelos_treinados/`
- Isso evita acumulação de arquivos e confusão entre modelos

---

## 7. Estrutura Final do Projeto

```
/workspace/
├── ml_project/                 # Projeto Django
│   ├── settings.py             # Configurações (MEDIA, UPLOAD limits)
│   ├── urls.py                 # URLs principais
│   └── wsgi.py
├── ml_interface/               # App de ML
│   ├── utils/
│   │   ├── cleanup.py          # Limpeza de .pkl antigos
│   │   └── dynamic_trainer.py  # Pipeline dinâmico
│   ├── templates/
│   │   └── ml_interface/
│   │       └── train.html      # Interface web
│   ├── forms.py                # Formulários Django
│   ├── views.py                # Lógica das views
│   └── urls.py                 # URLs do app
├── media/
│   └── modelos_treinados/      # Pasta dos modelos .pkl
├── requirements_django.txt     # Dependências
└── manage.py
```

---

## 8. Próximos Passos Sugeridos

1. **Implementar Treinamento Assíncrono:**
   - Usar Celery + Redis para treinar em background
   - Mostrar progresso via WebSocket ou polling

2. **Histórico de Treinamentos:**
   - Salvar metadados em banco de dados
   - Permitir comparar múltiplos treinamentos

3. **Visualizações:**
   - Curvas ROC, Matriz de Confusão
   - Gráficos de importância de features

4. **Validação de JSON Avançada:**
   - Editor JSON com syntax highlighting (CodeMirror/Monaco)
   - Validação de schema em tempo real

5. **Templates de Configuração:**
   - Salvar configurações JSON como templates
   - Permitir reutilização em novos treinamentos

---

## 9. Conclusão

A interface web Django transforma o processo manual de treinamento de ML em uma experiência interativa e controlável, mantendo a reprodutibilidade científica através do controle explícito de `random_state` e validação cruzada configurável.

**Benefícios alcançados:**
- ✅ Upload único de Excel com seleção dinâmica de colunas
- ✅ Configuração granular via JSON (scaler, pca, classifier)
- ✅ Controle total de validação cruzada (folds) e reprodutibilidade (random_state)
- ✅ Feedback visual com overlay durante treinamento
- ✅ Gerenciamento automático de modelos (.pkl)
- ✅ Download do melhor modelo encontrado
