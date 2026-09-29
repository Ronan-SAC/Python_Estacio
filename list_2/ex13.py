try:
    number = float(input('insert one number: '))
    print(f'the number is {'odd' if number % 2 else 'pair'}')
except ValueError:
    print('value invalid')