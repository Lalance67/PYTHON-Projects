class car():
    def __init__(self, model):
        self.model = model
        self.fuel = 100

    def drive(self, km):
        self.fuel -= km

    def ref(self, amount):
        self.fuel += amount
car1 = car("toyota")
car1.drive(50)
car1.ref(25)
print(car1.fuel)
