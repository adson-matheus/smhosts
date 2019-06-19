from django.shortcuts import render
from .forms import HostForm
from .models import Hosts
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from Principal.urls import principal
import json
from django.core.serializers.json import DjangoJSONEncoder

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
    hosts = Hosts.objects.all().values()
    hosts2 = json.loads(json.dumps(list(hosts), cls=DjangoJSONEncoder))
    for i in range(len(hosts2)):
        print("-->>>> Host {}: {}".format(i, hosts2[i]['hostname']))
        print(hosts2[i].values())
    return render(request, 'listagemHosts/ListarHosts.html', {'hosts': hosts})
# Create your views here.

@login_required
def BuscarHost(request):
    pass

@login_required
def AtualizarHost(request, id):
    host = get_object_or_404(Hosts, pk=id)
    form = HostForm(request.POST or None, instance=host)
    if(form.is_valid()):
        form.save()
        return redirect('../../ListarHosts')
    return render(request, 'registroHosts/RegistrarHost.html', {'form': form})

@login_required
def DeletarHost(request, id):
    hostDelete = get_object_or_404(Hosts, pk=id)
    hostDelete.delete()
    return redirect('../../ListarHosts')
