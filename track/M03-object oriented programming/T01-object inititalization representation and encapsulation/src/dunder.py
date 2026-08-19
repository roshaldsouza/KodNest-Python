class Student:
    def __init__(self,roll,name,age,marks):
        self.roll = roll
        self.name = name
        self.age = age
        self.marks = marks
    def study(self):
        print(self.name,"is studying")
# Read inputs for first student
roll = int(input())
name = input().strip()
age = int(input())
marks = int(input())

s1 = Student(roll, name, age, marks)
s1.study()
print(s1.roll)
print(s1.name)
print(s1.age)
print(s1.marks)

# Read inputs for second student
roll2 = int(input())
name2 = input().strip()
age2 = int(input())
marks2 = int(input())

s2 = Student(roll2, name2, age2, marks2)
s2.study()
print(s2.roll)
print(s2.name)
print(s2.age)
print(s2.marks)