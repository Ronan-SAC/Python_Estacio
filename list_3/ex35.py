try:
    meat_type = str(input('Enter meat type (FD - File Duplo, A - Alcatra, P - Picanha): ')).upper().strip()
    quantity = float(input('Enter meat quantity in kg: '))
    payment_type = str(input('Payment method (C - Tabajara Card, O - Other): ')).upper().strip()

    if quantity <= 0:
        raise ValueError

    match meat_type:
        case 'FD':
            meat_name = 'File Duplo'
            price_per_kg = 34.90 if quantity <= 5 else 35.80
        case 'A':
            meat_name = 'Alcatra'
            price_per_kg = 44.90 if quantity <= 5 else 46.80
        case 'P':
            meat_name = 'Picanha'
            price_per_kg = 66.90 if quantity <= 5 else 67.80
        case _:
            raise ValueError

    total_price = quantity * price_per_kg

    match payment_type:
        case 'C':
            payment_name = 'Tabajara Card'
            discount = total_price * 0.05
        case 'O':
            payment_name = 'Other'
            discount = 0.0
        case _:
            raise ValueError

    amount_to_pay = total_price - discount

    print('--------------- RECEIPT ---------------')
    print(f'Meat Type: {meat_name}')
    print(f'Quantity: {quantity:.2f} kg')
    print(f'Price per kg: R$ {price_per_kg:.2f}')
    print(f'Total Price: R$ {total_price:.2f}')
    print(f'Payment Method: {payment_name}')
    print(f'Discount: R$ {discount:.2f}')
    print(f'Amount to Pay: R$ {amount_to_pay:.2f}')
    print('---------------------------------------')
except ValueError:
    print('invalid value')
