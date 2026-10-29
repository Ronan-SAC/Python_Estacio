try:
    num1 = int(input('Enter first integer: '))
    num2 = int(input('Enter second integer: '))

    start = min(num1, num2)
    end = max(num1, num2)

    numbers = list(range(start + 1, end))
    if numbers:
        print(f'Integers between {start} and {end}:')
        for n in numbers:
            print(n, end=' ')
        print()
    else:
        print(f'No integers strictly between {start} and {end}.')
except ValueError:
    print('invalid value')
