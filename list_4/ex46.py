try:
    name = str(input('Enter name: ')).strip()
    gender = str(input('Enter gender (M/F): ')).strip().upper()
    marital_status = str(input('Enter marital status (SOLTEIRO, CASADO, ETC): ')).strip().upper()

    years_married = None
    if gender == 'F' and marital_status in ('CASADA', 'CASADO'):
        years_married = int(input('Enter time married in years: '))
        if years_married < 0:
            raise ValueError

    print(f'Name: {name}')
    print(f'Gender: {gender}')
    print(f'Marital Status: {marital_status}')
    if years_married is not None:
        print(f'Years married: {years_married}')
except ValueError:
    print('invalid value')
