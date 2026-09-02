class Developer:
    def work(self):
        pass
class JavaDeveloper(Developer):
    def work(self):
        print("java developer is working")
class pythonDeveloper(Developer):
    def work(self):
        print("python developer is working")
java_dev = JavaDeveloper()
python_dev = pythonDeveloper()
java_dev.work()
python_dev.work()

from abc import ABC,abstractmethod
class Developer(ABC):
    @abstractmethod
    def work(self):
        pass
class JavaDeveloper(Developer):
    def work(self):
        print("java developer is working")
class pythonDeveloper(Developer):
    def work(self):
        print("python developer is working")
java_dev = JavaDeveloper()
python_dev = pythonDeveloper()
java_dev.work()
python_dev.work()


