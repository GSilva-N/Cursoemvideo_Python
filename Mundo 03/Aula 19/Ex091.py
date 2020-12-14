from random import randint
jogador = dict()
resultado = list()

for i in range(0, 4):
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['jogada'] = randint(1, 6)
    resultado.append(jogador.copy())

for ver in resultado:
    print(ver)
