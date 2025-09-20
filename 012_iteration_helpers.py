number = [10, 20, 30]

for i, num in enumerate(number):   # enumerate() gets the value of each element
    print(f"index: {i}, value: {num}")

print("\n")

names = ["lance", "ann", "chito"]
grades = [95, 92, 90]
for name, score in zip(names, grades):   # zip() combines 2 or more list into pairs
    print(f"{name}: {score}")

print("\n")

numbers = [10, 20, 30]
for r in reversed(numbers):   # reverses the array
    print(r)

print("\n")

numbers = [30, 10, 20]

print(sorted(numbers))          # [10, 20, 30]
print(sorted(numbers, reverse=True))  # [30, 20, 10]

# prints in sorted manner but doesn't change the value