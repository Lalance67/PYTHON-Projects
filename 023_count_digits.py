# Count the number of digits in an integer
digits = int(input("Enter int: "))
count = 0
while digits > 0:
    digits //= 10
    count += 1

print(f"digits: {count}")