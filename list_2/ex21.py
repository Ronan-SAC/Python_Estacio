try:
    salary = float(input('enter your salary: '))
    total_sales = int(input('enter your total sales: '))

    value_sales = salary * 0.04
    commission = value_sales * total_sales

    print(f'your commission amount: {commission}')
    print(f'your total salary amount: {salary + commission}')

except ValueError:
    print('value invalid')