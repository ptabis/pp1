list = [32, 16, 5, 8, 24, 7]

with open('liczby.txt', 'w') as f:
    for i in list:
        f.write(str(i)+'\r\n')