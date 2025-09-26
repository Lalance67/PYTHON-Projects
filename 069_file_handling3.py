from collections import Counter

def char(str):
    if not str:
        return 0
    c = 0
    for i in str:
        if(i.isalpha()):
            c += 1
    return c

def words(str):
    if not str:
        return 0
    w = 1
    for i in str:
        if(i == ' '):
            w += 1
    return w

def line(str):
    if not str:
        return 0
    l = 1
    for i in str:
        if(i == '\n'):
            l += 1
    return l

ans = input("Enter text: ")
c = char(ans)
w = words(ans)
l = line(ans)

with open("sample.txt", "w") as f:
    f.write(ans)
    f.write("\n")
    f.write(str(c))
    f.write("\n")
    f.write(str(w))
    f.write("\n")
    f.write(str(l))
with open("sample.txt", "r") as f:
    content = f.readlines()

text, c, w, l = content
print(text, end = "")
print(c, end = "")
print(w, end = "")
print(l, end = "\n")