try:
    day = int(input('Enter the day (1-30): '))
    month = int(input('Enter the month (1-12): '))

    if day < 1 or day > 30 or month < 1 or month > 12:
        raise ValueError

    days_passed = ((month - 1) * 30) + day

    print(f'Date: {day:02d}/{month:02d}')
    print(f'Days passed since the beginning of the year: {days_passed}')
except ValueError:
    print('invalid value')
