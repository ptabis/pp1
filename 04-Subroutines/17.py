import random

def rzucKostka():
    return random.randint(1, 6)
s = 0
print("Wyrzucone oczka:", end=" ")
for i in range(0,3):
    z = rzucKostka()
    s += z
    print(z, end=" ")
print("\nSuma oczek: {}".format(s))
    
    