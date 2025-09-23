import collections
ans = input("Input: ").lower().split()
count = collections.Counter(ans)
len = len(list(collections.Counter(ans)))
print("{", end = "")
for i, (j, k) in enumerate(count.items()):
    if i == len - 1: print("'%s': %d"% (j, k), end = "")
    else: print("'%s': %d, "% (j, k), end = "")
print("}", end = "")



