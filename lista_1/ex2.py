try:
    number = int(input("Insert a number: "))
    if number > 100:
        print("Number is > 100")
        try:
            number_2 = int(input("Insert a second number: "))
            if number_2 > 150:
                print("Number is > 150")
        except ValueError:
            print("Invalid number")
    elif number < 100:
        print("Number is < 100")
    else:
        print("Number is == 100")
except ValueError:
    print("Invalid number")
