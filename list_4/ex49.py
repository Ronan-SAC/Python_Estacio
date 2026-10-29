try:
    dollar_amount = float(input('Enter value in USD ($): '))
    exchange_rate = float(input('Enter dollar exchange rate (USD to BRL): '))

    if dollar_amount < 0 or exchange_rate <= 0:
        raise ValueError

    real_amount = dollar_amount * exchange_rate

    print(f'Value in USD: $ {dollar_amount:.2f}')
    print(f'Exchange rate: R$ {exchange_rate:.2f}')
    print(f'Value in BRL: R$ {real_amount:.2f}')
except ValueError:
    print('invalid value')
