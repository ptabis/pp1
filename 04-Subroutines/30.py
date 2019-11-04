import random

t = []
def calkowita():
    return random.randint(1, 50)
for i in range(0, 1000):
    t.append(calkowita())
c = 0
for i in t:
    if i % 2 == 0:
        c += 1
print("Dla 1000 liczb wylosowanych z przedziału <1, 50>:\nLiczby parzyste {}%\nLiczby nieparzyste: {}%".format(c/10, (len(t)-c)/10)) 