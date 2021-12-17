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
    passo = 0
    #lenMenor = 100
    #toda vez que atualizar a pagina inicial, verifica o ping
    for h in hosts:
        verificaServer(h.id)

    #datas = retornaDatas()

    #guarda tudo em histTodosHosts
    for e in eventos:
        histPingHost, tam = historicoDePings(e.id)
        #if tam < lenMenor: lenMenor = tam
        if (histPingHost):
            #if (lenMenor < len(histPingHost)):
                #histPingHost = histPingHost[lenMenor:]

            histPingSemNone = histPingHost.copy()
            while None in histPingSemNone:
                histPingSemNone.remove(None)
            histTodosHosts.append(histPingHost)
            maxValorGraf.append(max(histPingSemNone)) #pega o maior valor de ping de cada host

    #valores de 'y' e 'passo' do grafico dashboard2.html
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
        'listaPing':listaPing,
        'listaHosts':listaHosts,
        'graf':graf,
        'maxValorGraf':maxValorGraf,
        'passo':passo
        }

    return render(request, 'principal.html', context)

#grafico de barras dashboard.html nao esta sendo utilizado
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

    # se nao esta online, nao vai pro grafico
    estaOn = historicoEvento.first().status
    if estaOn == 'ONLINE':
        for e in historicoEvento:
            if e.status == 'OFFLINE' or '':
                p.append(None)
                # if len(p) >= 10:
                #     p = p[:10]
                # p.reverse()
                # return p, len(p)
            else:
                p.append(e.ping)
    if len(p) >= 10:
        p = p[:10] #pega apenas os 10 ultimos pings

    p.reverse() #envia reverse para mostrar no grafico
    return p, len(p)

def retornaDatas():
    datas = []
    localhost = Evento.objects.first()
    histDatas = localhost.history.all()[:10]
    for d in histDatas:
        datas.append(d.dataHora)
    datas.reverse()
    return datas

