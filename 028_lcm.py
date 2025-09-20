# Find the least common multiple of two numbers
num1, num2 = input("Enter 2 numbers (separate with space): ").split()
num1 = int(num1)
num2 = int(num2)
lcm = list()
if(num1 < num2):
    temp = num1
    num1 = num2 
    num2 = temp
for i in range(2, num1):
    while((num1 % i == 0) and (num2 % i == 0)):
        num1 /= i
        num2 /= i
        lcm.append(i)
lcm.append(int(num1))
lcm.append(int(num2))
lcm2 = 1
for i in range(0, len(lcm)):
    lcm2 *= lcm[i]
print(lcm)
print(lcm2)