try:
    while True:
        username = input('Enter username: ')
        password = input('Enter password: ')

        if username == password:
            print('Error: Password cannot be the same as username. Please try again.\n')
        else:
            print('User registered successfully!')
            break

except ValueError:
    print('invalid value')
