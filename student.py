file = open("score2.txt")
line_split = [line.split() for line in file]
students = {}
topStudent = {}
topOne = 0

def getTotalpoints(firstname, lastname, addedpoints):
    for student in students:
        if firstname + " " + lastname == student:
            point = int(students[student]) + int(addedpoints)
            students[student] = point 
            return 
        students[firstname + " " + lastname] = addedpoints

for content in line_split:
    firstname = content[2]
    lastname = content[3]
    point = content[4]
    getTotalpoints(firstname, lastname, point)

for i in students:
    print("student name: --> {} studnt point: --> {}".format(i, students[i]))
    if topOne <= students[i]:
        topOne = students[i]

for i in students:
    if students[i] == topOne:
        topOne[i] = students[i]

        print(" the top studnt's points is: ")

for i in topStudent:
    print("the top is: --> {} with points: --> {}".format(i, students[i]))
