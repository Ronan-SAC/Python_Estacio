try:
    number = float(input('insert one number: '))
    if number == 0: print('number is zero')
    print(f'The number is {'positive' if number > 0 else 'negative'}')

except ValueError:
    print('invalid value')