try:
    cans = int(input('Enter quantity of 350ml cans: '))
    bottles_600 = int(input('Enter quantity of 600ml bottles: '))
    bottles_2l = int(input('Enter quantity of 2L bottles: '))

    if cans < 0 or bottles_600 < 0 or bottles_2l < 0:
        raise ValueError

    total_liters = (cans * 0.35) + (bottles_600 * 0.6) + (bottles_2l * 2.0)

    print(f'Total liters purchased: {total_liters:.2f} L')
except ValueError:
    print('invalid value')
