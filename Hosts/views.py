from django.http import request
from django.shortcuts import render
from django.contrib import messages
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render


from .forms import HostForm, EventoForm
from .models import Host, Evento
from ping3 import ping
from datetime import datetime
import json


@login_required
def RegistroHost(request):
    form = HostForm(request.POST or None)
    if(form.is_valid()):
        form.save()
        messages.success(request, 'Host Registrado com Sucesso!')
        return redirect('../ListarHosts')
    return render(request, 'registroHosts/RegistrarHost.html', {'form': form})

@login_required
def ListarHosts(request):
    hosts = Evento.objects.all()
    for i in hosts:
        registrarEvento(i.id)
    return render(request, 'listagemHosts/ListarHosts.html', {'hosts': hosts})

@login_required
def BuscarHost(request):
    pass

@login_required
def AtualizarHost(request, id):
    host = get_object_or_404(Host, pk=id)
    form = HostForm(request.POST or None, instance=host)
    if(form.is_valid()):
        form.save()
        return redirect('Hosts:ListarHosts')
    return render(request, 'registroHosts/RegistrarHost.html', {'form': form})

@login_required
def DeletarHost(request, id):
    hostDelete = get_object_or_404(Host, pk=id)
    hostDelete.delete()
    return redirect('../../ListarHosts')


def verificaServer(host):
    try:
        if ping(host) < 100:
            return 'ONLINE'
        elif ping(host) >= 100:
            return 'DEMORANDO'
        else:
            return 'OFFLINE'
    except TypeError:
        return 'OFFLINE'


def registrarEvento(id):
    evento = Host.objects.get(pk=id)
    eventoPing = verificaServer(evento.hostname)
    horaEvento = datetime.now()
    e = Evento(host=evento, status=eventoPing, dataHora=horaEvento)
    e.save()
    # if request.method == 'POST':
    #     form = EventoForm(request.POST, instance = evento)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('Hosts:ListarHosts')
    # else:
    #     form = EventoForm()
    # return render(request, 'registroEventos/registrarEvento.html', {'form': form,
    #                                                                 'evento':evento,
    #                                                                 'eventoPing':eventoPing,
    #                                                                 'horaEvento':horaEvento})

    