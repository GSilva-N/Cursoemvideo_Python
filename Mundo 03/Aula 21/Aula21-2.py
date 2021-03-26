def fatorial(num):
    valor = 1
    for i in range(1, num+1, 1):
        valor *= i
    return valor


print(fatorial(9))
