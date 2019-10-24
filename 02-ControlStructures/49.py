days = ['PN', 'WT', 'SR', 'CZ', 'PT', 'SB', 'ND']
nl = len(days)
nrDniaTygodnia = 2

for i in days:
    print("|{0:^4}".format(i), end="")
print("|")

for i in range(1, nrDniaTygodnia+1):
        print("|{0:^4}".format(""), end="")
if nrDniaTygodnia != 0:
    for i in range(1, 8-nrDniaTygodnia):
        print("|{0:^4}".format(i), end="")
    print("|")
    for i in range(8-nrDniaTygodnia, 31):
        if i % nl-(7-nrDniaTygodnia) == 0:
            print("|{0:^4}|".format(i))
        else:
            print("|{0:^4}".format(i), end="")
    print("|")
else:
    for i in range(1, 31):
        if i % nl == 0:
            print("|{0:^4}|".format(i))
        else:
            print("|{0:^4}".format(i), end="")
    print("|")