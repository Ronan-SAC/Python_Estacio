try:
    pop_a = 80000
    growth_a = 0.03
    pop_b = 200000
    growth_b = 0.015

    years = 0
    while pop_a < pop_b:
        pop_a += pop_a * growth_a
        pop_b += pop_b * growth_b
        years += 1

    print(f'População inicial País A: 80.000 habitantes (crescimento de 3.0% a.a.)')
    print(f'População inicial País B: 200.000 habitantes (crescimento de 1.5% a.a.)')
    print(f'Anos necessários: {years} anos')
    print(f'População final País A: {int(pop_a):,} habitantes')
    print(f'População final País B: {int(pop_b):,} habitantes')

except ValueError:
    print('invalid value')
