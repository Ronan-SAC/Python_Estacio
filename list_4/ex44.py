try:
    num = int(input('Enter a number for the multiplication table: '))

    print(f'Multiplication table of {num}:')
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')
except ValueError:
    print('invalid value')
