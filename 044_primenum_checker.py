import math
ans = int(input("Input: "))
isprime = False
if((ans < 2)):
    isprime = False
elif(ans == 2):
    isprime = True
elif(ans % 2 != 0):
    isprime = True
for i in range(3, int(math.sqrt(ans)) + 1, 2):
    if(ans % i == 0):
        isprime = False
        break
if(isprime):
    print("prime number")
else:
    print("not a prime number")