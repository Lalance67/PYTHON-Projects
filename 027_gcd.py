num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
remainder = int()

if(num1 < num2):
    temp = num1
    num1 = num2
    num2 = temp
while(1):
    remainder = num1 % num2
    if(remainder == 0):
        break
    num1 = num2
    num2 = remainder
print(f"gcd: {num2}")
        
    