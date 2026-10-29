try:
    evens = 0
    odds = 0

    for i in range(1, 11):
        num = int(input(f'Enter integer {i}/10: '))
        if num % 2 == 0:
            evens += 1
        else:
            odds += 1

    print(f'Even numbers: {evens}')
    print(f'Odd numbers: {odds}')
except ValueError:
    print('invalid value')
