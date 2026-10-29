try:
    a = int(input('Enter integer A: '))
    b = int(input('Enter integer B: '))

    if a == b:
        c = a + b
    else:
        c = a * b

    print(f'Result C: {c}')
except ValueError:
    print('invalid value')
