from random import choices

fruit_list = ["Laranja", "Limão", "Manga", "Banana", "Melão", "Abacate", "Uva", "Maçã", "Pitomba", "Acerola", "Goiaba", "Siriguela"]
sorteio_list = []
#inicio = True
nome = input("Escreva o seu nome: ")
saldo = float(input("Digite o valor que deseja depositar: "))
aposta = float(input("Digite o valor da sua aposta: "))


#print(sorteio_list)

#def inserir_deposito():
   # deposito = float()


while True:
    if saldo < aposta:
        print("Seu saldo é insuficiente, por favor deposite mais dinheiro.")
        continuar = input("Deseja continuar? s/n: ")

        if continuar == "n":
            break
        else:
            deposito = float(input("Digite o valor que deseja depositar: "))
            saldo += deposito
    else:

        if aposta <= saldo:
            for i in range(4):
             sorteio = choices(fruit_list)
             sorteio_list.append([fruit_list])
    
        print(sorteio)