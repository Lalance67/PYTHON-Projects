ans = int(input("Input: "))
ans2 = ans3 = ans
power = sum = 0
while(ans > 0):
    ans //= 10
    power += 1

while(ans2 > 0):
    sum += (ans2 % 10) ** power
    ans2 //= 10

if(ans3 == sum):
    print("armstrong number")
else:
    print("not an armstrong number")