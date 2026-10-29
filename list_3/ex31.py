try:
    shift = str(input('Enter your shift (M - Matutino, V - Vespertino, N - Noturno): ')).upper().strip()

    match shift:
        case 'M':
            print('Bom Dia!')
        case 'V':
            print('Boa Tarde!')
        case 'N':
            print('Boa Noite!')
        case _:
            print('Valor Inválido!')
except ValueError:
    print('invalid value')
