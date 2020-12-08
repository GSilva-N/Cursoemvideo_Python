numeros = list()

for i in range(0, 5):
    numeros.append(int(input('Digite um numero: ')))

maior = max(numeros)
menor = min(numeros)

for i, valor in enumerate(numeros):
    if numeros[i] == maior:
        print(f'O maior valor é {maior} e está na posição {i}!')

    if numeros[i] == menor:
        print(f'O menor valor é {menor} e está na posição {i}!')
