import random

def jogar_adivinhacao():
    numero_secreto = random.randint(1, 10)

    while True:
        try:
            palpite = int(input("Adivinhe um número entre 1 e 10: "))
            if 1 <= palpite <= 10:
                if palpite == numero_secreto:
                    print("Parabéns! Você acertou o número.")
                    break
                else:
                    print("Número incorreto. Tente novamente.")
            else:
                print("Por favor, insira um número entre 1 e 10.")
        except ValueError:
            print("Por favor, insira apenas números inteiros.")

jogar_adivinhacao()
