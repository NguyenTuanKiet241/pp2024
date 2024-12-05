def InputOfStudentInClass():
    numberOfStudents = int(input("Enter number of Students: "))
    for i in range(1, numberOfStudents + 1):
        id = input(f"Enter id of student {i}: ")
        name = input(f"Enter name of student {i}: ")
        dob = input(f"Enter DoB of student {i}: ")
        listOfStudents.append([id, name, dob])

def InputOfCoursesInClass():
    numberOfCourses = int(input("Enter number of Courses: "))
    for i in range(1, numberOfCourses + 1):
        id = input(f"Enter id of course {i}: ")
        name = input(f"Enter name of course {i}: ")
        listOfCourses.append([id, name])

def MarkForStudent():
    nameOfCourse = (input("Enter name of Courses: "))
    listScore = []
    for i in range(1, len(listOfStudents) + 1):
        score = int(input(f"Enter score of student {i}: "))
        listScore.append(score)
    dictOfMarks[nameOfCourse] = listScore
    
def ListCourses():
    for course in listOfCourses:
        print(f"Course: {course[0]} - {course[1]}")

def ListStudents():
    for student in listOfStudents:
        print(f"Student {student[0]}: {student[1]} - {student[2]}")

def MarkStudents():
    nameOfCourse = (input("Enter name of Courses to mark: "))
    print(dictOfMarks[nameOfCourse])

listOfStudents = []
listOfCourses = []
dictOfMarks = {}

while (True):
    print("------------")
    print("Student Mark Management:")
    print("1.Add Students")
    print("2.Add Courses")
    print("3.Add Marks to student for selected Course")
    print("4.Print all couress info")
    print("5.Print all students info")
    print("6.Check all marks for selected coures")
    print("7.Exit")
    print("---")
    choose = int(input("Your choose: "))

    if choose == 1:
        numberOfStudents = InputOfStudentInClass()

    if choose == 2:
        numberOfCourses = InputOfCoursesInClass()

    if choose == 3:
        MarkForStudent()

    if choose == 4:
        ListCourses()

    if choose == 5:
        ListStudents()

    if choose == 6:
        MarkStudents()

    if choose == 7:
        break

    print()