class player:
    game = "badminton"

    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"player: {self.name}"
p1 = player("lance")
p2 = player("jone")

print(p1.game)
print(p2)
print(p1)