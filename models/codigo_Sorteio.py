import random

frutas = ['Laranja', 'Limão', 'Manga', 'Banana','Melão', 'Abacate', 'Uva', 'Maçã', 'Pitomba','Acerola', 'Goiaba' ,'Siriguela']
lista_sorteio = []

#def validar_deposito(deposito):
    #if deposito.isdecimal(): 
        #return True
    #else:
        #return False   
def deposito_isnumber(deposito):
    try:
        float(deposito)
    except ValueError:
        return False
    return True

#def validar_aposta(aposta):
    #if aposta.isdecimal():
        #return True
    #else:
        #return False
def aposta_isnumber(aposta):
    try:
        float(aposta)
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
saldo = ''

deposito = float(deposito)




while deposito_isnumber(deposito) is False:
    print('\neii sibite baleado aqui só aceita números seu lezado !!!')
    deposito = input('digite o deposite o valor do deposito:')
aposta = input('digite o valor da aposta: ')

while aposta_isnumber(aposta) is False:
    print('\neii fi da chupi-chupi é pra digitar números !!!')
    aposta = input('digite o valor da aposta: ')

while verificar_aposta(aposta,deposito) is False:
    print('diabéisso macho, deixa de ser lizeira deposita mais')
    deposito = input('digite o valor do deposito: ')


#print('iniciar jogo')


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
    saldo = aposta + saldo
    print('\nvixi mah nem deu, só sobrou o buraco e a catinga',saldo)
else:
    saldo -= aposta
    print(saldo)