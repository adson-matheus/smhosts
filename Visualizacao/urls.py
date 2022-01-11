from django.urls import path
from Visualizacao.views import *

app_name='Visualizacao'

urlpatterns = [
    path('dashboard/', modoTV, name="dashboard"),
]
