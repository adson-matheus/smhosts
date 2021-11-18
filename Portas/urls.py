from django.urls import path
from Portas.views import *

app_name = 'Portas'

urlpatterns = [
    path("RegistrarPorta/", registrarPorta, name="RegistrarPorta"),
    path("ListarPortas/", ListarPortas, name="ListarPortas"),
    path("DeletarPorta/<int:id>/", DeletarPorta, name="DeletarPorta"),
]