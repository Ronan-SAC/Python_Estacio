try:
    small_shirts = int(input('Enter the number of small_shirts: ')) 
    average_shirts = int(input('Enter the number of average_shirts: ')) 
    big_shirts = int(input('Enter the number of big_shirts: ')) 

    print(f'total purchase value: {(small_shirts * 10) + (average_shirts * 12) + (big_shirts * 15)}')

except ValueError:
    print('value invalid')