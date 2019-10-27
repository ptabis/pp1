from random import randint

l = randint(1,6)
a = int(input("Podaj, ile oczek wyrzucił komputer: "))
print("Komputer wyrzucił: {}".format(l))
print("Zgadłeś: {}".format(l == a))