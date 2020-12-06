frase = str(input('Digite uma frase: ')).strip()

print('A letra A aparece {} na frase'.format(frase.upper().count('A')))
print('O 1º A aparece na posição {}'.format(frase.upper().find('A')))
print('O ultimo A aparece na posição {}'.format(frase.upper().rfind('A')))
