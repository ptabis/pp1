x = 1
y = -9
if x > 0 and y > 0:
    print("Punkt P({}, {}) znajduje się w I ćwiartce".format(x,y))
elif x < 0 and y > 0:
    print("Punkt P({}, {}) znajduje się w II ćwiartce".format(x,y))
elif x < 0 and y < 0:
    print("Punkt P({}, {}) znajduje się w III ćwiartce".format(x,y))
elif x > 0 and y < 0:
    print("Punkt P({}, {}) znajduje się w IV ćwiartce".format(x,y))
elif x == 0 and y == 0:
    print("Punkt P({}, {}) znajduje się na środku układu współrzędnych".format(x,y))
elif x == 0:
    print("Punkt P({}, {}) znajduje się na osi y".format(x,y))
elif y == 0:
    print("Punkt P({}, {}) znajduje się na osi x".format(x,y))