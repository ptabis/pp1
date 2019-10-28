with open('NoEducation.txt', 'r') as f:
    i = 0
    for line in f:
        i += 1
        print("{} {}".format(i,line), end='')
