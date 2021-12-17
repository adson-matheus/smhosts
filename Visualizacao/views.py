from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Hosts.models import Evento, Host_Porta
from Hosts.views import verificaServer
from Principal.views import historicoDePings, graficoBarras, retornaDatas

@login_required
def modoVisualizacao(request):
    hosts = Host_Porta.objects.all()
    eventos = Evento.objects.all()
    eventosOff = Evento.objects.filter(status="OFFLINE")
    histPingHost = []
    histTodosHosts = []
    maxValorGraf = []
    passo = 0
    lenMenor = 100
    #toda vez que atualizar a pagina inicial, verifica o ping
    for h in hosts:
        verificaServer(h.id)

    #datas = retornaDatas()

    #guarda tudo em histTodosHosts
    for e in eventos:
        histPingHost, tam = historicoDePings(e.id)
        if tam < lenMenor: lenMenor = tam
        if (histPingHost):
            if (lenMenor < len(histPingHost)):
                histPingHost = histPingHost[lenMenor:]
            histTodosHosts.append(histPingHost)
            maxValorGraf.append(max(histPingHost)) #pega o maior valor de ping de cada host

    #valores de 'y' e 'passo' do grafico visualizacaoDashboard.html
    if (maxValorGraf):
        maxValorGraf = int(max(maxValorGraf)) + 2 #maior valor do vetor + 2
        passo = int(maxValorGraf / 100)
    
    #dashboard.html nao esta sendo utilizado
    listaPing, listaHosts = graficoBarras(eventos)
    
    #zip junta as duas listas para usar no 'for' do grafico
    #pega cada host e seu historico de pings
    graf = zip(listaHosts, histTodosHosts)

    context = {
        'eventos': eventos,
        'eventosOff':eventosOff,
        'listaHosts':listaHosts,
        'graf':graf,
        'maxValorGraf':maxValorGraf,
        'passo':passo
    }

    return render(request, 'modoVisualizacao.html', context)
