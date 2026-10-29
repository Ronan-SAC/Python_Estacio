try:
    numbers = []
    for i in range(1, 6):
        num = float(input(f'Enter number {i}/5: '))
        numbers.append(num)

    total_sum = sum(numbers)
    average = total_sum / len(numbers)

    print(f'Sum of numbers: {total_sum}')
    print(f'Average of numbers: {average:.2f}')

except ValueError:
    print('invalid value')
