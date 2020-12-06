numero = int(input('Digite um numero para ver a sua tabuada: '))

for i in range(0, 11):
    print('{} x {} = {}'.format(numero, i, i*numero))
