try:     
    value_hour = float(input('enter your hourly rate: '))
    number_hours = int(input('Enter the number of hours worked per month: '))

    gross_salary = number_hours * value_hour

    match gross_salary:
        case gross_salary if gross_salary <= 900:
            IR = 1
            IR_print = 0
        case gross_salary if gross_salary > 900 and gross_salary <= 1500:
            IR = 0.05
            IR_print = 5
        case gross_salary if gross_salary > 1500 and gross_salary <= 2500:
            IR = 0.10
            IR_print = 10
        case gross_salary if gross_salary > 2500:
            IR = 0.20
            IR_print = 20

    IR_result = gross_salary*IR
    INSS = gross_salary*0.10
    FGTS = gross_salary*0.11
    total = IR_result + INSS
    liquid_salary = gross_salary - total

    print(f'gross_salary: ({number_hours} * {value_hour}) :R$ {gross_salary}')
    print(f'IR ({IR_print}%) :R$ {IR_result}')
    print(f'INSS (10%) :R$ {INSS}')
    print(f'FGTS (11%) :R$ {FGTS}')
    print(f'total_discount :R$ {total}')
    print(f'liquid salary :R$ {liquid_salary}')

except ValueError:
    print('invalid value')