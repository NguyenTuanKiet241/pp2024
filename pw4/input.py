from domains import *
from math import floor
from numpy import array

listOfStudents = []
listOfGPA = {}
listOfCourses = {}

def InputOfStudentInClass():
    numberOfStudents = int(input("Enter number of Students: "))
    for i in range(1, numberOfStudents + 1):
        id = input(f"Enter id of student {i}: ")
        name = input(f"Enter name of student {i}: ")
        dob = input(f"Enter DoB of student {i}: ")
        newStudent = Student(id, name, dob)
        listOfStudents.append(newStudent)

def InputOfCoursesInClass():
    numberOfCourses = int(input("Enter number of Courses: "))
    for i in range(1, numberOfCourses + 1):
        id = input(f"Enter id of course {i}: ")
        name = input(f"Enter name of course {i}: ")
        newCourse = Course(id, name)
        listOfCourses[name] = newCourse