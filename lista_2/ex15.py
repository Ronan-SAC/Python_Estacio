gender = str(input('Insert "M" for male or "F" for female: ')).upper()
match gender:
    case 'M':
        print('Male')
    case 'F':
        print('Female')
    case _:
        print('insert M or F please')
