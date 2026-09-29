try:
    number = float(input('Insert one Number: '))
    if number > 10: print('number greater than 10')
    if number < 10: print('number less than 10')
    if number == 10: print('number equal to 10')
except ValueError:
    print('value invalid')