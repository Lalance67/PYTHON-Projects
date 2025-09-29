def search(str, content):
    res = list()
    i = 1
    for con in content:
        if str in con:
            res.append(i)
        i += 1
    return res

with open("notes.txt", "r") as f:
    content = f.readlines()

ans = input("Enter search: ")
results = search(ans, content)
print(*results)