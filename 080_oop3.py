# Bank Account Class (Basics Only)

class bank():
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def withdraw(self, amount):
        print(f"balance after withdrawal: {self.balance - amount}")
        self.balance -= amount

    def deposit(self, amount):
        print(f"balance after deposit: {self.balance + amount}")
        self.balance += amount

acc1 = bank("lance")

print(acc1.owner)
acc1.deposit(100)
acc1.withdraw(50)
        
    