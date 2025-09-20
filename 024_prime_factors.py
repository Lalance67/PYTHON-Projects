# Print all prime factors of a number
num = int(input("Enter a number: "))
factors = list()
for i in range(2, num - 1):
    while num % i == 0:
        num /= i
        factors.append(i)
print(factors)