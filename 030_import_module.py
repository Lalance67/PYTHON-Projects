# full import
# import module1
# print(module1.add(1, 1))

# specific function
# from module1 import sub
# print(sub(5, 1))

# rename functin
from module1 import multiply as times
print(times(2, 2))

# package - a folder of modules to use 
# with an __init__.py file (it marks the folder as a package).

from my_package import math_utils, greetings
print(greetings.hi())
print(math_utils.divide(100, 4))
