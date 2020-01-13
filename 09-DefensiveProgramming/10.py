try:
    with open('NoEducation.txt', 'r') as f:
        print(f.read())
except:
    print("Cannot open the file!")