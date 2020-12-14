aluno = dict()


aluno['nome'] = str(input('Digite o nome do Aluno(a): '))
aluno['media'] = float(input('Média do Aluno(a): '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 4 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

print(aluno)
