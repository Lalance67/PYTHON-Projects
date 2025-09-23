def fib(n):
    prev, cur, sum, arr = 0, 1, int(), list()
    for i in range(n):
        if i == 0: arr.append(prev)
        elif i == 1: arr.append(cur)
        else:
            sum = prev + cur
            arr.append(sum)
            prev = cur
            cur = sum
    return arr
        
n = int(input("Input: "))
arr = fib(n)
print(f"Output: {arr}")