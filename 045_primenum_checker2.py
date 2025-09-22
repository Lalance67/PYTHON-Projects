import math
ans = int(input("Input:  "))
isprime = (ans > 1, all(ans % i != 0 for i in range(2, int(math.sqrt(ans)) + 1)))
print("prime number" if isprime else "not a prime number")