cena_netto = '100'

if type(cena_netto) == int or type(cena_netto) == float:
    print(f'Cena brutto z {cena_netto} zł to {cena_netto + cena_netto*0.23} zł')
else:
    raise ValueError("Całkowite lub rzeczywiste!")