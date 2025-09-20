# for loop
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3]

for fruit in fruits: 
    print(fruit)

print("\n")

for i in numbers:
    print(i)

print("\n")

for let in "lance":
    print(let)

print("\n")

for i in range(5):   # range(5) = 0,1,2,3,4
    print(i)

print("\n")

for i in range(2, 12, 2):  # range(start, stop, increment)
    print(i)               # like for(int i = 2; i <= 10; i += 2) in C

print("\n")


# while loop

i = 0

while i < 5:
    print(i + 1)
    i += 1

print("\n")

n = 0
while 1:
    print(n)
    if n == 10:
        break
    n += 2

print("\n")

n = 0
while n <= 10:
    if (n % 2) != 0:
        n += 1
        continue
    print(n)
    n += 1
