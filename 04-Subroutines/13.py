def suma(tablica):
    print("Tablica: ", end="")
    s = 0
    for i in tablica:
        print(i, end=" ")
        s += i
    print("\nSuma wartości: {}".format(s))
suma([4,3,7,1,3])
    
    