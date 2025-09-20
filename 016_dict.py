# A dictionary is like a map of key to value pairs.
# - Keys are unique.
# - Values can be any type (string, int, list, even another dict).
# - Keys must be immutable (strings, numbers, tuples).

person = {
    "name": "Lance",
    "age": 19,
    "is_student": True
}
print(person["name"])   # Lance
print(person["age"])    # 19

# safer way to print if the value doesn't exist
print(person.get("name"))
print(person.get("age"))
print(person.get("grade"))   # prints defauld value

print()

# .keys(), .values(), .items()
print(person.keys())  # prints the keys like "name", "age"
print(person.values)  # prints the values like "Lance", "19"
print(person.items()) # prints all the items (keys and value)

# convert list to dict
names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)  # {'Alice': 5, 'Bob': 3, 'Charlie': 7}
