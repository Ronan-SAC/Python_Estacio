try:
    name = input("What's your name?: ")
    eleitor_title = int(input("Insert your eleitor title: "))
    political_option = int(input("Insert your political option: "))
    print("Name: ", name)
    print("Eleitor title: ", eleitor_title)
    print("Political option: ", political_option)
except ValueError:
    print("Invalid number")