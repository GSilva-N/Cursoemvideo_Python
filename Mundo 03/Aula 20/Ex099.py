def maior(* numeros):
    cont = maior = 0
    print("Analisando o maior numero")

    for valor in numeros:
        print(f'{valor}')

        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'O maior valor informado é {maior}')


# Programa Principal
maior(0, 2, 6)
