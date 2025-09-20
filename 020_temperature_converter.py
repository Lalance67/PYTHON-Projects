# Convert temperature between Celsius and Fahrenheit.

while 1:
    print("[1] F to C")
    print("[2] C to F")
    print("[3] exit")
    ans = int(input("Enter num: "))
    if(ans == 1):
        f = float(input("Enter farenheit: "))
        c = (f - 32) * (5/9)
        print(f"Celcius: {c:.2f}\n")
    elif(ans == 2):
        c = float(input("Enter celsius: "))
        f = c * (9/5) + 32
        print(f"Celcius: {f:.2f}\n")
    elif(ans == 3):
        break
    else:
        print("invalid number. try again")