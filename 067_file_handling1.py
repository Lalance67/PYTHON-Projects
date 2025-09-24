# basic file handling

# opening a file
f = open("data.txt", "w")   # modes: r, w, a, x, rb, wb

# reading a file
with open("data.txt", "r") as f:
    content = f.read()    # reads the whole file
    line = f.readline()   # reads a single line
    lines = f.readlines() # reads all line as list

    print(type(lines))

# writing a file
with open("data.txt", "w") as f:
    f.write("hello, world!\n")

# appending a file
with open("data.txt", "a") as f:
    f.write("newline\n")

# saving a dict var in json
import json

contacts = {"lance": "09761338863", "nathan": "09761338862"}

# save contacts to file
with open("contacts.json", "w") as f2:
    json.dump(contacts, f2)

# load contacts from file
with open("contacts.json", "r") as f2:
    contacts = json.load(f2)

for k, v in contacts.items():
    print(f"{k}: {v}")

# close file
f.close()
f2.close()

# Using with automatically closes the file
