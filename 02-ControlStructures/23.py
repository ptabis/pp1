marks = ["niedostateczny", "mierny", "dostateczny", "dobry", "bardzo dobry", "celujący"]
mark = int(input("Podaj ocenę: "))
print("Ocena słownie: {}".format(marks[mark-1]))