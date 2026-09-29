try:
    name = str(input("What's your name?: "))
    age = int(input("What's your age?: "))
    if age < 0: raise ValueError
    match age:
        case age if age >= 0 and age <= 2:
            print(f'{name} you are baby')
        case age if age >= 3 and age <= 11:
            print(f'{name} you are child')
        case age if age >= 12 and age <= 21:
            print(f'{name} you are young')
        case age if age >= 22 and age <= 64:
            print(f'{name} you are adult')
        case age if age >= 65 and age <= 100:
            print(f'{name} you are old')
        case age if age > 100:
            print(f'{name} you are very old')
except ValueError:
    print('Value invalid')