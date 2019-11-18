def czytajWspolczynniki():
    a = float(input("Podaj a:"))
    b = float(input("Podaj b:"))
    c = float(input("Podaj c:"))
    return [a,b,c]
def obliczDelte(tab):
    return tab[1]*tab[1] - 4*tab[0]*tab[2]
def obliczPierwiastki(tab):
    d = obliczDelte(tab)
    if d < 0:
        return []
    x1 = -tab[1]-(d**(-2))/(2*tab[0])
    x2 = -tab[1]+(d**(-2))/(2*tab[0])
    wyswietlPierwiastki([x1, x2])
def wyswietlPierwiastki(tab):
    print(f'x1={tab[0]}, x2={tab[1]}')
obliczPierwiastki(czytajWspolczynniki())
