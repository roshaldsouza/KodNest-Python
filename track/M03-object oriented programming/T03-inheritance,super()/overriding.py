class Developer:
    def work(self):
        print("developer is working")
    def attendMeeting(self):
        print("developer is atttending meeting")
class JavaDeveloper(Developer):
    def work(self):
        print("Java Developer is working on java")
    def dojavaproject(self):
        print("Java Developer is doing java project")

class pythonDeveloper(Developer):
    def work(self):
        print("python Developer is working on python")
    def dopythonproject(self):
        print("python Developer is doing python project")
d = Developer()
d.work()
d.attendMeeting()

j = JavaDeveloper()
j.work()
j.attendMeeting()
j.dojavaproject()

p = pythonDeveloper()
p.work()
p.attendMeeting()
p.dopythonproject()
