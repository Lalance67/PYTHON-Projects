def print_table(grades):
        i = 1
        length = len(grades)
        print("\n%-8s  %-15s  %-20s "% ("number", "name", "grades"))
        print("-" * 50)
        if length >= 1:
            for name, grade in grades.items():
                grade_str = " ".join(map(str, grade))
                print("| %-8d| %-15s| %-20s|" % (i, name, grade_str))
                print("-" * 50)
                i += 1
def edit_g(grades):
    while 1:
        print_table(grades)
        print("[1] replace grades")
        print("[2] remove grades")
        print("[3] back to main menu")

        ans = int(input("Enter your choice: "))
        match ans:
            case 1: 
                ans2 = int(input("Enter student number to edit: "))
                l = list(grades)
                length = len(l)
                if ans2 >= 1 and ans2 <= length:
                    new = list(map(int, input(f"Enter {l[ans2 - 1]}'s new grades: ").split()))
                    grades[l[ans2 - 1]] = new
                    grades.update({l[ans2 - 1]: new})
                    return grades
            case 2: 
                ans2 = int(input("Enter student number to edit: "))
                l = list(grades)
                length = len(l)
                if ans2 >= 1 and ans2 <= length:
                    grades[l[ans2 - 1]] = ""
                    grades.update({l[ans2 - 1]: ""})
                    return grades
                
            case 3: return grades
            case _: print("Invalid input. try again")


def add_s(grades):
    while 1:
        name = input("name: ")
        g = list(map(int, input("grades: ").split()))
        ans = input(f"add: {name}: {' '.join(map(str, g))}? (y/n): ").lower()
        if(len(ans) == 1 and ans == 'y'):
            grades[name] = g
            break
        elif(len(ans) == 1 and ans == 'n'):
            break
        else: print("Invalid input. try again\n")
def remove_s(grades):
    while 1:
        exit = True
        ans1 = int(input("pick a student number to remove: "))
        l = list(grades)
        length = len(l)
        while(1):
            if ans1 >= 1 and ans1 <= length:
                ans2 = input("are you sure you want to remove ? (y/n): ")
                if len(ans2) == 1 and ans2 == 'y':
                    str = l[ans1 - 1]
                    grades.pop(str)
                    break
                elif len(ans2) == 1 and ans2 == 'n':
                    break
                else: print("Invalid input. try again\n")
                check = False
            else: print("Invalid input. try again\n")
        if exit: return grades

       
def edit_s(grades):
    while(1):
        print_table(grades)
        print("[1] add student")
        print("[2] remove student")
        print("[3] back to main\n")

        ans = int(input("Enter your choice: "))
        match ans:
            case 1: add_s(grades)
            case 2: remove_s(grades)
            case 3: return grades
            case _: print("Invalid input. try again\n")


grades = {
        "lance": [90, 92, 93],
        "ann": [2, 3, 4]
    }        
while(1):  
    print_table(grades)
    print("\n+--- MENU ---+")
    print("[1] edit student")
    print("[2] edit grade")
    print("[3] exit\n")
    
    ans = int(input("Enter your choice: "))
    match ans:
        case 1: edit_s(grades)
        case 2: edit_g(grades)
        case 3: break
        case _:  print("Invalid input. try again\n")
        
