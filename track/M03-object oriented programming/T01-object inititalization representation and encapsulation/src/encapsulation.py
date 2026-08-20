class Student:
    def __init__(self, roll, name):
        self.__roll = roll if roll > 0 else None
        self.__name = name

    def setRoll(self, roll):
        if roll > 0:
            self.__roll = roll
        else:
            print("Invalid roll no")

    def getRoll(self):
        if self.__roll is not None and self.__roll > 0:
            return self.__roll
        else:
            return "Invalid roll no"

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name
s1 = Student(11, "Arun")
print(s1.getRoll())
print(s1.getName())


s2 = Student(-12, "Arun")
print(s2.getRoll())
print(s2.getName())
