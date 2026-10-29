try:
    c1 = int(input('Enter quantity of 1 cent coins: '))
    c5 = int(input('Enter quantity of 5 cents coins: '))
    c10 = int(input('Enter quantity of 10 cents coins: '))
    c25 = int(input('Enter quantity of 25 cents coins: '))
    c50 = int(input('Enter quantity of 50 cents coins: '))
    r1 = int(input('Enter quantity of 1 real coins: '))

    if any(q < 0 for q in [c1, c5, c10, c25, c50, r1]):
        raise ValueError

    total = (c1 * 0.01) + (c5 * 0.05) + (c10 * 0.10) + (c25 * 0.25) + (c50 * 0.50) + (r1 * 1.00)

    print(f'Total saved: R$ {total:.2f}')
except ValueError:
    print('invalid value')
