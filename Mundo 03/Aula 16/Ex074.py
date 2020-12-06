from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(
    1, 10), randint(1, 10), randint(1, 10))

print(tupla)
tupla2 = sorted(tupla)

print(f'O menor numero da tupla é {tupla2[0]} e o maior é {tupla2[4]}')

# Maior valor = max(tupla)
# Menor valor = min(tupla)
