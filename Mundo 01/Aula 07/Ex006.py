from math import sqrt
num = float(input('Digite um numero: '))
dobro = num*2
triplo = num*3
raiz = sqrt(num)

print('O dobro de {} é {} \n o triplo é {} \n e a raiz quadrada é {:.3f}'.format(
    num, dobro, triplo, raiz))
