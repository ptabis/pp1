val = int(input("Podaj kwotę w zł: "))
rest = val

if rest < 5:
    fives = 0
else:
    fives = int(rest%5)
    while rest < fives*5:
        fives -= 1
    if fives == 0:
        fives = int(rest / 5)

    rest = rest - 5*fives

if val < 2 or rest < 2:
    twos = 0
else:
    twos = int(rest%2)
    if twos == 0:
        twos = int(rest/2)
    rest = rest - 2*twos

ones = rest
if ones < 0:
    ones = 0

print("Kwota {} zł w monetach: ".format(val))
print("5 zł - {} szt".format(fives))
print("2 zł - {} szt".format(twos))
print("1 zł - {} szt".format(ones))
