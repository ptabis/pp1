wzrost = int(input('Podaj wzrost(cm): '))
waga = float(input('Podaj wagę(kg): '))
assert type(wzrost) == int and type(waga) == float and 220 < wzrost < 150 and 150.0 < waga < 40.0, 'Niepoprawne dane'
print(f'bmi = {waga / wzrost**2}')