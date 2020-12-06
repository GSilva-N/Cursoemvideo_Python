tupla = ('zero', 'um', 'dois', 'três', 'quatro',
         'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

num = int(input('Digite um numero para ser lido: '))

if num > 10:
    num = int(
        input('Tente novamente! Digite um numero para ser lido entre 0 e 10: '))

print(tupla[num])
