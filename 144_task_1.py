def add(mode="a"):
    with open("Products.txt", mode) as f:
        while 1:
            try:

                code = int(input("PRODUCT CODE: "))
                name = input("PRODUCT NAME: ")
                quantity = int(input("QUANTITY: "))
            except ValueError:
                print("invalid input. code and quantity must be numbers.")
                continue

            f.write(f"{code}\n")
            f.write(f"{name}\n")
            f.write(f"{quantity}\n") 

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
            
            if isexit: 
                break

def delete():
    while 1:
        try:
            search = int(input("search product code: "))
        except ValueError:
            print("invalid input. try again.")
            continue

        try:
            with open("Products.txt", "r") as f:
                lines = f.read().splitlines()
        except FileNotFoundError:
            print("record not found")
            return

        isfound = 0
        new_lines = []
        i = 0
        
        while i < len(lines):
            if lines[i] == str(search):
                isfound = 1
                print(f"code: {lines[i]}")
                print(f"name: {lines[i+1]}")
                print(f"quantity: {lines[i+2]}")
                
                while 1:
                    ask = input("delete this? [y/n]: ").upper()
                    if ask == 'Y':
                        i += 3 
                        break
                    elif ask == 'N':
                        new_lines.extend([lines[i], lines[i+1], lines[i+2]])
                        i += 3
                        break
                    else:
                        print("invalid input. try again")
                break
            else:
                new_lines.extend([lines[i], lines[i+1], lines[i+2]])
                i += 3
        

        while i < len(lines):
            new_lines.extend([lines[i], lines[i+1], lines[i+2]])
            i += 3

        if not isfound:
            print("record not found")
            break
        else:
            if ask == 'Y':

                with open("Products.txt", "w") as f:
                    for line in new_lines:
                        f.write(f"{line}\n")
                print("record deleted.")
                break
            elif ask == 'N':

                continue

def edit():
    try:
        search = int(input("search product code: "))
    except ValueError:
        print("invalid input.")
        return

    try:
        with open("Products.txt", "r") as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        print("record not found")
        return

    isfound = 0
    i = 0
    
    while i < len(lines):
        if lines[i] == str(search):
            isfound = 1
            print(f"code: {lines[i]}")
            print(f"name: {lines[i+1]}")
            print(f"quantity: {lines[i+2]}")
            
            print("--- Enter new details ---")
            try:
                new_code = int(input("PRODUCT CODE: "))
                new_name = input("PRODUCT NAME: ")
                new_qty = int(input("QUANTITY: "))
            except ValueError:
                print("invalid input. edit failed.")
                return
            

            lines[i] = str(new_code)
            lines[i+1] = new_name
            lines[i+2] = str(new_qty)
            break
        i += 3

    if not isfound:
        print("record not found")
    else:

        with open("Products.txt", "w") as f:
            for line in lines:
                f.write(f"{line}\n")
        print("record updated.")

def transact():
    try:
        search = int(input("search product code: "))
    except ValueError:
        print("invalid input.")
        return

    try:
        with open("Products.txt", "r") as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        print("record not found")
        return

    isfound = 0
    i = 0
    
    while i < len(lines):
        if lines[i] == str(search):
            isfound = 1
            print(f"code: {lines[i]}")
            print(f"name: {lines[i+1]}")
            print(f"quantity: {lines[i+2]}")
            
            t_code = input("TRANSACTION CODE (P/S): ").upper()
            if t_code not in ['P', 'S']:
                print("invalid transaction code.")
                return
                
            try:
                qty = int(input("QUANTITY: "))
            except ValueError:
                print("invalid input.")
                return
            
            current_qty = int(lines[i+2])
            
            if t_code == 'P':
                current_qty += qty
            elif t_code == 'S':
                current_qty -= qty
                
            lines[i+2] = str(current_qty)
            break
        i += 3

    if not isfound:
        print("record not found")
    else:
        with open("Products.txt", "w") as f:
            for line in lines:
                f.write(f"{line}\n")
        print("transaction successful.")


print("--- INITIALIZE PRODUCT RECORDS ---")
add(mode="w") 

while 1:
    isexit = 0

    while 1:
        print("\n%-10s %-10s %-10s %-10s %-10s" % ('A - ADD', 'D - DELETE', 'E - EDIT', 'T - TRANSACT', 'X - EXIT'))
        choice = input("WHAT DO YOU WANT TO DO? ").upper()
        
        if choice == 'A':
            add(mode="a")

        elif choice == 'D':
            delete()

        elif choice == 'E':
            edit()
        
        elif choice == 'T':
            transact()

        elif choice == 'X':

            print("\n--- UPDATED FILE RECORDS ---")
            try:
                with open("Products.txt", "r") as f:
                    content = f.read()
                    print(content.strip() if content.strip() else "File is empty.")
            except FileNotFoundError:
                print("File is empty or does not exist.")
                
            print("end of program")
            isexit = 1
            break
            
        else:
            print("invalid input. try again")
            continue
            
    if isexit: 
        break