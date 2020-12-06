frase = str(input('Digite uma frase: '))
palavras = frase.split()
juntar = ''.join(palavras)
inverso = ''

for letras in range(len(juntar)-1, -1, -1):
    inverso += juntar[letras]

if inverso == juntar:
    print('É um Polindromo!')
else:
    print('Não é um Polindromo!')
