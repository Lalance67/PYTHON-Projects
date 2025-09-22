ans = int(input("Input: "))
factors = []
for i in range(ans):
    if((ans % (i + 1)) == 0):
        factors.append(i + 1)
print(factors)