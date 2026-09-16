try:
    balance = float(input('enter your balance: '))
    debt = float(input('enter your debt amount: '))
    credit = float(input('enter your credit: '))

    amount = balance - debt + credit
    if amount == 0: print('your amount is zero')
    print(f'your amount is {'positive' if amount > 0 else 'negative'}')

except ValueError:
    print('invalid value')