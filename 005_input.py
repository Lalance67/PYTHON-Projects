# input string
name = input("Enter your name: ")
print("hello, ", name)

# input int
age = int(input("Enter you age: "))
print("you'll be %d next year" % (age + 1))

#input float
n = float(input("Enter a float: "))
print(f"num + 1 is {n + 1:.2f}")




# (not working)
#multiple inputs in one line
# a, b = input("Enter two numbers: ").split
# a = int(a)
# b = int(b)
# print("Sum: ", a + b")"