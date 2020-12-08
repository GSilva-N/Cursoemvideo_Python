valores = list()

while True:
    num = int(input('Digite um número: '))

    if num not in valores:
        valores.append(num)
    else:
        print('Valor já inserido!')

    parar = str(input('Deseja continuar [S/N]? ')).upper()
    if parar in 'N':
        break

valores.sort()
print(valores)
