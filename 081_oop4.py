# Student Class

class student():
    def __init__(self, name, age, grade):
        self.name = name 
        self.age = int(age)
        self.grade = grade

    def introduce(self):
        print(f"name: {self.name}, age: {self.age}")

    def add(self):
        while 1:
            check = 0
            try:
                ans = int(input("enter grades to add: "))
                self.grade.append(ans)
            except ValueError: 
                print("invalid input. try again")
                continue
            while 1:
                ans2 = input("would you like to input more? [y/n]: ").lower()
                if ans2 == 'y':
                    check = 0
                    break
                elif ans2 == 'n':
                    check = 1
                    break
                else: print("invalid input. try again")
            if check: break
            else: continue
    
    def ave(self):
        count = 0
        sum = 0
        for i in self.grade:
            sum += i
            count += 1

        if count != 0:
            average = sum / count
            print(f"average: {average}")
        else: print("no grade input. try again")

s1 = student("lance", 20, [])
s1.introduce()
s1.add()
s1.ave()
print(", ".join(str(item) for item in s1.grade))
