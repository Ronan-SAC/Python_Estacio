try:
    odd_count = 0
    while True:
        num = int(input('Enter an integer (-999 to stop): '))
        if num == -999:
            break
        if num % 2 != 0:
            odd_count += 1

    print(f'Total odd numbers entered: {odd_count}')
except ValueError:
    print('invalid value')
