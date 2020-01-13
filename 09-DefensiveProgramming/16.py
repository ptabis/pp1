from random import randint
def rzut():
    return randint(1, 6)
a = rzut()
assert 0 < a < 7 and type(a) == int, "Złe wartości"