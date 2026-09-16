try:
    year = int(input('enter a year: '))
    print(f'the year is {'leap_year' if year % 4 == 0 else 'not leap_year'}')
except ValueError:
    print('invalid value')