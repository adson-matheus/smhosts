from django.contrib import messages
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render


from Hosts.forms import Host_PortaForm
from .models import Host, Evento, Host_Porta
from ping3 import ping
from datetime import datetime


@login_required
def RegistroHost(request):
    form = Host_PortaForm(request.POST or None)
    if(form.is_valid()):
        form.save()
        messages.success(request, 'Host Registrado com Sucesso!')
        return redirect('Hosts:ListarHosts')
    return render(request, 'registroHosts/RegistrarHost.html', {'form': form})

@login_required
def ListarHosts(request):
    hosts = Host_Porta.objects.all()
    #for i in hosts:
    #    registrarEvento(i.id)
    return render(request, 'listagemHosts/ListarHosts.html', {'hosts': hosts})

@login_required
def BuscarHost(request):
    pass

@login_required
def AtualizarHost(request, id):
    host = get_object_or_404(Host, pk=id)
    form = Host_PortaForm(request.POST or None, instance=host)
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
    #salva evento somente se nao estiver online
    if eventoPing != 'ONLINE':
        pass
    else:
        e.save()