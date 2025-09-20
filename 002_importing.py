# If the file is named "004_add.py", use importlib
import importlib
# or import filename (doesn't start with a letter)

# Load the module
add_module = importlib.import_module("004_add")   # use the file name (without .py)

print("\nadd_module.add: 2 + 3 =", add_module.addf(2, 3))

# If the file doesnt start with number like add.py,
# from add import add
# print("\nadd: 2 + 3 =", add(2, 3))

# Rename the function when importing
# from add import add as plus
# print(plus(2, 3))

# concatenate strings
print("\nstring:")
print(add_module.addf("lan", "ce"))

# concatenate lists
print("\nlist:")
print(add_module.addf([1, 2], [3, 4]))