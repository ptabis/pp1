number = int(input("Podaj liczbę: "))
number_names = ["zero", "jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem", "dziewięć"]
number_arr = []

for n in str(number):
    number_arr.append(int(n))

print("{} - ".format(number), end="")

for i in number_arr:
    print(number_names[i], end=" ")
