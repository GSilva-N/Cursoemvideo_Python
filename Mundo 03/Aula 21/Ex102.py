def fatorial(num, show=False):
    fat = 1
    if show == True:
        for i in range(num, 0, -1):
            fat *= i
            print(i, end=' ')
            if i > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')

        return fat

    else:
        for i in range(num, 0, -1):
            fat *= i
        return fat


print(fatorial(9, show=True))
