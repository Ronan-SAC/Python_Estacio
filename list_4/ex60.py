try:
    num = int(input('Enter a number between 1 and 10: '))
    if num < 1 or num > 10:
        raise ValueError

    print(f'Tabuada de {num}:')
    for i in range(1, 11):
        print(f'{num} X {i} = {num * i}')
except ValueError:
    print('invalid value')
