try:
    num = int(input('Enter a non-negative integer: '))
    if num < 0:
        raise ValueError

    if num == 0:
        print('0! = 1')
    else:
        factorial = 1
        factors = []
        for i in range(num, 0, -1):
            factorial *= i
            factors.append(str(i))

        breakdown = '.'.join(factors)
        print(f'{num}! = {breakdown} = {factorial}')
except ValueError:
    print('invalid value')
