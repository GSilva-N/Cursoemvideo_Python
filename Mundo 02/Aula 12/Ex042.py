ladoA = int(input('Valor do lado A: '))
ladoB = int(input('Valor do lado B: '))
ladoC = int(input('Valor do lado C: '))

if ladoA+ladoB > ladoC and ladoA+ladoC > ladoB and ladoB+ladoC > ladoA:
    if ladoA == ladoB == ladoC:
        print('\nTriangulo equilatero')
    elif ladoA == ladoB or ladoA == ladoC or ladoC == ladoB:
        print('\nTriangulo isóceles')
    else:
        print('\nTriangulo escalenos')
else:
    print('\nNão é possivel formar um triangulo')
