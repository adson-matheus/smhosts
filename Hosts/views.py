from django.shortcuts import render
from .forms import HostForm
from django.contrib import messages
from .models import Hosts
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from Principal.urls import principal


@login_required
def RegistroHost(request):
    form = HostForm(request.POST or None)
    if(form.is_valid()):
        form.save()
        messages.success(request, 'Host Registrado com Sucesso!')
        return redirect('../ListarHosts')
    return render(request, 'RegistroHost.html', {'form': form})

@login_required
def ListarHosts(request):
    hosts = Hosts.objects.all()
    return render(request, 'listagemHosts/ListarHosts.html', {'hosts': hosts})
# Create your views here.

@login_required
def BuscarHost(request):
    pass

@login_required
def AtualizarHost(request):
    host = get_object_or_404(Hosts, pk=id)
    form = HostForm(request.POST or None, instance=host)
    if(form.is_valid()):
        form.save()
        return redirect('../ListarHosts')
    return render(request, 'RegistroHosts.html', {'form': form})

@login_required
def DeletarHost(request):
    hostDelete = get_object_or_404(Hosts, pk=id)
    hostDelete.delete()
    return redirect('../ListarHosts')
