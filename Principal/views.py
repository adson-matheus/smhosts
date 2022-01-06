from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Hosts.models import Evento, Host_Porta
from Hosts.views import verificaServer

@login_required
def principal(request):
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

    context = {
        'eventos': eventos,
        'graf':graf,
        'y':y,
        'passo':passo,
        'datas':datas
    }
    return render(request, 'principal.html', context)

def getHost(e):
    return e.host_porta_id.host.descricao

def historicoDePings(id):
    #retorna todos os pings ja feitos
    evento = Evento.objects.get(pk=id)
    historicoEvento = evento.history.all()
    p = []

    # se nao esta online, nao vai pro grafico
    estaOn = historicoEvento.first().status
    if estaOn == 'ONLINE':
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
    datas = []
    localhost = Evento.objects.first()
    histDatas = localhost.history.all()[:10]
    for d in histDatas:
        datas.append(d.dataHora)
    datas.reverse()
    return datas

def getEixos(maximo):
    y = int(max(maximo)) + 6
    passo = int(y / 100)
    return y, passo

def removeValor(lista, remover):
    return [valor for valor in lista if valor != remover]
