names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy", "Teofil"]
longest = names[0]
for name in names:
    if len(longest) < len(name):
        longest = name
        
print("najdłuższe imię: {}".format(longest))