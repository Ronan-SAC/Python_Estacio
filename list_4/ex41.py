try:
    count = float(input('insert a count: '))
    if count < 0:
        raise ValueError
    count_div3 = int(count / 3)

    willian = count - (count_div3 + count_div3)

    print(f"Valor total da conta: R$ {count:.2f}")
    print(f"Maria deve pagar: R$ {count_div3:.2f}")
    print(f"Gabriel deve pagar: R$ {count_div3:.2f}")
    print(f"Willian deve pagar: R$ {willian:.2f}")

except ValueError:
    print('invalid value')
