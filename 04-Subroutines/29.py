def mediana(t):
    t.sort()
    return t[int(len(t)/2)]
def dominanta(t):
    return max(set(t), key=t.count)
    
tab = [2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4]
print("Tablica: {}\nDominanta: {}\nMediana: {}".format(tab, dominanta(tab), mediana(tab)))