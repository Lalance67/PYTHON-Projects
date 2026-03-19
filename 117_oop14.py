# inheritance

class Character:
    def __init__(self, name, hp = 100):
        self.name = name
        self.hp = hp
    def attack(self, enemy):
        enemy.hp -= 10
        print(f"{enemy.name} hp: {enemy.hp}")

class warrior(Character):
    def attack(self, enemy):
        enemy.hp -= 20
        print(f"{enemy.name} hp: {enemy.hp}")

class Mage(Character):
    def attack(self, enemy):
        enemy.hp -= 15
        print(f"{enemy.name} hp: {enemy.hp}")
    def fireball(self, enemy):
        enemy.hp -= 30
        print(f"{self.name} casts a fireball to {enemy.name}")
        print(f"{enemy.name} hp: {enemy.hp}")

p1 = warrior("lance")
p2 = Character("john")
p3 = Mage("april")

p2.attack(p1)
p1.attack(p2)
print()
p3.attack(p1)
p3.fireball(p1)