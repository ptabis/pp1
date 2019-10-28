import re

komunikat = 'wtorek - 23C, środa - 17C, czwartek 25C'
cyfry = re.findall('\d{2}', komunikat)
sum = 0
for i in cyfry:
    sum += int(i)
print("Średnia temperatur wynosi: {}".format(sum/len(cyfry)))