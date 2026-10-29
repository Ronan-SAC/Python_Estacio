try:
    weight = float(input('Enter fish weight in kg: '))
    if weight < 0:
        raise ValueError

    if weight > 50:
        excess = weight - 50
        fine = excess * 4.0
    else:
        excess = 0.0
        fine = 0.0

    print(f'Weight: {weight:.2f} kg')
    print(f'Excess: {excess:.2f} kg')
    print(f'Fine: R$ {fine:.2f}')
except ValueError:
    print('invalid value')
