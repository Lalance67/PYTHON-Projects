x = 5
y = 1.4
name = "lance"
char = 'l' #char have ''
check = True #capital t
r = None #means NULL in C
dictionary = {"name": "lance", "age": "19"}
print(dictionary["name"])        #dictionary can declare and store multiple data type
                                 #but it cannot be an array like in structs

#lists/array (int)
numbers = [1, 2, 3, 4, 5]   #declare and initialize
print(numbers[0])
numbers[1] = 20   #modify
print(numbers[1]) 
numbers.append(6)   #appends 6 at the end of the list
print(numbers)

#lists/array (one char)
letters = ['a', 'b', 'c']
letters.append('d')
print(letters)
#or use list()
word = "hello"
chars = list(word)
print(chars)

#lists/array of strings
names = {"lance", "ann", "chito"}
print(names)

#lists/array  (mixed)
mixed = [1, 3.14, 'a', "lance", True]
print(mixed)

# automatically assigns data type
# same rules in naming variables in C

# variables can change data type if you reassign
a = 5       #int
a = "lance" #now its a string

# multiple assignments
a, b, c, = 1, 2, 3 
x = y = z = 0

# check the type of the variable using the function "type()"
print(type(x))   # prints <class 'int'>

pi = 3.14159
print("pi: %.2f" % pi)   #uses %

name = "lance"
age = 19
print("\nname: {}, age: {}".format(name, age))   #uses format()
# or
print("pi to 3 decimals: {:.3f}".format(pi))

# THE MOST USED IS f-strings
print(f"\nf-strings:\nname: {name}, age: {age}")
print(f"next year, I'll be {age + 1}")
print(f"pi: {pi:.3f}")

# ps: do NOT forget to add f before the "" in print if you're using f-strings

#unpacking
numbers = (1, 2, 3)
a, b, c = numbers
print("\nunpacking:")
print(f"{a}, {b}, {c}")

a, _, c = numbers   # _ common convention to skip one index
print(f"{a}, {c}") 

numbers2 = (1, 2, 3, 4, 5)
a, *middle, c = numbers2   # * captures the rest numbers as an array
print(f"{a}, {middle}, {c}")

def add(x, y, z):
    return x + y + z

nums = [1, 2, 3]
print(add(*nums))   # * means captures the rest

