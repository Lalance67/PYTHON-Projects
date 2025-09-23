def max(arr):
    m = arr[0]
    for i in range(len(arr)):
        if(m < arr[i]):
            m = arr[i]
    return m
arr = list(map(int, input("Input numbers: ").split()))
m = max(arr)
print(f"maximum: {m}")
