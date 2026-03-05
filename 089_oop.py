class student():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"student: {self.name}"
s1 = student("lance")
print(s1)