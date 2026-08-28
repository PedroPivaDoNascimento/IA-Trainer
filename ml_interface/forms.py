"""
Forms para a interface de treinamento de ML.
"""
from django import forms
from django.core.exceptions import ValidationError
import json


class TrainingForm(forms.Form):
    """
    Formulário principal para configuração do pipeline de ML.
    """
    
    # Upload do arquivo Excel único
    excel_file = forms.FileField(
        label="Arquivo Excel (Dados + Target)",
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'accept': '.xlsx,.xls'
        }),
        help_text="Upload de um único arquivo Excel contendo features e target."
    )
    
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
    
    # Validação Cruzada
    cv_folds = forms.IntegerField(
        label="Número de Folds (Validação Cruzada)",
        min_value=2,
        max_value=20,
        initial=5,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': 2,
            'max': 20
        }),
        help_text="Número de folds para StratifiedKFold (ex: 3, 5, 10)."
    )
    
    # Random State para reprodutibilidade
    random_state = forms.IntegerField(
        label="Random State (Reprodutibilidade)",
        min_value=0,
        max_value=10000,
        initial=42,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': 0,
            'max': 10000
        }),
        help_text="Semente aleatória para train_test_split e StratifiedKFold."
    )
    
    # Configuração de Hiperparâmetros em JSON
    hyperparameters_json = forms.CharField(
        label="Configuração de Hiperparâmetros (JSON)",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': '15',
            'placeholder': '''{
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

Exemplo de classes disponíveis:
- Scalers: StandardScaler, RobustScaler, MinMaxScaler, MaxAbsScaler, QuantileTransformer, PowerTransformer, Normalizer
- Redução: PCA, SelectKBest
- Classificadores: MLPClassifier, RandomForestClassifier, SVC, LinearSVC, KNeighborsClassifier, LogisticRegression, GradientBoostingClassifier, ExtraTreesClassifier, RidgeClassifier, Perceptron
'''
        }),
        help_text="Defina os hiperparâmetros do scaler, PCA (opcional) e classifier em formato JSON."
    )
    
    def clean_hyperparameters_json(self):
        """Valida se o JSON está bem formado."""
        json_data = self.cleaned_data.get('hyperparameters_json')
        if json_data:
            try:
                parsed = json.loads(json_data)
                # Validação básica da estrutura
                if 'classifier' not in parsed:
                    raise ValidationError("O JSON deve conter a chave 'classifier'.")
                if 'class' not in parsed['classifier']:
                    raise ValidationError("O classifier deve ter uma chave 'class'.")
                if 'params_grid' not in parsed['classifier']:
                    raise ValidationError("O classifier deve ter uma chave 'params_grid'.")
            except json.JSONDecodeError as e:
                raise ValidationError(f"JSON inválido: {str(e)}")
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
