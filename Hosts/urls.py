from django.urls import path
from Hosts.views import *

app_name = 'Hosts'

urlpatterns = [
    path("RegistrarHost/", RegistroHost, name="RegistroHost"),
    path("RegistrarHost_Porta/<int:id>/", RegistroHost_Porta, name="RegistroHost_Porta"),
    path("ListarHosts/", ListarHosts, name="ListarHosts"),
    path("AtualizarHost/<int:id>/", AtualizarHost, name="AtualizarHost"),
    path("DeletarHost/<int:id>/", DeletarHost, name="DeletarHost"),
    path('logs/<int:id>', logs, name='logs'),
]