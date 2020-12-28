largura = float(input('Largura(em metros) do terreno: '))
comprimento = float(input('Comprimento (em metros) do terreno: '))


def area(largura, comprimento):
    area = largura*comprimento
    print(f'Área do terreno é {area} m²')


area(largura=largura, comprimento=comprimento)
