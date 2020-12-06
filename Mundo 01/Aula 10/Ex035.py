ladoA = int(input('Valor do lado A: '))
ladoB = int(input('Valor do lado B: '))
ladoC = int(input('Valor do lado C: '))

if ladoA+ladoB > ladoC and ladoA+ladoC > ladoB and ladoC+ladoB > ladoA:
    print('É posivel formar um triânglo!')
else:
    print('Não é posivel formar um triânglo!')
