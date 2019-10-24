sum_odd = 0
sum_even = 0
for i in range(1, 51):
    if i%2 == 0:
        sum_even += i
    else:
        sum_odd += i
print("Suma liczb parzystych: {} \nSuma liczb nieparzystych: {}".format(sum_even, sum_odd))
    