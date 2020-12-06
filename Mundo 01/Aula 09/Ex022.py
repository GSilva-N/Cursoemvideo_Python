nome = str(input('Digite seu nome: ')).strip()

print('Em Maiusculo: {}'.format(nome.upper()))
print('Em Minusculo: {}'.format(nome.lower()))
print('Seu Nome Completo tem {} letras'.format(len(nome)-nome.count(' ')))

nome1 = nome.split()
print('Seu 1º nome é {} e tem {} letras'.format(nome1[0], len(nome1[0])))
