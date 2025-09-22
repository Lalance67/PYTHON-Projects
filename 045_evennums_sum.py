ans = int(input("Input: "))
sum = 0
for i in range(ans):
    if((i + 1) % 2 == 0):
        sum += i + 1
print(sum)