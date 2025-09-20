def greet(name):
    print(f"hello, {name}")
    
greet("lance")

def multiple_operations(a, b):
    return a + b, a - b, a * b, a // b   # multiple returns

add, minus, multiply, divide = multiple_operations(5, 3)
print(add)
print(minus)
print(multiply)
print(divide)

def power(base, exp = 2):   # default exponent
    return base ** exp
print(power(3))
print(power(3, 3))

def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

# positional
describe_pet("dog", "Buddy")
# → I have a dog named Buddy.


describe_pet("dog", name="Buddy")  # ✅ valid   (positional, keyword)
# describe_pet(name="Buddy", "dog") # ❌ invalid (positional must come first)

def add_numbers(*args):   # variable-length positional arguments
    total = 0
    for i in args:
        total += i
    return total
print(add_numbers(1, 2, 3))

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")
print_info(name = "lance", age = 20, course = "BSIT")

# lambda - a small, unnamed function you can write in one line.
# It’s useful when you don’t want to define a full def function.

say_hi = lambda: "hi"
print(say_hi())

add = lambda a, b: a + b
print(add(2, 3))

square = lambda x: x * x
print(square(4))

nums = [1, 2, 3, 4, 5]

# square each number
squared = list(map(lambda x: x**2, nums))
print(squared)  # [1, 4, 9, 16, 25]

# filter even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4]

global count   # makes the variable global
def outer():
    var = 10
    def inner():
        nonlocal var   # accessess the var in outer def

# map(function, iterable) iterates to every alement in an array
# filter(function, iterable) keep the elements that returns true in the function
# sorted(iterable, key=... , reverse= ...) Sorts values, optionally using a key function.

words = ["banana", "apple", "cherry"]

# Sort by length
sorted_words = sorted(words, key=len)   #sorts by length
print(sorted_words)  # ['apple', 'banana', 'cherry']

# Sort numbers by absolute value
nums = [-5, 3, -2, 7]
print(sorted(nums, key=abs))  # [-2, 3, -5, 7]   sorts by absolute value
