try:
    books = int(input('Enter number of books purchased: '))
    if books < 0:
        raise ValueError

    if books == 0:
        points = 0
    elif books == 1:
        points = 5
    elif books == 2:
        points = 15
    elif books == 3:
        points = 30
    else:
        points = 60

    print(f'Books purchased: {books}')
    print(f'Points earned: {points}')

    if 20 <= points <= 30:
        print('Reward options: Eco Bag OR Personalized Pen')
    elif 35 <= points <= 60:
        print('Reward options: A book (up to R$ 30.00) OR Bedside lamp')
    elif points > 65:
        print('Reward options: 2 books (up to R$ 100.00) OR Power bank')
    else:
        print('No reward available for this point range.')
except ValueError:
    print('invalid value')
