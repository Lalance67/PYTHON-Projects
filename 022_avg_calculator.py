# Find the average of n numbers
numbers = list(map(int, input("enter numbers (separate with space): ").split()))
sum = 0
count = 0
for i in range(len(numbers)):
    sum += numbers[i]
    count += 1
print(f"sum: {sum:.2f}")
avg = sum / count
print(f"average: {avg:.2f}")
