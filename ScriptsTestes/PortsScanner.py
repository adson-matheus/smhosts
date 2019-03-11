import socket

def faixaPortas():
    hostIp = input("Endereço IP ou endereço do site: ")
    ports = []
    portsOpen = []
    nPortsIni = int(input("\nValor da porta Inicial: "))
    nPortsFim = int(input("Valor da porta Final: "))

    for i in range(nPortsIni, (nPortsFim+1)):
        ports.append(i)

    print("\nPor favor, aguarde!\nVerificando Portas...\n\n")
    for port in ports:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.settimeout(0.3)
        conexao = cliente.connect_ex((hostIp, port))

        if(conexao == 0):
            portsOpen.append(port)
            
    print("\t\tQUANTIDADE DE PORTAS ABERTAS:\n")
    tamPortsOpen = len(portsOpen)

    if(tamPortsOpen == 0):
        print(">> [Não há portas abertas dentro dessa faixa.]")
        
    else:
        for i in range(tamPortsOpen):
            print("\t\tPorta >>>", portsOpen[i])


def portaIndividual():
    hostIp = input("\nEndereço IP ou endereço do site: ")
    ports = []

    x = int(input("Quantidade de portas á serem escaneadas: "))
    i = 0
    print("")
    while(i < x):
        ports.append(int(input("Digite a {} porta: ".format(i+1))))
        i += 1
    print("")
    for port in ports:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.settimeout(0.3)
        conexao = cliente.connect_ex((hostIp, port))

        if(conexao == 0):
            print("\t\t %d\t>>>\tPorta aberta" %port)
        else:
            print("\t\t %d\t>>>\tPorta fechada" %port)


##print("\n\t\t[1] = VERIFICAR UMA FAIXA DE PORTAS")
##print("\t\t[2] = VERIFICAR UMA QUANTIDADE 'X' DE PORTAS")
##    
##opcao = int(input("\nInforme a sua opcao: "))
opcao = 2
if(opcao == 1):
    faixaPortas()
elif(opcao == 2):
    portaIndividual()
else:
    print("\n>:> ERRO: Opção inválida!")

print("\n------------------------\n")
