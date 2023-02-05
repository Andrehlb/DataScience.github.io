import random

def jogar_forca():
    def frases_asteriscos(stringFrase):
        tamanho = len(stringFrase) + 6
        print(35 * "*")
        print("*** {} ***" .format(stringFrase.center(33 - 8)))
        #print("*** {} ***" .format(stringFrase2.center(33 - 8)))
        print(35 * "*")
    frases_asteriscos("Bem Vindo ao Jogo da Forca!")
    palavras = ["python", "Alura", "Desenvolve", "Dados", "programação", "javascript"]
    palavra_secreta = random.choice(palavras)
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcamentos = 6
    tentativas = 0

    print("A palavra tem", len(palavra_secreta), "letras")
    print(" ".join(letras_acertadas))

    def desenhar_forca(enforcamentos):
        if enforcamentos == 6:
            print("  _______")
            print(" |/      |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("_|___")
        elif enforcamentos == 5:
            print("  _______")
            print(" |/      |")
            print(" |      (_)")
            print(" |")
            print(" |")
            print(" |")
            print("_|___")
        elif enforcamentos == 4:
            print("  _______")
            print(" |/      |")
            print(" |      (_)")
            print(" |       |")
            print(" |")
            print(" |")
            print("_|___")
        elif enforcamentos == 3:
            print("  _______")
            print(" |/      |")
            print(" |      (_)")
            print(" |      \|")
            print(" |")
            print(" |")
            print("_|___")
        elif enforcamentos == 2:
            print("  _______")
            print(" |/      |")
            print(" |      (_)")
            print(" |      \|/")
            print(" |")
            print(" |")
            print("_|___")
        elif enforcamentos == 1:
            print("  _______")
            print(" |/      |")
            print(" |      (_)")
            print(" |      \|/")
            print(" |       |")
            print(" |")
            print("_|___")
        else:
            print("  _______")
            print(" |/      |")
            print(" |      (_)")
            print(" |      \|/")
            print(" |       |")
            print(" |      / \\")
            print("_|___")

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
            desenhar_forca(enforcamentos)
            print("Você errou! Ainda tem", enforcamentos, "tentativas")
    
    if "_" not in letras_acertadas:
        print("Parabéns! Você ganhou!")
    else:
        print("Você perdeu! A palavra era", palavra_secreta)

jogar_forca()
