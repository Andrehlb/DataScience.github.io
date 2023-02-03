import random
#random.random()
""" para arredondar o número:
random.random() * 100 """
# função int, que irá converter o número aleatório, que é um float, em um número inteiro
int(random.random() * 100)
# função que arredonda esse número
numero_random = random.random() * 100
round(numero_random)
print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
tentativa = 1
for tentativa in range (1, total_de_tentativas + 1):
#while (total_de_tentativas > 0):
#while (total_de_tentativas >= tentativa):
    #print("Tentativa", tentativa, "de", total_de_tentativas)
    print("Tentativa {} de {}".format(tentativa, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    #chute_str = input("Digite teu número: ")
    print("Você digitiou: ", chute_str)
    chute = int(chute_str)
    if(chute < 1 or chute > 100):
        print ("Vocês deve digitar um número entre 1 e 100!")
        continue
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    if (acertou):
        print("Parabéns, você acertou!")
        break
    else:
        if(maior):
            print("Chute errado! Foi maior que o número secreto.")
        elif(menor):
            print("Chute errado! Foi menor que o número secreto.")
    total_de_tentativas = total_de_tentativas - 1
    tentativa = tentativa + 1
print("Fim de Jogo!")
#print("O tipo de variável de chute é: ", type(chute))
# @Author: André Luiz Barbosa (Andrehlb)
# Desenvolve 2023 | GB | Alura Cursos Online
# Path: #https://github.com/Andrehlb/dvelopment.github.io/blob/main/GameProjects/advinhacaoAndrehlb.py#L34
print("**************")

