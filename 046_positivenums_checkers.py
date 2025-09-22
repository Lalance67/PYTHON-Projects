ans = list((map(int, input("Enter numbers: ").split())))
ispos = all(ans[i] > 0 for i in range(len(ans)))
print("all numbers are positive" if ispos else "not all numbers are positive")

