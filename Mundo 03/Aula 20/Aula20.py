def mostraLinha():
    print('-'*30)


mostraLinha()


def contador(* num):
    print(num)


contador(3, 2, 3)
contador(3, 2, 10, 0)


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [2, 8, 4, 1]
dobra(valores)

print(valores)
