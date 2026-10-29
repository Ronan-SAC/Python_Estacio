try:
    n = int(input('Enter quantity of numbers (N): '))
    if n <= 0:
        raise ValueError

    numbers = []
    for i in range(1, n + 1):
        num = float(input(f'Enter number {i}/{n}: '))
        numbers.append(num)

    lowest = min(numbers)
    highest = max(numbers)
    total_sum = sum(numbers)

    print(f'Lowest value: {lowest}')
    print(f'Highest value: {highest}')
    print(f'Sum of values: {total_sum}')
except ValueError:
    print('invalid value')
