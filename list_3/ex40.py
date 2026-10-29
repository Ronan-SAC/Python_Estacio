try:
    salary = 1200.00
    bill1 = 200.00
    bill2 = 120.00
    penalty_rate = 0.02

    bill1_total = bill1 * (1 + penalty_rate)
    bill2_total = bill2 * (1 + penalty_rate)
    total_bills = bill1_total + bill2_total
    remaining_salary = salary - total_bills

    print(f'Initial Salary: R$ {salary:.2f}')
    print(f'Bill 1 with 2% penalty: R$ {bill1_total:.2f}')
    print(f'Bill 2 with 2% penalty: R$ {bill2_total:.2f}')
    print(f'Total Bills Paid: R$ {total_bills:.2f}')
    print(f'Remaining Salary: R$ {remaining_salary:.2f}')
except ValueError:
    print('invalid value')
