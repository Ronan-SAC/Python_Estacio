try:
    num = int(input('Enter an integer: '))
    predecessor = num - 1
    successor = num + 1

    print(f'Number: {num}')
    print(f'Predecessor: {predecessor}')
    print(f'Successor: {successor}')
except ValueError:
    print('invalid value')
