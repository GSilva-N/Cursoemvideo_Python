def contador(inicio, fim, passo):
    """
    -Função para contar valores e exibi-los na tela-
     parametro inicio: inicia a contagem
     parametro fim: finaliza a contagem
     parametro passo: passo da contagem
    """
    cont = inicio
    while cont <= fim:
        print(f'{cont}', end=' ')
        cont += passo


help(contador)
contador(0, 20, 5)
