from random import randint

numbers = ["Jedynka", "Dwójka", "Trójka", "Czwórka", "Piątka", "Szóstka"]
arr_random = []
for i in range(0, 100):
    arr_random.append(randint(1, 6))

for i in range(1, 7):
    print("{}: {}".format(numbers[i-1], arr_random.count(i)))