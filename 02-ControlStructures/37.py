first = int(input("Podaj pierwszą liczbę: "))
second = int(input("Podaj drugą liczbę: "))
third = int(input("Podaj trzecią liczbę: "))

arr = [first, second, third]
m = max(arr)
l = min(arr)
arr.remove(m)
arr.remove(l)
print("Mediana wynosi {}".format(arr[0]))