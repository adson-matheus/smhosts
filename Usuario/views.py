from django.shortcuts import render
from Hosts.models import *

def infoUsuario(request):
    username = request.user.username
    ultimoLogin = request.user.last_login
    dateJoined = request.user.date_joined
    permissoes = request.user.get_user_permissions
    staff = request.user.is_staff
    superuser = request.user.is_superuser
    hosts = Host.objects.count()
    portas = Porta.objects.count()
    context = {
        'username': username,
        'ultimoLogin': ultimoLogin,
        'dateJoined': dateJoined,
        'permissoes': permissoes,
        'staff': staff,
        'superuser': superuser,
        'hosts': hosts,
        'portas':portas
    }
    return render(request, 'infoUsuario.html', context)
