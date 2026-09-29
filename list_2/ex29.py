try:
    height = float(input('how tall are you: '))
    gender = str(input('Insert "M" for male or "F" for female: ')).upper()
    match gender:
        case 'M':
            weight = (72.7*height) - 58
            print(f'your ideal weight is {weight}')
        case 'F':
            weight = (62.1*height) - 44.7
            print(f'your ideal weight is {weight}')
        case _:
            ValueError

except ValueError:
    print('invalid value')