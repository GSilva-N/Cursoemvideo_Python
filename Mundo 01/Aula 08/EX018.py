# Calcular seno, cosseno e tangente
from math import sin, cos, tan

angulo = float(input('Digite o angulo: '))

print('O seno de {} é {:.2f}'.format(angulo, sin(angulo)))
print('O cosseno de {} é {:.2f}'.format(angulo, cos(angulo)))
print('A tangente de {} é {:.2f}'.format(angulo, tan(angulo)))
