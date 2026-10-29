try:
    count_50 = 0
    while True:
        num = int(input('Enter an integer (0 to stop): '))
        if num == 0:
            break
        if num == 50:
            count_50 += 1

    print(f'The number 50 was entered {count_50} time(s)')
except ValueError:
    print('invalid value')
