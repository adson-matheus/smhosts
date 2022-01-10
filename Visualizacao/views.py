from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Hosts.models import Evento, Host_Porta
from Hosts.views import isOffline, verificaServer
from Principal.views import historicoDePings, retornaDatas, removeValor, getEixos, getHost

@login_required
def modoVisualizacao(request):
    hosts = Host_Porta.objects.all()
    eventos = Evento.objects.all()
    eventosOff = isOffline()
    histPingHost = []
    histTodosHosts = []
    maxValorGraf = []
    listaHosts = []

    for h in hosts:
        verificaServer(h.id)

    datas = retornaDatas()
    
    #guarda tudo em histTodosHosts
    for e in eventos:
        histPingHost = historicoDePings(e.id)
        if (histPingHost):
            histTodosHosts.append(histPingHost)
            listaHosts.append(getHost(e))
            listaSemNull = removeValor(histPingHost, 'null')
            maxValorGraf.append(max(listaSemNull))

    if (maxValorGraf):
        y, passo = getEixos(maxValorGraf)
    else:
        y = passo = 0

    #zip junta as duas listas para usar no 'for' do grafico
    #pega cada host e seu historico de pings
    graf = zip(listaHosts, histTodosHosts)

    context = {
        'eventos':eventos,
        'eventosOff':eventosOff,
        'graf':graf,
        'y':y,
        'passo':passo,
        'datas':datas
    }

    return render(request, 'visualizacaoDashboard.html', context)

def dashboard(request):
    hosts = Host_Porta.objects.all()
    eventos = Evento.objects.all()
    eventosOff = isOffline()
    histPingHost = []
    histTodosHosts = []
    maxValorGraf = []
    listaHosts = []

    for h in hosts:
        verificaServer(h.id)

    datas = retornaDatas()
    
    #guarda tudo em histTodosHosts
    for e in eventos:
        histPingHost = historicoDePings(e.id)
        if (histPingHost):
            histTodosHosts.append(histPingHost)
            listaHosts.append(getHost(e))
            listaSemNull = removeValor(histPingHost, 'null')
            maxValorGraf.append(max(listaSemNull))

    if (maxValorGraf):
        y, passo = getEixos(maxValorGraf)
    else:
        y = passo = 0

    #zip junta as duas listas para usar no 'for' do grafico
    #pega cada host e seu historico de pings
    graf = zip(listaHosts, histTodosHosts)

    lastData = datas[-1]

    context = {
        'eventos': eventos,
        'eventosOff':eventosOff,
        'graf':graf,
        'y':y,
        'passo':passo,
        'datas':datas,
        'lastData':lastData,
    }

    return render(request, 'dashboard.html', context)