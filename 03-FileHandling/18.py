tab = []
with open('numbers.txt', 'r') as f:
    for line in f:
        tab.append(int(line))
tab.sort()
for i in tab:
    print(i, end=" ")