wiek = 210
if type(wiek) != int:
    raise TypeError('Wiek powinien być liczbą całkowitą!')
if wiek < 0 or wiek > 120:
    raise ValueError('Zły przedział wiekowy!')
print(f'Masz {wiek} lat')