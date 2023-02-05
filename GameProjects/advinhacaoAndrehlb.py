import random
#random.random()
""" para arredondar o número:
round(random.random() * 100) """
# função int, que irá converter o número aleatório, que é um float, em um número inteiro
int(random.random() * 100)
# função que arredonda esse número
numero_random = random.random() * 100
round(numero_random)
def jogar_advinhacao():
    print(33 * "*")
    #print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print(33 * "*")
    #print("*********************************")
    numero_secreto = random.randrange(1, 101)
    #numero_secreto = round(random.random() * 100)
    #numero_secreto = 42
    total_de_tentativas = 3
    print("Escolha o nível de dificuldade")
    print(" 1 - Fácil | 2 - Médio | 3 - Difícil")
    nivel = int(input("Digite o nível escolhido: "))
    
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5          
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
        pontos = 1000
        if (acertou):
            print("Parabéns, você acertou e fez {} pontos" .format(pontos))
            break
        else:
            if(maior):
                print("Chute errado! Foi maior que o número secreto.")
            elif(menor):
                print("Chute errado! Foi menor que o número secreto.")
            pontos_perdididos = abs(numero_secreto - chute)
print(33 * "*")
#print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print(33 * "*")
#print("*********************************")
numero_secreto = random.randrange(1, 101)
#numero_secreto = round(random.random() * 100)
#numero_secreto = 42
total_de_tentativas = 3
print("Escolha o nível de dificuldade")
print(" 1 - Fácil | 2 - Médio | 3 - Difícil")
nivel = int(input("Digite o nível escolhido: "))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5          
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
    pontos = 1000
    if (acertou):
        print("Parabéns, você acertou e fez {} pontos" .format(pontos))
        break
    else:
        if(maior):
            print("Chute errado! Foi maior que o número secreto.")
        elif(menor):
            print("Chute errado! Foi menor que o número secreto.")
        pontos_perdididos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdididos
    total_de_tentativas = total_de_tentativas - 1
    tentativa = tentativa + 1
    if total_de_tentativas == 0:
        print("O número era {}".format(numero_secreto))
print(12 * "*")
print("Fim de Jogo!")
print(12 * "*")
#print("O tipo de variável de chute é: ", type(chute))
# @Author: André Luiz Barbosa (Andrehlb)
# Desenvolve 2023 | GB | Alura Cursos Online
# Path: #https://github.com/Andrehlb/dvelopment.github.io/blob/main/GameProjects/advinhacaoAndrehlb.py#L34


stringBJA = "Bem vindo ao jogo de Adivinhação!"
stringFJ = "Fim de Jogo!"
print("O tamanho das strings são:", len(stringBJA), "|", len(stringFJ))
""" print("O tamanho das strings são: ", end="")
print(len(stringBJA), len(stringFJ), sep=" | ") """
#print("O tamanho das strings são: ", len(stringBJA), len(stringFJ), sep=" | ")
#print("**************")
"""stringBJA = "Bem vindo ao jogo de Adivinhação!"
    stringFJ = "Fim de Jogo!"
    print(len(stringBJA))
    print(len(stringFJ))
"""
