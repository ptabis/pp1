from math import ceil
number = int(input("Podaj liczbę: "))
bin = ""
while number != 1:
    bin += str(number % 2)
    number = int(number/2)
bin += "1"
print(bin[::-1])
