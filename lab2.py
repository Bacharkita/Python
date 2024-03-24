file = open("score2.txt")
line_split = [line.split() for line in file]
students = {}
topStudent = {}
topOne = 0

def getTotalPoints(firstname, lastname, addedPoints):
    for student in students:
        if firstname+" "+lastname == student:
            point = int(students[student]) + int(addedPoints)
            students[student] = point
            return 
        students[firstname+" "+lastname] = addedPoints
#Extracts info from the file by index
for content in line_split:
    firstname = content[2]
    lastname = content[3]
    point = content[4]
    getTotalPoints(firstname, lastname, point) # to update student's points in the dictionary 

for i in students: 
    print("Student Name: --> {} Student Points: --> {}".format(i, students[i]))
    if topOne <= students[i]:
        topOne = students[i]
#checks if the student's points match the maximum points 
# If they match, the student is considered one of the top students.
for i in students: 
    if students[i] == topOne: 
        topStudent[i] = students[i]

print("the Top student's points is")

for i in topStudent: 
    print("The Top Is: --> {} Whith Points = {}".format(i, topStudent[i]))
