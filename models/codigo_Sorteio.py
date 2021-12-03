import random

frutas = ['Laranja', 'Limão', 'Manga', 'Banana','Melão', 'Abacate', 'Uva', 'Maçã', 'Pitomba','Acerola', 'Goiaba' ,'Siriguela']
lista_sorteio = []

def validar_deposito(deposito):
    if deposito.isnumeric(): 
        return True
    else:
        return False   

def validar_aposta(aposta):
    if aposta.isnumeric():
        return True
    else:
        return False

def verificar_aposta(aposta,deposito):
    aposta = float(aposta)
    deposito = float(deposito)
    if aposta <= deposito :    
        return True
    else:
        return False


# codigo 
nome_jogador = input('digite seu nome:')
deposito = input('digite o deposito:')
saldo = deposito

while validar_deposito(deposito) is False:
    print('Opa... Não consigo reconhecer o valor depositado. Por-favor deposite novamente.')
    deposito = input('digite o deposito do saldo:')

aposta = input('digite o valor da aposta: ')

while validar_aposta(aposta) is False:
    print('Opa... Não consigo reconhecer o valor da aposta. Por-favor aposte novamente.')
    aposta = input('digite o valor da aposta: ')

while verificar_aposta(aposta,deposito) is False:
    print('O saldo é insuficiente para esse valor de aposta.')
    deposito = input('digite o deposito do saldo:')


print('iniciar jogo')

saldo = float(saldo)
aposta = float(aposta)

for i in range(4):
        sorteio = random.choice(frutas)
        lista_sorteio.append(sorteio)
print(lista_sorteio)
if lista_sorteio[0] == lista_sorteio[1] and lista_sorteio[2] == lista_sorteio[3]:
    saldo += aposta * 10
    print('aposta * 10 ',saldo)
    
elif lista_sorteio[0] == lista_sorteio[1] or lista_sorteio[2] == lista_sorteio[3]:  
    saldo += aposta * 5 
    print('aposta * 5',saldo)
elif lista_sorteio[0] != lista_sorteio[1] and lista_sorteio[2] != lista_sorteio[3]:
    saldo = aposta
    print('errou todas',saldo)
else:
    saldo -= aposta
    print(saldo)