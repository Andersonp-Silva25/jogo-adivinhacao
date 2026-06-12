# Jogo de adivinhação

# No jogo, o usuario precisa adivinhar um numero secreto.
# Ele pode tentar varias vezes ate acertar.

import random

secret_number = random.randint(1,10)
correct_number = 0

while secret_number != correct_number:
    correct_number = int(input("Tente adivinhar o numero secreto de 1 a 10: "))

    if correct_number < secret_number:
        print("Voce errou, o numero secreto é maior do que o numero que voce tentou")
    elif correct_number > secret_number:
        print("Voce errou, o numero secreto é menor do que o numero que voce tentou")
    else:
        print("Parabéns, voce acertou o numero secreto")