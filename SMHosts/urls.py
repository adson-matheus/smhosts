"""SMHosts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import include
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include, path

from SMHosts.views import loadApp, logoutApp
from Hosts import urls as hosts_urls
from Portas import urls as portas_urls
from Principal import urls as principal_urls

urlpatterns = [
    path('', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path("loadApp/", loadApp),
    path("logoutApp/", logoutApp),
    path('admin/', admin.site.urls),

    path('principal/', include(principal_urls)),
    path('hosts/', include(hosts_urls)),
    path('portas/', include(portas_urls)),
]
