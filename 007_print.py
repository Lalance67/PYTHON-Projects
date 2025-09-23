print("""hello
python
world""")
# multiple lines in one print

print("\nhello\nworld")
# newline "\n" like in c

def ds():
    """
    this is called docstrings
    Docstrings describe what a function/class/module does.
    """

print(ds.__doc__)   #prints the docstring

# format specifier
pi = 3.14159265
print("Pi with 2 decimals: %.2f" % pi)   # 3.14
print("Integer: %d, Hex: %x" % (255, 255))  # Integer: 255, Hex: ff

# str.format()
pi = 3.14159265
print("Pi with 2 decimals: {:.2f}".format(pi))   # 3.14
print("Binary of 10: {:b}".format(10))           # 1010