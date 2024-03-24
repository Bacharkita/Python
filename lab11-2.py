import sqlite3

f= open('score2.txt') 
matrix=[line.split() for line in f]

connect = sqlite3.connect('mydatabase.db')# create connection with db
c = connect.cursor()#to interact with db


c .execute(''' CREATE TABLE IF NOT EXISTS personID (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name1 TEXT,
                name2 TEXT)
                ''')

person = []

for m in matrix[:]: 
    firstName= m[2] 
    lastName= m[3]

    if (firstName, lastName) not in person:
        person.append((firstName,lastName))
#print(person)
# c .executemany("INSERT INTO personID(name1,name2) VALUES (?,?)", person)
print("#################################################################")

for row in c .execute('SELECT * FROM personID ORDER BY id'):
    print(row)


print("#################################################################")

c.execute(''' CREATE TABLE IF NOT EXISTS Scores (personId INTEGER, 
                Task INTEGER, 
                Score INTEGER,
                FOREIGN KEY (personId) REFERENCES personID (id),
                UNIQUE(Task, personId))
                ''')

connect.commit
for m in matrix[:]: 
    task = int(m[1])
    firstName= m[2] 
    lastName= m[3]
    points = int(m[4])
for id in c.execute("SELECT * FROM personID WHERE name1==? AND name2==? ",[firstName,lastName]):
    c.execute('INSERT INTO Scores(personId, Task, Score) VALUES(?,?,?)',[id[0],task,points])
    

print("#################################################################")

for row in c.execute('SELECT * FROM Scores ORDER BY Task'):
    print(row)

print("#################################################################")
for lowresult in c.execute("SELECT s.Task, SUM(s.Score) FROM Scores as s GROUP BY Task ORDER BY SUM(s.Score) ASC LIMIT 10"):
        print(lowresult)

print("#################################################################")

for hightScore in c.execute("SELECT person.name1, person.name2, SUM(s.Score) FROM personID AS person JOIN Scores AS s ON person.id = s.personId GROUP BY person.name1 ,person.name2 ORDER BY SUM(s.Score) DESC LIMIT 10 "):
    print(hightScore)
print("#################################################################")



connect.commit()
connect.close()