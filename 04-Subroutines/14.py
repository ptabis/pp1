def wystepuje(liczba, tablica):
    print("Liczba: {}".format(liczba))
    print("Tablica: ", end="")
    for i in tablica:
        print(i, end=" ")
    print("\nRezultat: ", end="")
    if liczba in tablica:
        print("Podana liczba występuje w tablicy.")
    else:
        print("Podana liczba nie występuje w tablicy.")
wystepuje(23, [15, 38, 7, 23, 14])  