students = []
with open('students.txt', 'r') as f:
    for l in f:
        students.append(l.split(','))
for i in range(1, len(students)):
    if int(students[i][2]) < 30:
        print("{}\t{}\t{}".format(students[i][0], students[i][1], students[i][-1]), end="")
        