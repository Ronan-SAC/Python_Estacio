try:
    print('----- MENU -----')
    print('1 - Bife a Cavalo: R$ 22.00')
    print('2 - Bife Acebolado: R$ 18.00')
    print('3 - Lasanha: R$ 25.00')
    print('4 - Frango Grelhado: R$ 16.00')
    print('5 - Feijoada: R$ 30.00')
    print('----------------')

    choice = int(input('Choose an option (1-5): '))
    match choice:
        case 1:
            dish = 'Bife a Cavalo'
            price = 22.00
        case 2:
            dish = 'Bife Acebolado'
            price = 18.00
        case 3:
            dish = 'Lasanha'
            price = 25.00
        case 4:
            dish = 'Frango Grelhado'
            price = 16.00
        case 5:
            dish = 'Feijoada'
            price = 30.00
        case _:
            raise ValueError

    tip_choice = str(input('Aceita pagar a gorjeta do garcom 10% sobre o valor do prato? (S/N): ')).strip().upper()
    if tip_choice == 'S':
        final_value = price * 1.10
    elif tip_choice == 'N':
        final_value = price
    else:
        raise ValueError

    print(f'Prato escolhido: {dish}')
    print(f'Valor final: R$ {final_value:.2f}')
except ValueError:
    print('invalid value')
