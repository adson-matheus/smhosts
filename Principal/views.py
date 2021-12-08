from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Hosts.models import Evento, Host_Porta
from Hosts.views import verificaServer, isOffline

@login_required
def principal(request):
    hosts = Host_Porta.objects.all()
    eventos = Evento.objects.all()
    histPingHost = []
    histTodosHosts = []
    dataHora = []
    maxValorGraf = []
    passo = 0

    #toda vez que atualizar a pagina inicial, verifica o ping
    for h in hosts:
        verificaServer(h.id)

    #guarda tudo em histTodosHosts
    for e in eventos:
        histPingHost, dataHora = historicoDePings(e.id)
        histTodosHosts.append(histPingHost)
        maxValorGraf.append(max(histPingHost)) #pega o maior valor de ping de cada host

    if (maxValorGraf):
        maxValorGraf = int(max(maxValorGraf)) + 1 #maior valor do vetor + 3
        passo = int(maxValorGraf / 12)
    
    listaPing, listaHosts = graficoBarras(eventos)
    
    #zip junta as duas listas para usar no 'for' do grafico
    graf = zip(listaHosts, histTodosHosts)

    return render(request, 'principal.html', {'eventos': eventos, 'listaPing':listaPing, 'listaHosts':listaHosts, 'dataHora':dataHora, 'graf':graf, 'maxValorGraf':maxValorGraf, 'passo':passo})

def graficoBarras(eventos):
    listaPing = []
    listaHosts = []
    for e in eventos:
        if e.ping == None:
            pass
        else:
            listaPing.append(e.ping)
            listaHosts.append(e.host_porta_id.host.descricao)
    return listaPing, listaHosts

def historicoDePings(id):
    #retorna todos os pings ja feitos
    evento = Evento.objects.get(pk=id)
    historicoEvento = evento.history.all()
    p = []
    d = [] #lista com horas para usar no grafico

    for e in historicoEvento:
        p.append(e.ping)
        d.append(e.dataHora)
    d.pop()
    p.pop() #elimina o None de quando foi criado
    
    if len(d) >= 10:
        d = d[:10]
    if len(p) >= 10:
        p = p[:10] #pega apenas os 10 ultimos pings
    
    d.reverse()
    p.reverse() #envia reverse para mostrar no grafico
    return p, d
