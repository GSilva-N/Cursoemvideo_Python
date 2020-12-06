from random import randint

computador = int
computador = randint(0, 10)

cont = 0
acertou = False

while not acertou:

    jogador = int(input('Qual numero o computador pensou? '))
    cont += 1
    if jogador == computador:
        acertou = True
        print('Voce acertou!')

print('Voce precisou de {} chances para acertar'.format(cont))
