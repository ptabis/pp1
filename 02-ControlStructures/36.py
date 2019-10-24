l = [2, 3, 4, 5, 6]
i = 0
found = 0
while found == 0:
    if i % 7 == 0:
        for j in l:
            if i % j == 1:
                continue
            else:
                break
            found = 1
            print("Liczba to: {}".format(i))
        if found == 1:
            break
    i += 1

    
