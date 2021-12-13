import os 
import time


inicio = True

def limpar_tela():
    if os.name =='nt':
        os.system("cls")
    else:
        os.system("clear")

def deposito_isnumber(deposito):
    try:
        deposito = float(deposito)
        if 0.0 <= deposito < 1.0: 
            return False  
    except ValueError:
        return False
    return True

def aposta_isnumber(aposta):
    try:
        aposta = float(aposta)
        if 0.0 <= aposta < 1.0:
            return False 
    except ValueError:
        return False
    return True

def verificar_aposta(aposta,deposito):
    aposta = float(aposta)
    deposito = float(deposito)
    if 0.0 <= aposta < 1.0:
        return False
    if deposito >= aposta :    
        return True
    else:
        return False



while inicio == True:
    print (35 * '=' + ' BEM VINDO ' + 35 * '='+'\n')
    print ('Esse é o sistema de apostas do Grupo Patotinhas')
    print('Desenvolvido por Rayssa Victória, Fabricio Viana, Wesley Alves, Hobson Breno e Levi.\n')
    input('Pressione o botão "ENTER" para continuar.\n')
    
    limpar_tela()
    print('\n',22 * '=' + ' Área de Cadastro '+ 22 * '='+'\n')
    nome = input(' Digite seu nome:')
    deposito = input(' Digite o valor que deseja depositar: R$ ')
    deposito = deposito.replace(',','.')
    saldo = deposito
    print('\n Verificando os dados...')   
    time.sleep(2)
    limpar_tela()

    while deposito_isnumber(deposito) is False:
        print('\n',22 * '=', ' ERRO ','='* 22)
        print('\n eii sibite baleado o deposito é inválido!!!')
        deposito = input('\n digite novamente o valor do depósito: R$ ')
        deposito = deposito.replace(',','.')
        saldo = deposito
        print('\n Verificando...')
        time.sleep(2) 
        limpar_tela()
           
    
    deposito = float(deposito)    #melhorar a mundaça de tela 
    saldo = float(saldo)

    print('\n',22 * '=' + ' Área de Aposta '+ 22 * '='+'\n') 
    print(' O seu saldo é R$ {:.2f} reais.'.format(saldo))  
    aposta = input(' Digite o valor da aposta: R$ ')
    aposta = aposta.replace(',','.')
    print('\nVerificando a aposta....')
    time.sleep(3)
    limpar_tela()
    
    while aposta_isnumber(aposta) is False:
        print('\n',22 * '=', ' ERRO ','='* 22)
        print('\n eii fi da chupi-chupi a aposta é inválido!!!')
        print(' O seu saldo é R$ {:.2f} reais.'.format(saldo))
        aposta = input('\n Digite novamente o valor da aposta: R$ ')
        aposta = aposta.replace(',','.')
        time.sleep(2)
        limpar_tela()
    
    aposta = float(aposta)

    while verificar_aposta(aposta,deposito) is False:
            if saldo >= aposta:
                time.sleep(1)
                limpar_tela()
                break
            else:
                print('\n',22 * '=', ' ERRO ','='* 22)
                print('\n Diabéisso macho, sua aposta foi maior do que seu saldo.\n')
                print(' O seu saldo é R$ {:.2f} reais.'.format(saldo))
                print(' A sua aposta foi de R$ {:.2f} reais.'.format(aposta),'\n')
                try :
                    print(' Altere o depósito ou aposta :')
                    print(' [1] depósito ou [2] aposta')
                    alterar = int(input(' Confirme aqui: '))
                    time.sleep(3)
                    limpar_tela()

                except:
                    print('\nErro, digite somente números.')
                    print(' Redirecionando...')
                    time.sleep(2)
                    limpar_tela()

                while True:
                        if alterar == 1:
                            print('\n', 15 * "=", ' Depósito ' ,15 * '=')
                            print('\n O seu saldo é R$ {:.2f} reais.'.format(saldo))
                            print(' A sua aposta foi de R$ {:.2f} reais.'.format(aposta),'\n')
                            deposito = input('\n Digite o valor do deposito: R$ ')
                            deposito = deposito.replace(',','.')
                            deposito = float(deposito)
                            saldo += deposito
                            deposito = saldo
                            print(' Verificando...')
                            time.sleep(1)
                            limpar_tela()
                            if saldo >= aposta:
                                limpar_tela()
                                break
                        if alterar == 2:
                            print('\n', 15 * "=", ' Aposta ' ,15 * '=')
                            print('\n O seu saldo é R$ {:.2f} reais.'.format(saldo))
                            print(' A sua aposta foi de R$ {:.2f} reais.'.format(aposta),'\n')
                            aposta_atual =input('\n Digite o valor que deseja apostar:')
                            aposta = aposta_atual.replace(',','.')
                            aposta = float(aposta)
                            #aposta -= aposta_atual
                            print(' Verificando...')
                            time.sleep(1)
                            limpar_tela()
                            if saldo >= aposta:
                                limpar_tela()
                                break 
    while True:
        print(22 * '=' + ' Confirmação '+ 22 * '='+'\n')
        print(' O seu saldo é R$ {:.2f} reais.'.format(saldo))
        print(' A sua aposta foi de R$ {:.2f} reais.'.format(aposta),'\n')
        try:
            print(' Confirma as informações?')
            print(' [1] sim ou [2] não')
            cont = int(input(' Confirme aqui:'))
        
        except:
            print('\n Erro, digite somente números.')
            print(' Redirecionando...')
            time.sleep(3)
            limpar_tela()     
    
        if cont == 1:
            print('saldo', saldo)
            print('deposito',deposito)
            print('aposta',aposta)