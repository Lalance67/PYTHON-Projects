def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
while(1):
    print("menu: ")
    print("[1] add")
    print("[2] subtract")
    print("[3] multiply")
    print("[4] divide")
    print("[5] exit")

    ans = int(input("Enter your choice: "))
    num1 = float(input("num1: "))
    num2 = float(input("num2: "))

    match ans:
        case 1: print(f"Output: {divide(num1, num2):.2}\n")
        case 2: print(f"Output: {subtract(num1, num2):.2}\n")
        case 3: print(f"Output: {multiply(num1, num2):.2}\n")
        case 4: print(f"Output: {divide(num1, num2):.2}\n")
        case 5: break
        case _: print("invalid choice. try again")