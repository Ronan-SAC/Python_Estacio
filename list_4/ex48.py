try:
    price = float(input('Enter product price: '))
    if price <= 0:
        raise ValueError

    print('Payment options:')
    print('1 - Cash or PIX (10% discount)')
    print('2 - Credit card in cash (5% discount)')
    print('3 - 2x (normal price, no interest)')
    print('4 - 3x (normal price + 10% interest)')
    option = int(input('Select payment option (1-4): '))

    match option:
        case 1:
            final_price = price * 0.90
        case 2:
            final_price = price * 0.95
        case 3:
            final_price = price
        case 4:
            final_price = price * 1.10
        case _:
            raise ValueError

    print(f'Final price to pay: R$ {final_price:.2f}')
except ValueError:
    print('invalid value')
