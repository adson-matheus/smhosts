from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from Hosts.models import Porta
from .forms import PortaForm

@login_required
def registrarPorta(request):
    if request.method == 'POST':
        form = PortaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Portas:ListarPortas')
    else:
        form = PortaForm()
    return render(request, 'registroPortas/RegistrarPorta.html', {'form':form})

@login_required
def ListarPortas(request):
    portas = Porta.objects.all()
    return render(request, 'listagemPortas/ListarPorta.html', {'portas': portas})

@login_required
def DeletarPorta(id):
    portaDelete = Porta.objects.get(pk=id)
    #portaDelete = get_object_or_404(Porta, pk=id)
    portaDelete.delete()
    return redirect('Portas:ListarPortas')