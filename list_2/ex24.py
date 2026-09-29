try:
    all_sandwiches = int(input('Enter the number of sandwiches: '))
    cheese_kg = ((all_sandwiches * 2) * 50) / 1000
    ham_kg = (all_sandwiches * 50) / 1000
    hamburger_kg = (all_sandwiches * 100) / 1000

    print(f'will need cheese_kg: {cheese_kg}, ham_kg: {ham_kg} and hamburger_kg: {hamburger_kg}')

except ValueError:
    print('value invalid')