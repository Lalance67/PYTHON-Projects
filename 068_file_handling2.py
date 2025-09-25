name = input("name: ")
age = int(input("age: "))

with open("data.txt", "w") as f:
    f.write(name)
    f.write("\n")
    f.write(str(age))
with open("data.txt", "r") as f:
    content = f.read()
print(content)