while True:
    numero = int(input('Digite um numero para a Tabuada: '))

    if numero < 0:
        break

    for i in range(0, 11):
        print(f'{numero} x {i} = {numero*i}')
