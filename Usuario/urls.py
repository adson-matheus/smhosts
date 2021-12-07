from django.urls import path
from .views import infoUsuario

app_name='Usuario'

urlpatterns = [
    path('info/', infoUsuario, name='infoUsuario'),
]