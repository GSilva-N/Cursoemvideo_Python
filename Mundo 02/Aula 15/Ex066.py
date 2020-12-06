cont = 0
soma = 0

while True:
    num = int(input('Digite um valor (999 para parar): '))

    if num == 999:
        break

    cont += 1
    soma += num

print(f'Foram lidos {cont} valores e a soma dele é {soma}')
