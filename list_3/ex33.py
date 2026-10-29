try:
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    operation = str(input('Choose operation (+, -, *, /): ')).strip()

    match operation:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            if num2 == 0:
                raise ValueError
            result = num1 / num2
        case _:
            raise ValueError

    # Par ou Ímpar (definido para números inteiros)
    if result.is_integer():
        parity = 'Even' if int(result) % 2 == 0 else 'Odd'
        number_type = 'Integer'
    else:
        parity = 'Not applicable (decimal number)'
        number_type = 'Decimal'

    # Positivo ou Negativo
    if result > 0:
        sign = 'Positive'
    elif result < 0:
        sign = 'Negative'
    else:
        sign = 'Neutral (zero)'

    print(f'Result: {result}')
    print(f'Parity: {parity}')
    print(f'Sign: {sign}')
    print(f'Type: {number_type}')
except ValueError:
    print('invalid value')
