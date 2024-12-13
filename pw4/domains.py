class Object:
    def __init__(self, id, name):
        self._id = id
        self._name = name

class Student(Object):
    def __init__(self, id, name, dob):
        super().__init__(id, name)
        self.__dob = dob

    def getId(self):
        return self._id
    
    def getName(self):
        return self._name
    
    def addScore(self, score):
        self.__score = score

    def getScore(self):
        return self.__score

    def __str__(self) -> str:
        return f"Student {self._id}: {self._name} - {self.__dob}"

class Course(Object):
    def __init__(self, id, name):
        super().__init__(id, name)

    def addMark(self, scoreList):
        self.__scoreList = scoreList

    def getMark(self):
        return self.__scoreList

    def printMark(self):
        print(self.__scoreList)

    def __str__(self) -> str:
        return f"Course {self._id}: {self._name}"