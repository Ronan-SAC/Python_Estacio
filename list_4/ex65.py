try:
    debt = float(input('Enter debt amount: '))
    if debt <= 0:
        raise ValueError

    installments_options = [
        (1, 0),
        (3, 10),
        (6, 15),
        (9, 20),
        (12, 25)
    ]

    print(f"{'Valor da Dívida':<18} {'Valor dos Juros':<18} {'Quantidade de Parcelas':<25} {'Valor da Parcela':<18}")

    for installments, interest_pct in installments_options:
        interest_val = debt * (interest_pct / 100)
        total_debt = debt + interest_val
        installment_val = total_debt / installments

        str_debt = f"R$ {total_debt:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        str_interest = f"{interest_val:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.') if interest_val > 0 else "0"
        str_installment = f"R$ {installment_val:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

        print(f"{str_debt:<18} {str_interest:<18} {installments:<25} {str_installment:<18}")

except ValueError:
    print('invalid value')
