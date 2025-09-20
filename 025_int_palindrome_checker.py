num = int(input("Enter a number: "))
rev = int(str(num)[::-1])
if rev == num:
    print("palindrome")
else:
    print("not palindrome")