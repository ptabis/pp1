with open('numbers.txt', 'r') as f:
    sum = 0
    for line in f:
        sum += int(line)
    print("Suma = {}".format(sum))