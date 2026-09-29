try:
    rectangle_base = float(input("Insert the base of the rectangle: "))
    rectangle_height = float(input("Insert the height of the rectangle: "))
    print('Area of rectangle: ', rectangle_base * rectangle_height)
except ValueError:
    print("Invalid number")