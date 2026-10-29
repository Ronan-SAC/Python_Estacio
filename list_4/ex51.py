try:
    total_sum = 0.0
    while True:
        num = float(input('Enter a number (-999 to stop): '))
        if num == -999:
            break
        total_sum += num

    print(f'Total sum: {total_sum}')
except ValueError:
    print('invalid value')
