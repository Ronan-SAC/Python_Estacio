try:
    bread_qty = int(input('Enter the quantity of french breads: '))
    broa_qty = int(input('Enter the quantity of broas: '))

    if bread_qty < 0 or broa_qty < 0:
        raise ValueError

    bread_price = 1.00
    broa_price = 3.50

    total_revenue = (bread_qty * bread_price) + (broa_qty * broa_price)
    savings = total_revenue * 0.10

    print(f'French Breads: {bread_qty} un (R$ {bread_qty * bread_price:.2f})')
    print(f'Broas: {broa_qty} un (R$ {broa_qty * broa_price:.2f})')
    print(f'Total Revenue: R$ {total_revenue:.2f}')
    print(f'Savings to deposit (10%): R$ {savings:.2f}')
except ValueError:
    print('invalid value')
