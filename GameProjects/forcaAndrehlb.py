import random


def frases_asteriscos(stringFrase):
    tamanho = len(stringFrase) + 6
    print(35 * "*")
    print("*** {} ***" .format(stringFrase.center(33 - 8)))
    #print("*** {} ***" .format(stringFrase2.center(33 - 8)))
    print(35 * "*")

frases_asteriscos("Bem Vindo ao Jogo da Forca!")

def jogar_forca():
    print("Bem-vindo ao Jogo da Forca!")
    palavras = ["python", "java", "kotlin", "javascript", "ruby"]
    palavra_secreta = random.choice(palavras)
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcamentos = 6
    tentativas = 0

    print("A palavra tem", len(palavra_secreta), "letras")
    print(" ".join(letras_acertadas))

    while enforcamentos > 0 and "_" in letras_acertadas:
        tentativa = input("Adivinhe uma letra: ").strip().lower()
        if tentativa in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if letra == tentativa:
                    letras_acertadas[index] = letra
                index += 1
            print(" ".join(letras_acertadas))
        else:
            enforcamentos -= 1
            print("Você errou! Ainda restam", enforcamentos, "tentativas")

    if "_" not in letras_acertadas:
        print("Você ganhou!")
    else:
        print("Você perdeu!")
        print("A palavra era", palavra_secreta)

jogar_forca()
