"""
URLs do app ml_interface.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.train_view, name='train'),
    path('extract-columns/', views.extract_columns, name='extract_columns'),
    path('download/<str:filename>/', views.download_model, name='download_model'),
]
