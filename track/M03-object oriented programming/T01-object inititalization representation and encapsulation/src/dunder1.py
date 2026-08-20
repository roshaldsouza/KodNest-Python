class Student:
    def set_roll(self,roll,name,age,marks):
        self.__roll = roll
        self.__name = name
        self.__age = age
        self.__marks = marks
    

    def get_values(self,roll,name,age,marks):
        return self.__roll
        self.__name
        self.__age
        self.__marks

    def study(self):
        print(self.__name,"is studying")

roll = int(input())
name = input().strip()
age = int(input())
marks = int(input())

s1 = Student(roll, name, age, marks)
s1.study()
print(s1.get_roll())
print(s1.get_name())
print(s1.get_age())
print(s1.get_marks())


roll2 = int(input())
name2 = input().strip()
age2 = int(input())
marks2 = int(input())

s2 = Student(roll2, name2, age2, marks2)
s2.study()
print(s2.get_roll())
print(s2.get_name())
print(s2.get_age())
print(s2.get_marks())