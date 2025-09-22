ans = int(input("Input: "))
sum = 0
for i in range(ans - 1):
    if(ans % (i + 1) == 0):
        sum += i + 1
if(sum == ans):
    print("perfect number")
else:
    print("not a perfect number")