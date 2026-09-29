try:
    triangle_perimiter1 = float(input("Insert the perimeter of the first triangle: "))
    triangle_perimiter2 = float(input("Insert the perimeter of the second triangle: "))
    triangle_perimiter3 = float(input("Insert the perimeter of the third triangle: "))
    
    print('Area of triangle 1: ', (triangle_perimiter1 * triangle_perimiter2 * triangle_perimiter3 / 2))
except ValueError:
    print("Invalid number")