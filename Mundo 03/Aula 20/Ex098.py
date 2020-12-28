def contador(i, f, p):
    for num in range(1, 11):
        print(num, end=' ')
    print()

    for num2 in range(10, 0, -1):
        print(num2, end=' ')
    print()

    for num3 in range(i, f-1, p):
        print(num3, end=' ')


contador(100, 0, -10)
