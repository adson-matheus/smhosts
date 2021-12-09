from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Hosts.models import Evento, Host_Porta
from Hosts.views import isOffline, verificaServer
from Principal.views import historicoDePings, graficoBarras

@login_required
def modoVisualizacao(request):
    hosts = Host_Porta.objects.all()
    eventos = Evento.objects.all()
    eventosOn = Evento.objects.filter(status="ONLINE")
    eventosOff = Evento.objects.filter(status="OFFLINE")
    histPingHost = []
    histTodosHosts = []
    dataHora = []
    maxValorGraf = []
    passo = 0

    #toda vez que atualizar a pagina inicial, verifica o ping
    for h in hosts:
        verificaServer(h.id)

    #guarda tudo em histTodosHosts
    for e in eventosOn:
        histPingHost, dataHora = historicoDePings(e.id)
        histTodosHosts.append(histPingHost)
        maxValorGraf.append(max(histPingHost)) #pega o maior valor de ping de cada host

    #valores de 'y' e 'passo' do grafico visualizacaoDashboard.html
    if (maxValorGraf):
        maxValorGraf = int(max(maxValorGraf)) + 1 #maior valor do vetor + 3
        passo = int(maxValorGraf / 12)
    
    #dashboard.html nao esta sendo utilizado
    listaPing, listaHosts = graficoBarras(eventos)
    
    #zip junta as duas listas para usar no 'for' do grafico
    #pega cada host e seu historico de pings
    graf = zip(listaHosts, histTodosHosts)


    return render(request, 'modoVisualizacao.html', {'eventos': eventos, 'eventosOff':eventosOff, 'listaHosts':listaHosts, 'dataHora':dataHora, 'graf':graf, 'maxValorGraf':maxValorGraf, 'passo':passo})
