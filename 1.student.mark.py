def InputOfStudentInClass():
    for i in range(1, numberOfStudents + 1):
        id = input(f"Enter id of student {i}: ")
        name = input(f"Enter name of student {i}: ")
        dob = input(f"Enter DoB of student {i}: ")
        listOfStudents.append([id, name, dob])

def InputOfCoursesInClass():
    for i in range(1, numberOfCourses + 1):
        id = input(f"Enter id of course {i}: ")
        name = input(f"Enter name of course {i}: ")
        listOfCourses.append([id, name])

def MarkForStudent(course):
    listScore = []
    for i in range(1, numberOfStudents + 1):
        score = int(input(f"Enter score of student {i}: "))
        listScore.append(score)
    dictOfMarks[course] = listScore
    
def ListCourses():
    for i in range(numberOfCourses):
        print(f"Course {listOfCourses[i][0]}: {listOfCourses[i][1]}")

def ListStudents():
    for i in range(numberOfStudents):
        print(f"Student {listOfStudents[i][0]}: {listOfStudents[i][1]} - {listOfStudents[i][2]}")

def MarkStudents(course):
    for i in range(numberOfStudents):
        print(f"Student {listOfStudents[i][0]}: {dictOfMarks[course][i]}")

listOfStudents = []
listOfCourses = []
dictOfMarks = {}
numberOfStudents = int(input("Enter number of Students: "))
InputOfStudentInClass()
numberOfCourses = int(input("Enter number of Courses: "))
InputOfCoursesInClass()
nameOfCourse = (input("Enter name of Courses: "))
MarkForStudent(nameOfCourse)
ListCourses()
ListStudents()
nameOfCourse = (input("Enter name of Courses: "))
MarkStudents(nameOfCourse)