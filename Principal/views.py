from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Hosts.models import Evento, Host_Porta
from Hosts.views import isOffline, verificaServer

@login_required
def principal(request):
    context = dashboard()
    return render(request, 'principal.html', context)

def dashboard():
    hosts = Host_Porta.objects.all()
    eventos = Evento.objects.all()
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
    eventosOff = isOffline()

    context = {
        'eventos': eventos,
        'eventosOff':eventosOff,
        'graf':graf,
        'y':y,
        'passo':passo,
        'datas':datas,
        'lastData':lastData,
    }

    return context

def getHost(e):
    return e.host_porta_id.host.descricao

def historicoDePings(id):
    #retorna todos os pings ja feitos
    evento = Evento.objects.get(pk=id)
    historicoEvento = evento.history.all()
    p = []
    
    if evento.status == 'ONLINE':
        for e in historicoEvento:
            if len(p) >= 10:
                p = p[:10]
                p.reverse()
                return p

            if e.status == 'ONLINE' or 'DEMORANDO':
                if e.ping == None:
                    p.append('null')
                else:
                    p.append(e.ping)
            else:
                p.append('null')

    p.reverse() #envia reverse para mostrar no grafico
    return p

def retornaDatas():
    """ imprescindivel que o primeiro host cadastrado seja a maquina que ira rodar o servico """
    datas = []
    localhost = Evento.objects.first()
    histDatas = localhost.history.all()[:10]
    for d in histDatas:
        datas.append(d.dataHora)
    datas.reverse()
    return datas

def getEixos(maximo):
    if (max(maximo)) < 100:
        y = int(max(maximo)) + 10
    elif (max(maximo)) <= 200:
        y = int(max(maximo)) + 15
    else:
        y = int(max(maximo)) + 20
    passo = int(y / 100)
    return y, passo

def removeValor(lista, remover):
    return [valor for valor in lista if valor != remover]
