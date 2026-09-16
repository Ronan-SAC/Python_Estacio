try:
    product = float(input('enter value product: '))
    print(f'current value: {product - product*0.10}')

except ValueError:
    print('value invalid')