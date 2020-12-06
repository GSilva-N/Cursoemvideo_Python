numero = int(input('Escreva um numero para ser convertido: '))

print('Opções: \n[1] Binário \n[2] Octadecimal \n[3] Hexadecimal')

opcao = int(input('Digite a opção que deseja: '))

if opcao == 1:
    print('{} convertido para binário é {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para octadecimai é {}'.format(
        numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para hexagonal = {}'.format(numero, hex(numero)[2:]))
