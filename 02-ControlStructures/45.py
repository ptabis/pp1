N = int(input("Ile liczb pierwszych znaleźć: "))
dividors = 0
print("Liczby pierwsze:", end=" ")
for i in range(2, N):# 1 nie jest liczbą pierwszą
    for j in range(1, i+1):
        if i % j == 0:
            dividors += 1
    if dividors < 3:
        print(i, end=" ")
    dividors = 0