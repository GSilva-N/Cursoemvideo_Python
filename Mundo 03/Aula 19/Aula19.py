pessoas = {'nome': 'Guilherme', 'idade': 25, 'sexo': 'M'}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

estado1 = {'UF': 'Pernambuco', 'Sigla': 'PE'}
estado2 = {'UF': 'São Paulo', 'Sigla': 'SP'}

brasil = list()
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['Sigla'])

produto = dict()
estoque = list()

for i in range(0, 3):

    produto['tipo'] = str(input('Tipo do produto: '))
    produto['marca'] = str(input('Marca do produto: '))
    produto['preço'] = float(input('Preço do produto: '))

    estoque.append(produto.copy())

print(estoque)
