from datetime import datetime

funcionario = dict()

funcionario['nome'] = str(input('Nome do Funcionário: '))
nasc = int(input('Ano de Nascimento: '))
funcionario['idade'] = datetime.now().year - nasc
funcionario['ctps'] = int(input('Número da CTPS: '))

if funcionario['ctps'] != 0:
    funcionario['anoContrato'] = int(input('Ano de Contratação: '))
    funcionario['salario'] = float(input('Salário do Funcionário: '))
    funcionario['aposenta'] = funcionario['anoContrato'] + 35


for k, v in funcionario.items():
    print(f'{k}: {v}')
