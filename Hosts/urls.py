from django.urls import path
from .views import ListarHosts, AtualizarHost, DeletarHost

urlpatterns = [
    path("ListarHosts/", ListarHosts, name="ListarHosts"),
    path("AtualizarHost/<int:id>/", AtualizarHost, name="AtualizarHost"),
    path("DeletarHost/<int:id>/", DeletarHost, name="DeletarHost"),
]