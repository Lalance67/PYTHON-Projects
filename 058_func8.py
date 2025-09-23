import math
def isprime(n):
        return n >= 2 and all(n % i != 0 for i in range(3, int(math.sqrt(n)) + 1, 2))
ans = int(input("Input: "))
if(isprime(ans)): print("prime number")
else: print("not a prime number")