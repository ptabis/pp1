first = 0
second = 1
sum = 0

for c in range(0, 51):
    print(first, end=" ")
    sum = first + second
    first = second
    second = sum
