"""
Views para a interface de treinamento de ML.
"""
import json
import os
import tempfile
import traceback
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
