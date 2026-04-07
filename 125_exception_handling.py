# 1. TypeError
# This happens when you try to do something to a data type that it wasn't meant for.
# Example: Trying to add a string and a number: "Hello" + 5.

# 2. ValueError
# The data type is correct, but the content is wrong for the operation.
# Example: You tell Python to turn a string into an integer using int("apple"). Python knows how to turn strings into numbers, but "apple" isn't a valid number.

# 3. NameError
# This happens when you try to use a variable or function name that doesn't exist yet (or is misspelled).
# Example: Calling print(user_name) before you ever defined user_name.

# 4. ArithmeticError
# This is the "Parent" category for math mistakes. The most famous one is ZeroDivisionError.
# Example: 10 / 0.

def hello():
    print("hello")

try:
    print("hello" + 5)
except TypeError:
    print("type error")

try:
    print(int("hello"))
except ValueError:
    print("value error")

try:
    hello()
except NameError:
    print("name error")

try:
    print(10/0)
except ArithmeticError:
    print("arithmetic error")
