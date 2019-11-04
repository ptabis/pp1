def jestImie(imie, imiona):
    print("Imiona: {}".format(imiona))
    print("Imię: {}".format(imie))
    print("Rezultat: ", end="")
    if imie in imiona:
        print("Imię zawarte jest w wykazie imion.")
    else:
        print("Imię nie jest zawarte w wykazie imion.")
t = ['Janek', 'Ania', 'Wojtek', 'Zosia']
jestImie('Wojtek', t)