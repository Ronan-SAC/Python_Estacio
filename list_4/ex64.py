import random

try:
    city_1 = {'code_city': random.randint(1, 100), 'vehicles': random.randint(500, 5000), 'traffic_accidents': random.randint(10, 500)}
    city_2 = {'code_city': random.randint(1, 100), 'vehicles': random.randint(500, 5000), 'traffic_accidents': random.randint(10, 500)}
    city_3 = {'code_city': random.randint(1, 100), 'vehicles': random.randint(500, 5000), 'traffic_accidents': random.randint(10, 500)}
    city_4 = {'code_city': random.randint(1, 100), 'vehicles': random.randint(500, 5000), 'traffic_accidents': random.randint(10, 500)}
    city_5 = {'code_city': random.randint(1, 100), 'vehicles': random.randint(500, 5000), 'traffic_accidents': random.randint(10, 500)}

    cities = [city_1, city_2, city_3, city_4, city_5]

    print("--- DADOS DAS CIDADES ---")
    for city in cities:
        print(f"Cidade {city['code_city']}: {city['vehicles']} veículos | {city['traffic_accidents']} acidentes")
    print("-" * 35)

    # 1. Maior e menor índice de acidentes de trânsito e a cidade
    highest_accidents = max(cities, key=lambda c: c['traffic_accidents'])
    lowest_accidents = min(cities, key=lambda c: c['traffic_accidents'])

    print(f"Maior índice de acidentes: {highest_accidents['traffic_accidents']} (Cidade {highest_accidents['code_city']})")
    print(f"Menor índice de acidentes: {lowest_accidents['traffic_accidents']} (Cidade {lowest_accidents['code_city']})")

    # 2. Média de veículos nas cinco cidades juntas
    total_vehicles = sum(city['vehicles'] for city in cities)
    avg_vehicles = total_vehicles / len(cities)
    print(f"Média de veículos nas 5 cidades: {avg_vehicles:.2f}")

    # 3. Média de acidentes de trânsito nas cidades com menos de 2.000 veículos
    cities_under_2000 = [city for city in cities if city['vehicles'] < 2000]
    if cities_under_2000:
        avg_accidents_under_2000 = sum(city['traffic_accidents'] for city in cities_under_2000) / len(cities_under_2000)
        print(f"Média de acidentes nas cidades com menos de 2.000 veículos: {avg_accidents_under_2000:.2f} ({len(cities_under_2000)} cidade(s))")
    else:
        print("Nenhuma cidade possui menos de 2.000 veículos de passeio.")

except ValueError:
    print('invalid value')
