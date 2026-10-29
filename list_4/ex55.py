try:
    numbers = []
    for i in range(1, 21):
        num = float(input(f'Enter number {i}/20: '))
        numbers.append(num)

    lowest = min(numbers)
    highest = max(numbers)

    print(f'Lowest number: {lowest}')
    print(f'Highest number: {highest}')
except ValueError:
    print('invalid value')
