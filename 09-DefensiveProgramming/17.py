dni = ['Pon', 'Wt', 'Śr', 'Czw', 'Pt']
dzien = int(input('Podaj numer dnia tygodnia: '))
assert 0 < dzien < 8, '1-7'
print(dni[dzien-1])