# @Author: André Luiz Barbosa (Andrehlb)
# Desenvolve 2023 | GB | Alura Cursos Online
# https://github.com/Andrehlb/dvelopment.github.io/blob/main/GameProjects/jogosEscolhaAdivinhacaoForca.py#L3

#stringEJ = "Escolha teu Jogo!"
#print(len(stringEJ)) # 17 caracteres
#stringBVJF = "Bem Vindo ao Jogo da Forca!"
#print(len(stringBVJF)) # 27 caracteres
#stringBVJF = "Bem Vindo ao Jogo da Adivinhação!"
#print(len(stringBVJF)) # 33 caracteres
#stringFJ = "Fim de Jogo!"
#print(len(stringFJ))

import adivinhacaoAndrehlb
import forcaEnforcado_Andrehlb


def escolhe_jogo():
    print("*********************************")
    print("******** Escolha teu Jogo! ******")
    print("*********************************")
    print("1|Advinhação\n2|Forca")
    print("*********************************")
    jogo = int(input("Digite o número do jogo escolhido: "))
    if (jogo == 1):
        print("Jogando Advinhação")
        adivinhacaoAndrehlb.jogo_adivinhacao()
    elif(jogo == 2):
        print("Jogando Forca")
        forcaEnforcado_Andrehlb.jogar_forca()
    if(__name__ == "__main__"):
        escolhe_jogo()
        
def frases_asteriscos(stringFrase1, stringFrase2):
    tamanho = len(stringFrase1), len(stringFrase2) + 6
    print(33 * "*")
    print("*** {} ***" .format(stringFrase1.center(33 - 8)))
    print("*** {} ***" .format(stringFrase2.center(33 - 8)))
    print(33 * "*")

""" frases_asteriscos("Escolha o jogo")
print("1|Advinhação\n2|Forca")
print(33 * "*")
escolhaJogos = int(input("Digite o número do jogo escolhido: "))

if (escolhaJogos == 1):
    print("Jogando Advinhação")
    adivinhacaoAndrehlb.jogo_adivinhacao()
elif(escolhaJogos == 2):
    print("Jogando Forca")
    forcaEnforcado_Andrehlb.jogar_forca() """

 
""" frases_asteriscos("Escolha o jogo")
#line break in printing 
print("1|Advinhação\n2|Forca")
print(33 * "*")
escolhaJogos = int(input("Digite o número do jogo escolhido: "))
if (escolhaJogos == 1):
    print("Jogando Advinhação")
    jogar_adivinhacao()
elif(escolhaJogos == 2):
    print("Jogando Forca")
    jogar_forca()"""
    

print((12 + 7) * "*")
print(3 * "*", "Fim de Jogo", 3 * "*")
print((12 + 7) * "*")