from django.contrib import messages
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render


from Hosts.forms import Host_PortaForm, HostForm
from .models import Host, Evento, Host_Porta, Porta
from ping3 import ping
from datetime import datetime


@login_required
def RegistroHost(request):
    host = HostForm(request.POST or None)
    if(host.is_valid()):
        host.save()
        h = Host.objects.latest('id')
        return redirect('Hosts:RegistroHost_Porta', h.id)
    return render(request, 'registroHosts/RegistrarHost.html', {'host': host})

# add somente o host, e depois add as portas?

@login_required
def RegistroHost_Porta(request, id):
    host = Host.objects.get(pk=id)
    porta = Porta.objects.all()
    if request.method == 'POST':
        host_porta = Host_PortaForm(request.POST)
        if host_porta.is_valid():
            host_porta.save()
            return redirect('Hosts:ListarHosts')
    return render(request, 'registroHost_Porta/registroHost_Porta.html', {'host': host, 'porta': porta})


@login_required
def ListarHosts(request):
    hosts = Host_Porta.objects.all()
    eventos = Evento.objects.all()
    return render(request, 'listagemHosts/ListarHosts.html', {'hosts': hosts, 'eventos':eventos})

@login_required
def BuscarHost(request):
    pass

@login_required
def AtualizarHost(request, id):
    form = Host.objects.get(pk=id)
    #porta = Porta.objects.all()
    if request.method=='POST':
        form = HostForm(request.POST, instance=form)
        if(form.is_valid()):
            form.save()
        return redirect('Hosts:ListarHosts')
    else:
        HostForm(instance=form)
    return render(request, 'editarHost/EditarHost.html', {'form': form})

@login_required
def DeletarHost(request, id):
    hostDelete = get_object_or_404(Host_Porta, pk=id)
    hostDelete.delete()
    return redirect('Hosts:ListarHosts')


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

#falta registrar automaticamente
def registrarEvento(request, id):
    host = Host.objects.get(pk=id)
    eventoPing = verificaServer(host.hostname)
    e = Evento(status=eventoPing, host_id=host)
    #salva evento somente se nao estiver online
    if eventoPing == 'OFFLINE':
        e.save()
        host.evento = e
        host.save()
    else:
        pass
    return redirect('Hosts:ListarHosts')
