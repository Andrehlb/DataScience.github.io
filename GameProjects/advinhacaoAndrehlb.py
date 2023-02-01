print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
while(total_de_tentativas > 0):
    chute_str = input("Digite teu número: ")
    print("Você digitiou: ", chute_str)
    chute = int(chute_str)

"""chute_str = input("Digite o seu número: ")"""
print("Você digitou: ", chute_str)
chute = int(chute_str)
acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto
if (acertou):
    print("Parabéns, você acertou!")
else:
    if(maior):
        print("Chute errado! Foi maior que o número secreto.")
    elif(menor):
        print("Chute errado! Foi menor que o número secreto.")
print("Fun de Jogo! | O tipo de variável de chute é: ", type(chute))


"""
# Idade
idade_str = input("Digite sua idade: ")
idade = int(idade_str)
if(idade > 18):
    print("Você é maior de idade.")
else:
    if(idade < 12):
        print("Você é uma criança.")
    elif(idade > 12):
        print("Você é um adolescente.") 
"""
        
