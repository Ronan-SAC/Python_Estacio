try:
    int1 = int(input('insert a number int: '))
    int2 = int(input('insert a number int: '))
    real = float(input('insert a number real: '))

    product = (int1*2) * int2 / 2
    print(product)
    product = (int1*3) + real
    print(product)
    product = real ** 3
    print(product)


except ValueError:
    print('invalid value')