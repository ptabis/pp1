import math

x = 3.7
y = 4

sqrtX = math.sqrt(x)
powX_Y = math.pow(x, y)
rootX_Y = x**(1/y)
circle = math.pi * y * y
fact = math.factorial(y)
floor = math.floor(x)

print(f'''Pierwiastek kwadratowy z {x}: {sqrtX}\n
{x} podniesione do {y}: {powX_Y}\n
Pierwiastek {y} stopnia z {x}: {rootX_Y}\n
Koło o promieniu {y} ma pole: {circle}
Silnia z {y}: {fact}\n
Największa liczba całkowita <= {x}: {floor}
''')