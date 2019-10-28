nums = []
sum = 0
with open('numbersinrows.txt', 'r') as f:
    for l in f:
        for i in l.split(','):
            nums.append(int(i))
for i in nums:
    sum += i
    
print("Liczb: {}\nSuma: {}".format(len(nums), sum))