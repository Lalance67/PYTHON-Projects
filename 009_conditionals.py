# if statement
if 1 == 1:
    print("hello\n")

if 0:
    print("hello")

# elif and else statement
age = 5

if age < 12:
    print("child")
elif (age < 18) and (age > 12):   # python uses & for and
    print("teen")
elif (age > 18) and (age < 100):
    print("adult")
else:
    print("invalid age")