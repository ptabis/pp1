def podatek(dochod):
    if dochod <= 5000:
        return dochod*0.17
    else:
        return (5000*0.17) + ((dochod - 5000)*0.32)
d = float(input("Podaj dochód: "))
print("Podatek należny: {}".format(podatek(d)))
