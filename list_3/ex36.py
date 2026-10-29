try:
    sandwich_code = int(input('Enter sandwich code (100, 101, 102, 103): '))
    drink_code = int(input('Enter drink code (201, 202, 203): '))

    match sandwich_code:
        case 100:
            sandwich_name = 'Cachorro Quente'
            sandwich_price = 11.20
        case 101:
            sandwich_name = 'Ovo Simples'
            sandwich_price = 8.30
        case 102:
            sandwich_name = 'Bauru com Ovo'
            sandwich_price = 11.50
        case 103:
            sandwich_name = 'Hambúrguer'
            sandwich_price = 16.20
        case _:
            raise ValueError

    match drink_code:
        case 201:
            drink_name = 'Refrigerante'
            drink_price = 6.00
        case 202:
            drink_name = 'Suco'
            drink_price = 7.50
        case 203:
            drink_name = 'Água Mineral'
            drink_price = 4.70
        case _:
            raise ValueError

    total = sandwich_price + drink_price

    print(f'Sandwich: {sandwich_name} - R$ {sandwich_price:.2f}')
    print(f'Drink: {drink_name} - R$ {drink_price:.2f}')
    print(f'Total to Pay: R$ {total:.2f}')
except ValueError:
    print('invalid value')
