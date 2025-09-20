arr = input("input a string: ")
rev = list()
for i in range(len(arr) - 1, - 1, - 1):
    rev.append(arr[i])
rev_str = "".join(rev)
if rev_str == arr:
    print("palindrome")
else:
    print("not palindrome")