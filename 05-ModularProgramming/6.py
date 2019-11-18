import csv
import statistics

with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    print("#{:^10}{:^10}{:^10}{:^10}"
          .format("SURNAME","NAME", "AGE", "EMAIL"))
    print("="*40)
    i = 1
    r = list(reader)
    r.pop(0)
    ages = []
    for row in r:
        print("{:^2}{:^10}{:^10}{:^10}{:^10}"
          .format(i,row[0], row[1], row[2], row[3]))
        i += 1
        ages.append(int(row[2]))
    print("Średnia wieku pracowników: {}".format(statistics.mean(ages)))
        #print(row)