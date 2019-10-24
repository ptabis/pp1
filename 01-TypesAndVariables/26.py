height = int(input("Podaj wzrost w cm: "))
weight = int(input("Podaj wagę w kg: "))

height /= 100
bmi = weight/(height*height)
print("Wskaźnik BMI {}".format(bmi))