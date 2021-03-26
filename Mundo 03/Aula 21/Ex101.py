from datetime import date


def voto(anoNasc):
    anoAtual = date.today().year
    idade = anoAtual - anoNasc

    if idade < 16:
        return "NEGADO"
    elif (idade >= 16 and idade < 18) or (idade > 65):
        return "OPCIONAL"
    else:
        return "OBRIGATÓRIO"


print(voto(2010))
