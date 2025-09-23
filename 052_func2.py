def iseven(n):
    if(n % 2 == 0):
        return True
    else:
        return False
    
ans = int(input("Input: "))
if(iseven(ans)):
    print("even")
else:
    print("odd")