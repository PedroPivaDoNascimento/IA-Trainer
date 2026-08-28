"""
Utilitário para limpeza de modelos antigos.
"""
import os
import glob
from django.conf import settings


def cleanup_old_models():
    """
    Remove todos os arquivos .pkl da pasta de modelos treinados.
    Deve ser chamado antes de iniciar um novo treinamento.
    """
    modelos_dir = os.path.join(settings.MEDIA_ROOT, 'modelos_treinados')
    
    # Cria o diretório se não existir
    if not os.path.exists(modelos_dir):
        os.makedirs(modelos_dir)
        return
    
    # Remove todos os arquivos .pkl
    pkl_files = glob.glob(os.path.join(modelos_dir, '*.pkl'))
    for file_path in pkl_files:
        try:
            os.remove(file_path)
            print(f"Modelo antigo removido: {file_path}")
        except Exception as e:
            print(f"Erro ao remover {file_path}: {e}")
