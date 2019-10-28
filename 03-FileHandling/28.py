import re
with open('land.txt', 'r') as f:
    r = re.findall('[0-9]+', f.read())
    sum = 0
    for i in r:
        sum += int(i)
    print("Suma wynosi: {}".format(sum))
