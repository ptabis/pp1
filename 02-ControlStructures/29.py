tab = [15, 8, 31, 47, 2, 19]
print("tab: ", end="")
for el in tab:
    print(el, end=" ")
print("\ntab in reverse: ", end="")
for i in range(1, len(tab)+1):
    print(tab[len(tab)-i], end=" ")
