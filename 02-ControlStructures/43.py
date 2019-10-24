n1 = int(input("Podaj pierwszą liczbę: "))
n2 = int(input("Podaj drugą liczbę: "))
n3 = int(input("Podaj trzecią liczbę: "))

numbers = [n1, n2, n3]

c = 0
while True:
    if c+1 == len(numbers):
        break
    if numbers[c] < numbers[c+1]:
        c += 1
    else:
        d = numbers[c]
        numbers[c] = numbers[c+1]
        numbers[c+1] = d
        c = 0
print("Liczby w kolejności rosnącej: {}".format(numbers))