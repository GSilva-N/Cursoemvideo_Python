# Calcular a hipotnusa de um triangulo retangulo
from math import sqrt, pow

catetoOposto = int(input('Cateto Oposto: '))
catetoAdjacente = int(input('Cateto Adjacente: '))

hipotenusa = sqrt(pow(catetoOposto, 2)+pow(catetoAdjacente, 2))

print('Hipotenusa vale {:.2f}'.format(hipotenusa))
