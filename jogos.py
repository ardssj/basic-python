import adv
import forca


def escolhe_jogo():

    print("==============================")
    print("Bem-vindo! Escolha o seu jogo!")
    print("==============================")

    print("1 - Jogo da Adivinhação")
    print("2 - Jogo da Forca")

    jogo = int(input("Escolha o jogo:"))

    if (jogo == 1):
        print("Jogo da Adivinhação")
        adv.jogar_adivinhacao()
    elif (jogo == 2):
        print("Jogo da Forca")
        forca.jogar_forca()


if (__name__ == "__main__"):
    escolhe_jogo()
