try:
    all_sides = []
    first_side = float(input('Type the first side of the triangle: '))
    second_side = float(input('Type the second side of the triangle: '))
    third_side = float(input('Type the third_side side of the triangle: '))
    
    all_sides.append(first_side)
    all_sides.append(second_side)
    all_sides.append(third_side)

    if len(set(all_sides)) == 1: print('Equilateral triangle')
    if len(set(all_sides)) == 2: print('Isosceles triangle')
    if len(set(all_sides)) == 3: print('Right triangle')
    
except ValueError:
    print('invalid value')