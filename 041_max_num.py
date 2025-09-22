ans = list(map(int, input("Input numbers: ").split()))
max = ans[0]
for i in range(len(ans)):
    if(max < ans[i]):
        max = ans[i]
print(max)