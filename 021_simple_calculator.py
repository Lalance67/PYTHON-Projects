# Perform basic operations (+, -, *, /) between two numbers.
while 1:
    num1 = num2 = ans = None
    print("+--- SIMPLE CALCULATOR ---+")
    print("[1] add")
    print("[2] subract")
    print("[3] multiply")
    print("[4] divide")
    print("[5] exit")

    ans = int(input("\nEnter choice: "))

    match ans:
        case 1:
            num1 = float(input("\nnum1: "))
            num2 = float(input("num2: "))
            print(f"answer: {num1 + num2}\n")
        case 2:
            num1 = float(input("num1: "))
            num2 = float(input("num2: "))
            print(f"answer: {num1 - num2}\n")
        case 3:
            num1 = float(input("num1: "))
            num2 = float(input("num2: "))
            print(f"answer: {num1 * num2}\n")
        case 4:
            num1 = float(input("num1: "))
            num2 = float(input("num2: "))
            print(f"answer: {num1 / num2}\n")
        case 5:
            break
        case _:
            print("invalid answer. try again\n")
