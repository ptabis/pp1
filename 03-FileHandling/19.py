unis = []
with open('universities.txt', 'r') as f:
    for l in f:
        unis.append(l)
        
unis.sort()
with open('universities.txt', 'w') as f:
    for uni in unis:
        f.write(uni)