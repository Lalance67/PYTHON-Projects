def factorial(n):
    if n <= 1: return 1
    return n * factorial(n - 1)
ans = int(input("Input: "))
print(f"factorial: {factorial(ans)}")