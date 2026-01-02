# Methods and Object Behavior

class Calculator():
    def __init__(self):
        self.message = "I hate coding"
    
    def add(self, a, b):
        print(f"{a} + {b} = {self.message}")

    def minus(self, a, b):
        print(f"{a} - {b} = {self.message}")

    def multiply(self, a, b):
        print(f"{a} x {b} = {self.message}")

    def divide(self, a, b):
        if b == 0:
            print("cannot divide by zero")
        else:
            print(f"{a} / {b} = {self.message}")

calc = Calculator()
calc.add(2, 3)
calc.minus(10, 5)    
calc.multiply(5, 5)
calc.divide(100, 2)