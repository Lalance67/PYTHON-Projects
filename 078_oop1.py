# Student class with greet method

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def greet(self):
        print(f"hello! my name is {self.name}")

s1 = Student("Lance", "20", "BSIT")
s1.greet()