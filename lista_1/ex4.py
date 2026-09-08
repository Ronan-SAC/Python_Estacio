try:
    car_name = input("What's your car name?: ")
    car_plate = input("What's your car plate?: ")
    car_model = input("What's your car model?: ")
    car_color = input("What's your car color?: ")
    print("Car name: ", car_name)
    print("Car plate: ", car_plate)
    print("Car model: ", car_model)
    print("Car color: ", car_color)
except ValueError:
    print("Invalid")