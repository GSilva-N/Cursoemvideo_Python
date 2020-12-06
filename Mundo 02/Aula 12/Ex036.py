salario = float(input('Qual é o valor do seu salário? '))
valorCasa = float(input('Qual é o valor da casa? '))
anos = float(input('Em quantos anos você deseja financiar? '))

valorParcela = valorCasa/(anos*12)
salario30 = salario*0.3

print('Para pagar uma casa de R$ {:.2f} em {} anos, o valor da parcela é R$ {:.2f}'.format(
    valorCasa, anos, valorParcela))

if valorParcela > salario30:
    print('\nEmprestimo não pode ser concedido!')
elif valorParcela <= salario30:
    print('\nEmprestimo pode ser concedido!')
