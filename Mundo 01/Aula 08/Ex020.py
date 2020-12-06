from random import shuffle  # embaralha valores de uma lista

aluno1 = str(input('Nome do 1º Aluno: '))
aluno2 = str(input('Nome do 2º Aluno: '))
aluno3 = str(input('Nome do 3º Aluno: '))
aluno4 = str(input('Nome do 4º Aluno: '))

listaAlunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(listaAlunos)
print('Ordem de apresentação é: {}'.format(listaAlunos))
