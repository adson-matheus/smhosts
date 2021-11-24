from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Hosts.models import Evento, Host_Porta

from Hosts.views import verificaServer
import json

@login_required
def principal(request):
    hosts = Host_Porta.objects.all()
    listaPing = []
    listaHosts = []
    #toda vez que atualizar a pagina inicial, verifica o ping
    for h in hosts:
        verificaServer(h.id)

    eventos = Evento.objects.all()
    for e in eventos:
        listaPing.append(e.ping)
        listaHosts.append(e.host_porta_id.host.hostname)
    #listaPing.remove(None)
    return render(request, 'principal.html', {'eventos': eventos, 'listaPing':listaPing, 'listaHosts':listaHosts})