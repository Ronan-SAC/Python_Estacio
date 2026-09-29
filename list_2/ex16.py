try:
    number = float(input('insert first number: '))
    number_2 = float(input('insert second number: '))
    number_3 = float(input('insert third number: '))

    bigger = max(number, number_2, number_3)
    smaller = min(number, number_2, number_3)

    print(f'the largest number is {bigger}')
    print(f'the smallest number is {smaller}')

except ValueError:
    print('invalid value')