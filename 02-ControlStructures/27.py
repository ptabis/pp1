l = int(input("Podaj szerokość piramidy: "))
if l % 2 == 0:
    center = int(l/2)
else:
    center = int(l/2)+1
for i in range(1, center+1):
    print("*"*i)
for i in range(center, l+1):
    print("*"*(l-i)) 