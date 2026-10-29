try:
    liters = float(input('Enter liters of fuel sold: '))
    fuel_type = str(input('Enter fuel type (A - Alcohol, G - Gasoline): ')).upper().strip()
    if liters <= 0:
        raise ValueError

    match fuel_type:
        case 'A':
            price_per_liter = 1.90
            discount = 0.03 if liters <= 20 else 0.05
            fuel_name = 'Alcohol'
        case 'G':
            price_per_liter = 2.50
            discount = 0.04 if liters <= 20 else 0.06
            fuel_name = 'Gasoline'
        case _:
            raise ValueError

    total_gross = liters * price_per_liter
    total_to_pay = total_gross * (1 - discount)

    print(f'Fuel: {fuel_name}')
    print(f'Liters: {liters:.2f}')
    print(f'Price per liter: R$ {price_per_liter:.2f}')
    print(f'Discount: {discount * 100:.0f}%')
    print(f'Total to Pay: R$ {total_to_pay:.2f}')
except ValueError:
    print('invalid value')
