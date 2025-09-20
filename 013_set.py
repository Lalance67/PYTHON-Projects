# set - collection of unique elements
#     - enclosed by {}

numbers = {1, 2, 3, 3, 4}
print(numbers)   #   removes duplicated numbers
print(type(numbers))

print("\n")

s = {10, 20, 30}
s.add(40) # appends to the first element
s.remove(10) # removes element
s.discard(100)  # removes an element (no error if it doesn't exist)
print(s)

s.clear()   # removes all element
print(s)

print("\n")

# set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)                  #prints all elements (ignores duplicate)
print(a.union(b))             #same

print(a & b)                  #prints common elements
print(a.intersection(b))      #same

print(a - b)                  #prints elements in a that are not in b
print(a.difference(b))        #same

print(a ^ b)                  #prints elements in either, but not in both
print(a.symmetric_difference(b))


#checking membership
print(2 in a)   # True
print(10 in b)  # False

# Why Use Sets?

# Automatically remove duplicates from data.
# Useful for fast membership tests (in is faster in sets than in lists).
# Handy for comparing groups of items.