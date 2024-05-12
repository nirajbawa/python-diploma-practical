from abc import abstractmethod

class person():
    @abstractmethod
    def greet(self):
        pass

class student(person):
    def __init__(self) -> None:
        print("hello")
    def greet(self):
        print("hii")

s = student()
s.greet()