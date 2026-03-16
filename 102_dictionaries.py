# pairs
dic = {"s1": "lance", "s2": "pao"}

dic2 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

#access
print(dic2["brand"])

#len 3
print(len(dic2))
print()

# elements can be list or other
dic2 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

#accessing values
x = (dic2["brand"])
#or
x = dic2.get("brand")
print(x)
print()

#accesssing keys
x = dic2.keys()
print(x)
print()

# adding new key pairs
x = dic2.keys()
dic2["electric"] = False
print(x)
print(dic2)


# access values
x = dic2.values()
print(x)
print("\n\n")

# access values and items
x = dic2.items()
print(x)

#update key pairs
dic2.update({"year": 2020})
print(dic2["year"])
print()

# pop key pairs
dic2.pop("electric")\
# dic2.popitem() removes last item
print(dic2)

# delete variable
# del dic2

#delete content
# dic2.clear()

#loops keys
for s in dic2.keys():
    print(s)

print()

#loops values
for s in dic2.values():
    print(s)
print()

#loops the items(overall):
for s, k in dic2.items():
    print(s, k)

print()

#copies
cop = {
    "price": 1000
}
dic2 = cop
print(dic2)



