from input import *
import output

def MarkForStudent():
    nameOfCourse = (input("Enter name of Courses: "))
    listScore = []
    for i in range(1, len(listOfStudents) + 1):
        score = float(input(f"Enter score of student {i}: "))
        listOfStudents[i-1].addScore(i-1)
        listScore.append(math.floor(score * 10) / 10)
    listOfCourses[nameOfCourse].addMark(listScore)
    
def ListCourses():
    if len(listOfCourses) <= 0:
        print("don't have any courses")
    for course in listOfCourses:
        print(listOfCourses[course])

def ListStudents():
    if len(listOfStudents) <= 0:
        print("don't have any students")
    for student in listOfStudents:
        print(student)

def MarkStudents():
    nameOfCourse = (input("Enter name of Courses to mark: "))
    try:
        listOfCourses[nameOfCourse].printMark()
    except:
        print("don't have that course")

def CalculateGPA():
    idStudent = input("Enter id of student: ")
    studentScore = 0
    for student in listOfStudents:
        if idStudent == student.getId():
            studentScore = student.getScore()
            break
    
    total = 0
    count = 0
    for course in listOfCourses:
        total += listOfCourses[course].getMark()[student.getScore()]
        count += 1

    gpa = total/count
    global listOfGPA
    listOfGPA[idStudent] = gpa
    listOfGPA = dict(sorted(listOfGPA.items(), key=lambda item: item[1], reverse=True))
    print(listOfGPA)

def GPA():
    print(listOfGPA)

while (True):
    print("------------")
    print("Student Mark Management:")
    print("1.Add Students")
    print("2.Add Courses")
    print("3.Add Marks to student for selected Course")
    print("4.Print all couress info")
    print("5.Print all students info")
    print("6.Check all marks for selected coures")
    print("7.Calculate GPA and Sort it descending")
    print("8.Print all GPA")
    print("9.Exit")
    print("---")
    choose = int(input("Your choose: "))

    if choose == 1:
        InputOfStudentInClass()

    if choose == 2:
        InputOfCoursesInClass()

    if choose == 3:
        MarkForStudent()

    if choose == 4:
        ListCourses()

    if choose == 5:
        ListStudents()

    if choose == 6:
        MarkStudents()

    if choose == 7:
        CalculateGPA()

    if choose == 8:
        GPA()

    if choose == 9:
        break

    print()