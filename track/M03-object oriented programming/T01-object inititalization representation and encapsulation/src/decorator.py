class Student:
    def __init__(self, roll, name):
        self.__roll = roll if roll > 0 else None 
        print("enter correct roll no")
        self.__name = name
    #calling the getter methods as attribute @property is used
    @property
    def roll(self):
        return self.__roll
    @property
    def name(self):
        return self.__name

    #in order to call the setter method as attribute @name.setter is used
    @roll.setter
    def roll(self, roll):
        self.__roll = roll
    @name.setter
    def name(self, name):
        self.__name = name
s1 = Student(11, "Arun")
print(s1.roll)
print(s1.name)
s1.roll = 12
s1.name = "suraj"
print(s1.roll)
print(s1.name)


# decorator which changes function body without changing the original function
#can perform any function or operations in decorator @property or @name.setter
#if no setter method then it will work only as read only method