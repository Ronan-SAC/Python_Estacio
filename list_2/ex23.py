try:
    all_chickens = int(input('Enter the number of chickens: '))
    print(f'expenses: {all_chickens * 4 + all_chickens * 3.5}')

except ValueError:
    print('value invalid')