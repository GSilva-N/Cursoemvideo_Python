lista = list()
listaPar = list()
listaImpar = list()

while True:
    num = int(input('Digite um número: '))
    parar = str(input('Deseja continuar [S/N]? ')).upper()
    if parar in 'N':
        break

for i, valor in enumerate(lista):

    if lista[i] % 2 == 0:
        listaPar.append(lista[i])
    else:
        listaImpar.append(lista[i])

print(f'Lista geral {lista}')
print(f'Lista dos pares {listaPar}')
print(f'Lista dos impares {listaImpar}')
