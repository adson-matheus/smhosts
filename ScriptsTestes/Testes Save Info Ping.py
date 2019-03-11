import os, re

IPs = ['192.168.0.1', '8.8.8.8', '189.90.16.20', '300.90.10.50']

results = {}
valores = {}

#Organizando as Estatísticas dos pacotes
def OrganizaInfoPacotes(lista):
    aux = '{} {}'.format(lista[8].strip(' '), lista[9].strip(' '))
    aux = aux.split(': ')
    del(aux[0])
    aux = aux[0].split(', ')
    aux2 = aux[2].split(',')
    aux.append(aux2[0])
    del(aux[2])
    valores['Pacotes'] = aux

    #Organizando os Tempos em 'ms'
def OrganizaInfoTempo(lista, statusPacotes):
    if(re.search('100%', statusPacotes)):
        aux = 'Sem medição de tempo.'
    else:
        aux = lista[11].split(', ')
        aux[0] = aux[0].strip(' ')
        aux2 = aux[0].split(' = ')
        aux[0] = 'Mínimo = {}'.format(aux2[1])
        aux2 = aux[1].split(' = ')
        aux[1] = 'Máximo = {}'.format(aux2[1])
        aux2 = aux[2].split(' = ')
        aux[2] = 'Média = {}'.format(aux2[1])
    valores['Tempo'] = aux

for i in range(len(IPs)):
    cmd = 'ping {}'.format(IPs[i])
    test = "".join(os.popen(cmd).readlines())
    test = test.split('\n')
    if(re.search('Verifique o nome', test[0])):
        valores['Pacotes'] = 'Host Inválido'
        valores['Tempo'] = 'Sem medição de tempo.'
        results[IPs[i]] = valores
    else:
        OrganizaInfoPacotes(test)
        OrganizaInfoTempo(test, valores['Pacotes'][2])
        results[IPs[i]] = valores
    valores = {}

for i in range(len(IPs)):
    print('\n{} ->\t{}\n\t\t{}'.format(IPs[i], results[IPs[i]]['Pacotes'], results[IPs[i]]['Tempo']))
