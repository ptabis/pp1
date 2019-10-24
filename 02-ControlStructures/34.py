pesel = input("Podaj PESEL: ")
gender_male = [1, 3, 5, 7, 9]
age = pesel[0:7]
gender = ""

pesel_gender = int(pesel[-2])
pesel_age = age[0:2]
pesel_month = age[2:4]

if pesel_gender in gender_male:
    gender = "mężczyzna"
else:
    gender = "kobieta"
if int(pesel_month) > 12:
    year_born = 2000 + int(pesel_age)
else:
    year_born = 1900 + int(pesel_age)
curr_age = 2018-year_born
print("Płeć: {}".format(gender))
print("Wiek: {}".format(curr_age))