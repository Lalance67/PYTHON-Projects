ans = int(input("Input: "))
f = 0
prev = 1
num = int()
for i in range(ans):
    if(i == 0):
        print(f)
    else:
        num = f + prev
        print(num)
        prev = f
        f = num
    
