try:
    count = 0
    while True:
        num = float(input('Enter a number (-1 to stop): '))
        if num == -1:
            break
        count += 1

    print(f'Total numbers entered: {count}')
except ValueError:
    print('invalid value')
