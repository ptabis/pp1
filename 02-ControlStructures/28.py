a = 4
b = 15

for y in range(1, a+1):
    for x in range(1, b+1):
        if y == 1 or y == a or x == 1 or x == b: 
            print("*", end="")
        else:
            print(" ", end="")
    print("")