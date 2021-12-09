from django.urls import path
from Visualizacao.views import *

app_name='Visualizacao'

urlpatterns = [
    path('modoTV/', modoVisualizacao, name="modoVisualizacao"),
]
