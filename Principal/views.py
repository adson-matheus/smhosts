from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Hosts.models import Evento

import json

@login_required
def principal(request):
    listaPing = []
    listaHosts = []
    eventos = Evento.objects.all()
    for e in eventos:
        listaPing.append(e.ping)
        listaHosts.append(e.host_porta_id.host.hostname)
    #listaPing.remove(None)
    return render(request, 'principal.html', {'eventos': eventos, 'listaPing':listaPing, 'listaHosts':listaHosts})