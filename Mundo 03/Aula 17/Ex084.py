informacoes = list()
pessoas = list()

while True:

    informacoes.append(str(input('Nome: ')))
    informacoes.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        maior = menor = informacoes[1]
    else:
        if informacoes[1] > maior:
            maior = informacoes[1]
        if informacoes[1] < menor:
            menor = informacoes[1]

    pessoas.append(informacoes[:])
    informacoes.clear()

    parar = str(input('Deseja continuar [S/N]? ')).upper()
    if parar in 'N':
        break

print(f'Foram cadastradas {len(pessoas)}')

for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}', end='')
