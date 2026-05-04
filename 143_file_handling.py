def add(f):
    while 1:
            code = int(input("PRODUCT CODE: "))
            name = input("PRODUCT NAME: ")
            quantity = int(input("QUANTITY: "))
            f.write(f"{code}\n")
            f.write(f"{name}\n")
            f.write(f"{quantity}")

            isexit = 0
            while 1:
                choice = input("Enter more? [Y/N]: ").upper()
                if choice == 'Y':
                    break
                elif choice == 'N':
                    isexit = 1
                    break
                else:
                    print("invalid input. try again")
                    continue
            if isexit: break

def delete(f):
    search = int(input("search product code: "))
    content = f.read()

    lines = content.splitlines()
    f.seek(0)
    f.truncate()
    isfound = 0

    for i in range(0, len(lines), 3):
        if lines[i] == str(search):
            isfound = 1
            isexit = 0
            while 1:
                print(f"code: {lines[i]}")
                print(f"name: {lines[i+1]}")
                print(f"quantity: {lines[i+2]}")
                ask = input("delete this? [y/n]: ").upper()
                if choice == 'Y':
                    
                    break
                elif choice == 'N':
                    isexit = 1
                    break
                else:
                    print("invalid input. try again")
                    continue
            if isexit: break

    if not isfound:
        print("no search found")


    


with open("Products.txt", "w") as f:              
    add(f)

while 1:
    isexit = 0

    while 1:
        print("%-10s %-10s %-10s %-10s %-10s" % ('A - ADD', 'D - DELETE', 'E - EDIT', 'T - TRANSACT', 'X - EXIT'))
        choice = input("WHAT DO YOU WANT TO DO? ").upper()
        if choice == 'A':
            with open("Products.txt", "a") as f:  
                add(f)

        elif choice == 'D':
            with open("Products.txt", "r") as f:  
                delete(f)

        # elif choice == 'E':
        
        # elif choice == 'T':

        elif choice == 'X':
            isexit = 1
            break
        else:
            print("invalid input. try again")
            continue
    if isexit: break
        

                