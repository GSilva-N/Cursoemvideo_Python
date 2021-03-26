def notasAluno(* notas, situacao=False):
    resultado = dict()
    resultado['Total de notas'] = len(notas)
    resultado['Maior'] = max(notas)
    resultado['Menor'] = min(notas)
    resultado['Média'] = sum(notas)/len(notas)

    if situacao == True:
        if resultado['Média'] < 6:
            resultado['Situação'] = 'Ruim'
        elif resultado['Média'] > 6 and resultado['Média'] < 8:
            resultado['Situação'] = 'Boa'
        elif resultado['Média'] > 8 and resultado['Média'] < 10:
            resultado['Situação'] = 'Excelente'

    return resultado


print(notasAluno(5.5, 4.7, 9, situacao=True))
