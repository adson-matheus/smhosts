from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from Hosts.forms import Host_PortaForm, HostForm
from .models import Host, Evento, Host_Porta, Porta
from ping3 import ping



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

            #cria o evento default
            h = Host_Porta.objects.latest('id')
            e = Evento(host_porta_id=h, status='')
            e.save()

            return redirect('Hosts:ListarHosts')
    return render(request, 'registroHost_Porta/registroHost_Porta.html', {'host': host, 'porta': porta})


@login_required
def ListarHosts(request):
    hosts = Host_Porta.objects.all()

    #toda vez que lista os hosts, verifica o ping
    for h in hosts:
        verificaServer(h.id)
    eventos = Evento.objects.all()
    return render(request, 'listagemHosts/ListarHosts.html', {'hosts': hosts, 'eventos':eventos})

@login_required
def BuscarHost(request):
    pass

@login_required
def AtualizarHost(request, id):
    form = Host.objects.get(pk=id)

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


def verificaServer(id):
    host = Host_Porta.objects.get(pk=id)
    p = ping(host.host.hostname)
    evento = Evento.objects.filter(host_porta_id=host.id).get()

    #https://docs.djangoproject.com/en/3.2/ref/models/querysets/#update-or-create
    try:
        if p < 100:
            evento, created = Evento.objects.update_or_create(
                host_porta_id=evento.host_porta_id,
                defaults={'status':'ONLINE'},
                )
        elif p >= 100:
            evento, created = Evento.objects.update_or_create(
                host_porta_id=evento.host_porta_id,
                defaults={'status':'DEMORANDO'},
                )
        else:
            evento, created = Evento.objects.update_or_create(
                host_porta_id=evento.host_porta_id,
                defaults={'status':'OFFLINE'},
                )
    except TypeError:
        evento, created = Evento.objects.update_or_create(
            host_porta_id=evento.host_porta_id,
            defaults={'status':'OFFLINE'},
            )
    evento.save()
