from django.urls import path
from Hosts.views import *

app_name = 'Hosts'

urlpatterns = [
    path("RegistrarHost/", RegistroHost, name="RegistroHost"),
    path("ListarHosts/", ListarHosts, name="ListarHosts"),
    path("AtualizarHost/<int:id>/", AtualizarHost, name="AtualizarHost"),
    path("DeletarHost/<int:id>/", DeletarHost, name="DeletarHost"),
    path("RegistrarEvento/<int:id>/", registrarEvento, name="RegistrarEvento"),
]