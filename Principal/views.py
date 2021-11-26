from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Hosts.models import Evento, Host_Porta

from Hosts.views import verificaServer
import json

@login_required
def principal(request):
    hosts = Host_Porta.objects.all()
    eventos = Evento.objects.all()
    listaPing = []
    listaHosts = []
    pingTeste = []
    pingsAll = []
    
    #toda vez que atualizar a pagina inicial, verifica o ping
    for h in hosts:
        verificaServer(h.id)

    #guarda tudo em pingsAll
    for e in eventos:
        pingTeste = retornaPing(e.id)
        pingsAll.append(pingTeste)

    for e in eventos:
        if e.ping == None:
            pass
        else:
            listaPing.append(e.ping)
            listaHosts.append(e.host_porta_id.host.id)

    return render(request, 'principal.html', {'eventos': eventos, 'listaPing':listaPing, 'listaHosts':listaHosts, 'pingTeste':pingTeste, 'pingsAll':pingsAll})

def retornaPing(id):
    #retorna todos os pings ja feitos
    #envia para o grafico
    evento = Evento.objects.get(pk=id)
    historicoEvento = evento.history.all()
    listaPing = []
    for e in historicoEvento:
        listaPing.append(e.ping)
    return listaPing