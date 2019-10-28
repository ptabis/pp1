nums = []
with open('numbers.txt', 'r') as f:
    for l in f:
        if int(l) % 2 == 0:
            nums.append(l)
with open('evennumbers.txt', 'w') as f:
    for num in nums:
        f.write(num)