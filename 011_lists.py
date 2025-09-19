fruits = ["apple", "banana"]
fruits.append("cherry")
fruits.extend(["grapes", "orange"])
fruits.insert(0, "strawberry")
fruits.pop(2)
print(fruits)

num = [4, 2, 5, 7, 1, 3, 9, 8, 6]
num.sort()
print(num)

fruits = ["apple", "banana", "cherry", "mango", "grape"]
print(fruits[1:4])   # slicing where you only print certain index ranges
print(fruits[:3])
print(fruits[1:])
print(fruits[::2])   # every second item
print(fruits[::-1])  # reversed
print(fruits[-3:])   # ['cherry', 'mango', 'grape']  (last 3 items)
print(fruits[:-2])   # ['apple', 'banana', 'cherry'] (everything except last 2)