velocidade = int(input('Qual é a velociade do carro (Km/h)? '))

if velocidade > 80:
    print('Excesso de velocidade!')
    excesso = velocidade-80
    multa = float(excesso*7.00)
    print('Valor da multa R$ {:.2f}'.format(multa))
else:
    print('Siga em frente!')
