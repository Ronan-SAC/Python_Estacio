try:
    purchasing = float(input('Please state the purchasing power of the product: ')) 
    if purchasing < 50: sale_value = purchasing + (purchasing * 0.45)
    else: sale_value = purchasing + (purchasing * 0.30)

    print(f'sale value: {sale_value} ')

except ValueError:
    print('value invalid')