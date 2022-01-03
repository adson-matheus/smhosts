from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Hosts.models import Evento, Host_Porta
from Hosts.views import verificaServer
from Principal.views import historicoDePings, retornaDatas, removeValor, getEixos, getHosts

@login_required
def modoVisualizacao(request):
    hosts = Host_Porta.objects.all()
    eventos = Evento.objects.all()
    eventosOff = Evento.objects.filter(status="OFFLINE")
    histPingHost = []
    histTodosHosts = []
    maxValorGraf = []

    for h in hosts:
        verificaServer(h.id)

    datas = retornaDatas()

    #guarda tudo em histTodosHosts
    for e in eventos:
        histPingHost = historicoDePings(e.id)
        if (histPingHost):
            histTodosHosts.append(histPingHost)
            listaSemNull = removeValor(histPingHost, 'null')
            maxValorGraf.append(max(listaSemNull))

    y, passo = getEixos(maxValorGraf)
    listaHosts = getHosts(eventos)

    #zip junta as duas listas para usar no 'for' do grafico
    #pega cada host e seu historico de pings
    graf = zip(listaHosts, histTodosHosts)

    context = {
        'eventos': eventos,
        'eventosOff':eventosOff,
        'graf':graf,
        'y':y,
        'passo':passo,
        'datas':datas
    }

    return render(request, 'modoVisualizacao.html', context)
