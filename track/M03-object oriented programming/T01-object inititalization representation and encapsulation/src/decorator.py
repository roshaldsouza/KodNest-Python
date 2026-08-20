class Student:
    def __init__(self, roll, name):
        self.__roll = roll if roll > 0 else None 
        print("enter correct roll no")
        self.__name = name
    @property
    def roll(self):
        return self.__roll
    @property
    def name(self):
        return self.__name
s1 = Student(11, "Arun")
print(s1.roll)
print(s1.name)

