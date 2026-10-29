try:
    plate_weight = float(input('Enter the weight of the meal in kg: '))
    if plate_weight <= 0:
        raise ValueError

    price_per_kg = 59.00
    total_to_pay = plate_weight * price_per_kg

    print(f'Meal Weight: {plate_weight:.3f} kg')
    print(f'Price per kg: R$ {price_per_kg:.2f}')
    print(f'Total to Pay: R$ {total_to_pay:.2f}')
except ValueError:
    print('invalid value')
