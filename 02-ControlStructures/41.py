numbers = []
number = -1
while number != 0:
    number = int(input("Podaj liczbę: "))
    numbers.append(number)
numbers.remove(0)

len_numbers = len(numbers)
sum_numbers = 0

for i in numbers:
    sum_numbers += i

avg_numbers = sum_numbers/len_numbers

print("REZULTAT: Liczb={}, Suma={}, Średnia={}".format(len_numbers, sum_numbers, avg_numbers))