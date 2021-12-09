import random

frutas = ['Laranja', 'Limão', 'Manga', 'Banana','Melão', 'Abacate', 'Uva', 'Maçã', 'Pitomba','Acerola', 'Goiaba' ,'Siriguela']
lista_sorteio = []

 
def deposito_isnumber(deposito):
    try:
        float(deposito)
        if 0.1 <= deposito < 1.0:
            return False
    except ValueError:
        return False
    return True


def aposta_isnumber(aposta):
    try:          
        float(aposta)
        if 0.1 <= aposta < 1.0:
            return False
    except ValueError:
        return False
    return True        

def verificar_aposta(aposta,deposito):
    aposta = float(aposta)
    deposito = float(deposito)
    if aposta <= deposito :    
        return True
    else:
        return False


# codigo 
nome_jogador = input('digite seu nome:')
deposito = input('digite o valor do deposito:')
deposito = deposito.replace(',','.')
saldo = deposito

deposito = float(deposito)
saldo = float(saldo)



while deposito_isnumber(deposito) is False:
    print('\neii sibite baleado aqui só aceita números seu lezado !!!')
    deposito = input('digite o deposite o valor do deposito:')
    deposito = deposito.replace(',','.')
    
aposta = input('digite o valor da aposta: ')
aposta = aposta.replace(',','.')
aposta = float(aposta)


while aposta_isnumber(aposta) is False:
    print('\neii fi da chupi-chupi é pra digitar números !!!')
    aposta = input('digite o valor da aposta: ')
    aposta = aposta.replace(',','.')

while verificar_aposta(aposta,deposito) is False:
    print('diabéisso macho, deixa de ser lizeira deposita mais')
    print('O seu saldo: R${:.2f}'.format(saldo))
    print('O seu aposta: R${:.2f}'.format(aposta))
    deposito = input('digite o valor do deposito: ')
    saldo = deposito + saldo




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
    saldo = aposta - saldo
    print('\nvixi mah nem deu, só sobrou o buraco e a catinga',saldo)
else:
    saldo -= aposta
    print(saldo)