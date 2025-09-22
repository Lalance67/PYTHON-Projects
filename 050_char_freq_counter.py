from collections import Counter
ans = input("Input: ")
count = Counter(ans)
for i in count:
        print(f"{i}: {count[i]}", end = ", ")