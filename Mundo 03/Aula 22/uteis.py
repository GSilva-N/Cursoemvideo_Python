def raiz(num):
    num = num ** 0.5
    return num


def quadrado(num):
    num *= num
    return num


def fatorial(num):
    fat = 1

    for i in range(1, num+1):
        fat *= i

    return fat
