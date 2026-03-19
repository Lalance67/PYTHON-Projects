class Character:
    def __init__(self, name, hp = 100):
        self.name = name
        self.hp = hp

    def attack(self, enemy):
        enemy.hp -= 10
        print(f"{self.name} attacked {enemy.name}")

        if enemy.hp <= 0:
            enemy.hp = 0
            print(f"{enemy.name} has been defeated")
        
        print(f"{enemy.name} hp: {enemy.hp}")

p1 = Character("lance")
p2 = Character("john", 10)

p1.attack(p2)
        