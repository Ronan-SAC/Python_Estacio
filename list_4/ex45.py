try:
    birth_year = int(input('Enter birth year: '))
    current_year = int(input('Enter current year: '))

    if current_year < birth_year or birth_year < 0:
        raise ValueError

    age_years = current_year - birth_year
    age_months = age_years * 12
    age_days = age_years * 365
    age_weeks = age_years * 52

    print(f'Age in years: {age_years}')
    print(f'Age in months: {age_months}')
    print(f'Age in days: {age_days}')
    print(f'Age in weeks: {age_weeks}')
except ValueError:
    print('invalid value')
