try:
    gas = 6.11
    kmh = float(input("Insert km/h: "))
    print(f"The car will spend R${(kmh / 10) * gas:.2f}")
except ValueError:
    print("Invalid number")
    