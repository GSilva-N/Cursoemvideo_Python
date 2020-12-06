import random

print('Vou pensar em um número entre 0 e 5. Tente adivinhar')
sorteado = random.randint(0, 5)

numero = int(input('Qual numero pensei? '))

if sorteado == numero:
    print('ACERTOOOUUU!')
else:
    print('ERROOOOOOOUUU!')
    print('Eu pensei no numero {}'.format(sorteado))
