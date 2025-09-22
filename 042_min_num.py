ans = list(map(int, input("Enter numbers: ").split()))
min = ans[0]
for i in range(len(ans)):
    if(min > ans[i]):
        min = ans[i]
print(min)