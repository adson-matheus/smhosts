from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Principal.views import dashboard

@login_required
def modoTV(request):
    context = dashboard()
    return render(request, 'baseVisualizacao.html', context)