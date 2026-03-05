class rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        print(f"area: {self.length * self.width}")

    def perimeter(self):
        print(f"perimeter: {(2 * self.length) + (2 * self.width)}")
        
shape1 = rectangle(2, 3)
shape1.area()
shape1.perimeter()