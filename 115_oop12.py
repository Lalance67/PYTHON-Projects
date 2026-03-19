# Create a class Character

class character:
    def __init__(self, name, hp = 100):
        self.name = name
        self.hp = hp

    def attack(self, enemy):
        enemy.hp -= 10
        print(f"{self.name} attacked {enemy.name}")
        
    def show(self):
        print(f"{self.name} hp: {self.hp}")

p1 = character("lance")
p2 = character("john")

p1.attack(p2)
p2.show()