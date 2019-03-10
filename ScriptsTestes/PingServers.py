import os
from platform import system as system_name # Retorna o nome do Sistema Operacional
from os import system as system_call       # Executa um comando no Shell


#Função que realiza o ping no host
def ping(host, quant):
    if(system_name().upper() == "WINDOWS"):
        parametros = ("-n %s" %quant)
    else:
        parametros = ("-c %s" %quant)
        
    return system_call("ping " + parametros + " " + host) == 0


hostname = input("\nInforme o Host: ")
quant = int(input("\nQuantidade de vezes que irá pingar: "))

if(ping(hostname, quant)):
    print("\n%s está ONLINE.\n" %hostname)
else:
    print("\n%s está OFFLINE.\n" %hostname)
