ans = int(input("Input: "))
rev = int()
while(ans > 0):
    rev = ans % 10
    ans //= 10
    print(rev, end = "")
