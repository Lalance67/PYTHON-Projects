# Class = blueprint
# Object / Instance = real thing made from the blueprint

# example:
# class Car:       # blueprint
#     pass

# my_car = Car()   # object


# basic attributes
class Car:
    def __init__(self, brand, color):
        self.brand = brand # attribute
        self.color = color

# create object
car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

print(car1.brand, car1.color)
print(car2.brand, car2.color)



#basic methods

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"{self.brand} is driving!")

my_car = Car("Toyota", "Red")   # for attributes
my_car.drive()                  # for methods (functions)