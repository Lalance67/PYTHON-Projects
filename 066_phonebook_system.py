def print_res(res, contacts):
    i = 0
    print("========== RESULTS =========")
    print("+", end = "")
    print("-" * 45, end = "+\n")
    print(f"| {'number':<8}| {'name':<20}| {'contact':<12}|")
    print("+", end = "")
    print("-" * 45, end = "+\n")

    l = len(list(contacts))
    if l >= 1:
        for k, v in contacts.items():
            if i in res:
                print(f"| {i + 1:<8}| {k:<20}| {v:<12}|")
                print("+", end = "")
                print("-" * 45, end = "+\n")
            i += 1

def search_contact(contacts):
    while 1:
        res = set()
        ir = 0
        print("\n[1] search by name")
        print("[2] search by number")
        print("[3] exit\n")

        ans = int(input("Enter your choice: "))
        match ans:
            case 1: 
                while 1:
                    print("0 to cancel")
                    ans2 = input("Enter name: ")
                    if len(ans2) == 1 and ans2[0] == '0':
                        break
                    else: 
                        for i in list(contacts):
                            if ans2 in i:
                                res.add(ir)
                            ir += 1
                        print_res(res, contacts)
                        break
            case 2: 
                while 1:
                    print("0 to cancel")
                    ans2 = input("Enter name: ")
                    if len(ans2) == 1 and ans2[0] == '0':
                        break
                    else: 
                        for v in contacts.values():
                            if ans2 in v:
                                res.add(ir)
                            ir += 1
                        print_res(res, contacts)
                        break
            case 3: break
            case _: print("Invalid input. Try again\n")



def remove_contact(ans2, contacts):
    contacts.pop(list(contacts)[ans2 - 1])
    return contacts

def add_contact(name, contact, contacts):
    contacts[name] = contact
    return contacts


contacts = {
    "lance": "09761338863",
    "nathan": "09761338862"
}
while 1:
    i = 0
    print("========== PHONEBOOK MANAGEMENT SYSTEM =========")
    print("+", end = "")
    print("-" * 45, end = "+\n")
    print(f"| {'number':<8}| {'name':<20}| {'contact':<12}|")
    print("+", end = "")
    print("-" * 45, end = "+\n")
    l = len(list(contacts))
    if l >= 1:
        for k, v in contacts.items():
            print(f"| {i + 1:<8}| {k:<20}| {v:<12}|")
            print("+", end = "")
            print("-" * 45, end = "+\n")
            i += 1

    print("+--- MENU ---+")
    print("[1] add contact")
    print("[2] remove contact")
    print("[3] search contact")
    print("[4] exit program\n")
    
    ans1 = int(input("Enter your choice: "))
    match ans1:
        case 1:
            while 1:
                print("\n0 to cancel")
                name = input("Enter name: ")
                if len(name) == 1 and name[0] == '0':
                    break
                print("\n0 to cancel")
                contact = input("Enter contact: ")
                if len(str(contact)) == 1 and contact == 0:
                    break
                if len(contact) == 11 and int(contact) > 999999999:
                    add_contact(name, contact, contacts)
                    break
                else: print("Invalid input. Try again")
        case 2:
            while 1:
                print("0 to cancel")
                ans2 = int(input("Enter number to remove: "))
                if ans2 >= 1 and ans2 <= l:
                    remove_contact(ans2, contacts)
                    break
                elif len(str(ans2)) == 1 and ans2 == 0:
                    break
                else: print("Invalid input. Try again\n")
        case 3: search_contact(contacts)
        case 4: break
        case _: print("Invalid input. Try again\n")