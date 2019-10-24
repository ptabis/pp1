for i in range(1, 8):
    for j in range(1, 8):
        print("{0:>3}".format(i+(7*(j-1))), end="")
    print()
