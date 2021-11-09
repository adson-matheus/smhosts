from django.urls import path
from .views import principal
from SMHosts.views import logoutApp

app_name='Principal'

urlpatterns = [
    path('', principal, name="principal"),
    path('logoutApp', logoutApp, name="logoutApp"),
]
