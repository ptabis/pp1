a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))

delta = b*b - 4 * a *c

if delta == 0:
    x = (-b)/(2*a)
    print("Jedno miejsce zerowe: {}".format(x))
elif delta > 0:
    x1 = (-b-(delta**(-2)))/(2*a)
    x2 = (-b+(delta**(-2)))/(2*a)
    print("Dwa miejsca zerowe: {}, {}".format(x1, x2))
else:
    print("Brak miejsc zerowych.")