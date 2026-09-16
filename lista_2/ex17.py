try:
    salary = float(input('enter your salary: '))
    if salary < 0: raise ValueError
    match salary:
        case salary if salary <= 280:
            increase = salary*0.20
            print(f'his salary was {salary}')
            print(f'had an increase of {increase}')
            salary = salary + increase
            print(f'and now it is {salary}')
        case salary if salary > 280 and salary <= 700:
            increase = salary*0.15
            print(f'his salary was {salary}')
            print(f'had an increase of {increase}')
            salary = salary + increase
            print(f'and now it is {salary}')
        case salary if salary > 700 and salary <= 1500:
            increase = salary*0.10
            print(f'his salary was {salary}')
            print(f'had an increase of {increase}')
            salary = salary + increase
            print(f'and now it is {salary}')
        case salary if salary > 1500:
            increase = salary*0.05
            print(f'his salary was {salary}')
            print(f'had an increase of {increase}')
            salary = salary + increase
            print(f'and now it is {salary}')
except ValueError:
    print('invalid value')