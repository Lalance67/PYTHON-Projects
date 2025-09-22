ans = int(input("Input: "))
sum = 0
while(ans > 0):
    sum += (ans % 10)
    ans //= 10
print(f"Output: {sum}")