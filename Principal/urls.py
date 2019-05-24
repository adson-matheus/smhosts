from django.urls import path
from .views import principal
from SMHosts.views import logoutApp

urlpatterns = [
    path('', principal, name="principal"),
    path('logoutApp', logoutApp, name="logoutApp"),
]
