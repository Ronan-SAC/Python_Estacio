try:
    name = str(input('Insert your name: \n'))
    gender = str(input('Insert your gender: \n (mas-fem-n)\n insert some of these options: \n'))
    if gender == 'mas': gender = 'masculine'
    elif gender == 'fem': gender = 'feminine'
    elif gender == 'n': gender = 'non'
    else: raise ValueError
    address = str(input ('Insert your address: \n'))
    phone = int(input ('Insert yout phone (only numbers): \n'))
    ddd = phone[:2]
    rest_phone = phone[2:]
    phone = f'({ddd}) {rest_phone}'

    print('Your name is: ' + name + '\n Your gender is: ' + gender + '\n Your address is: ' + 
          address + '\n Your phone is: ' + str(phone))
        

except ValueError:
    print('Enter the correct value.')
