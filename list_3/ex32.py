try:
    amount = int(input('Enter the withdrawal amount (between 10 and 600): '))
    if amount < 10 or amount > 600:
        raise ValueError

    notes_100 = amount // 100
    remainder = amount % 100

    notes_50 = remainder // 50
    remainder = remainder % 50

    notes_10 = remainder // 10
    remainder = remainder % 10

    notes_5 = remainder // 5
    notes_1 = remainder % 5

    print(f'Withdrawal amount: R$ {amount}')
    if notes_100 > 0:
        print(f'R$ 100 notes: {notes_100}')
    if notes_50 > 0:
        print(f'R$ 50 notes: {notes_50}')
    if notes_10 > 0:
        print(f'R$ 10 notes: {notes_10}')
    if notes_5 > 0:
        print(f'R$ 5 notes: {notes_5}')
    if notes_1 > 0:
        print(f'R$ 1 notes: {notes_1}')
except ValueError:
    print('invalid value')
