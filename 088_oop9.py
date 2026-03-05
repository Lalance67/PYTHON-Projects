class player():
    
    game = "badminton"
     
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def show(self):
        print(f"{self.name} plays {self.game}, and has score {self.score}")

s1 = player("lance", 10)
s1.show()