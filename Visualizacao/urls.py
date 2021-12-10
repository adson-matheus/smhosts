from django.urls import path
from Visualizacao.views import *

app_name='Visualizacao'

urlpatterns = [
    path('TV/', modoVisualizacao, name="modoVisualizacao"),
]
