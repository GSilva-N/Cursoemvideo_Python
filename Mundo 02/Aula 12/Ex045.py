from random import randint
from time import sleep

itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
jogador = int(input('Qual é a sua jogada? '))

print("""Opções:
[0] Pedra
[1] Papel
[2] Tesoura""")

print("JO\n")
sleep(1)
print("KEN\n")
sleep(1)
print("POOH!!!\n")

print("-="*20)
print("O computador escolheu: {}".format(itens[computador]))
print("O jogador escolheu: {}".format(itens[jogador]))
print("-="*20)

if computador == 0:
    if jogador == 0:
        print("Empate!")
    elif jogador == 1:
        print("Jogador perdeu")
    elif jogador == 2:
        print("Computador venceu")
    else:
        print("Operacao invalida")

elif computador == 1:
    if jogador == 0:
        print("Computador perdeu")
    elif jogador == 1:
        print("Empate!")
    elif jogador == 2:
        print("Jogador venceu")
    else:
        print("Operacao invalida")
elif computador == 2:
    if jogador == 0:
        print("Jogador venceu")
    elif jogador == 1:
        print("Computador venceu")
    elif jogador == 2:
        print("Empate!")
    else:
        print("Operacao invalida")
else:
    print("Operacao invalida")
