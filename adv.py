import random


def jogar_adivinhacao():

    print("================================")
    print("Bem-vindo ao Jogo da Adivinhação")
    print("================================")

    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000

    print("Selecione o nível de dificuldade:")
    print("1 - Fácil")
    print("2 - Médio")
    print("3 - Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou!")
            print("Sua pontuação foi de: {}".format(pontos))
            break
        else:
            if(maior):
                print("O chute foi maior que o número secreto.")
            elif(menor):
                print("O chute foi menor que o número secreto.")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

    print("Fim do jogo!")


if(__name__ == "__main__"):
    jogar_adivinhacao()
