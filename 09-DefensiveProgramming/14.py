def pole_prostokata(a, b):
    if type(a) != int or type(b) != int or type(a) != float or type(b) != float or a < 0 or b < 0:
        raise ValueError("Złe dane")
    return a*b
pole_prostokata(3, 4)
pole_prostokata(3.1, 4.0)
pole_prostokata(3, '4')
pole_prostokata(3, -2)