from django.urls import path
from Usuarios.views import *

app_name = 'Usuarios'

urlpatterns = [
    path('new/', signup_view, name='signup_view')
]