def is_palindrome(arr):
    rev = arr[::-1]
    if rev == arr: return True
    else: return False
ans = input("Input: ")
if(is_palindrome(ans)): print("palindrome")
else: print("not a palindrome")