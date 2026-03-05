class circle():
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        print(f"area: {3.14 * (self.radius * self.radius)}")
    
    def circumference(self):
        print(f"circumference: {2 * 3.14 * self.radius}")

shape1 = circle(3)
shape1.area()
shape1.circumference()
        