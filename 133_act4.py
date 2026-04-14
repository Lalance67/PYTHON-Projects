# function for computing gross salary
def compute(position, num):
    match position:
        case "Instructor 1":
            return 29165 + (150 * num)
        case "Instructor 2":
            return 31320 + (200 * num)
        case "Instructor 3":
            return 33843 + (250 * num)
        case "Assistant Professor 1":
            return 36619 + (300 * num)
        case "Assistant Professor 2":
            return 39672 + (350 * num)
        case "Assistant Professor 3":
            return 43030 + (400 * num)
        case "Assistant Professor 4":
            return 46725 + (450 * num)
        case _:
            print(f"\nPosition '{position}' is not recognized.")
            return 0

# declaration and initialization of necessary variables       
employeeDetails = {}
employeeList = []
total = age = work_hours = 0
name = gender = status = college = position = ""

# looping until "N"
while 1:

    # Asking user for input
    try:
        name = input("\nEnter Employee Name: ")
        age = int(input("Enter Employee age: "))
        gender = input("Enter Employee Gender: ")
        status = input("Enter Employee Civil Status: ")
        college = input("Enter Employee College: ")
        position = input("Enter Employee Position: ")
        work_hours = int(input("Number of Hours Work (per month): "))
        
        if age < 0:
            raise ValueError("Age cannot be negative.")
        if not name or not position:
            raise ValueError("Name and Position are required fields.")
        
    except ValueError as e:
        print(f"invalid input: {e}")
        continue

    # storing user input in a dict
    employeeDetails = {"employee name": name, "age": age, "gender": gender, "status": status, "college": college, "position": position}
    
    # adding the newly made dict into a a list
    employeeList.append(employeeDetails)

    # computing and displaying gross salary of the employe
    grossSalary = compute(position, work_hours)
    print(f"\nTotal Monthly Gross Salary: Php {grossSalary:,}\n")

    # adding the total salary of every employee
    total += grossSalary

    # asking the user to input another or not
    isexit = 0
    while 1:
        check = input("Enter Another [Y/N]? ").upper()

        if check == "Y":
            break
        elif check == "N":
            isexit = 1
            break
        else:
            print("invalid input. try again")
    
    if isexit: break

# computing total numbers
male_count = sum(1 for emp in employeeList if emp["gender"].title() == "Male")
female_count = sum(1 for emp in employeeList if emp["gender"].title() == "Female")
single_count = sum(1 for emp in employeeList if emp["status"].title() == "Single")
married_count = sum(1 for emp in employeeList if emp["status"].title() == "Married")

# summary output
print("\nSUMMARY DETAILS\n")
print(f"Total Number of Employees: {len(employeeList)}")
print(f"Total Number of Male Employees: {male_count}")
print(f"Total Number of Female Employees: {female_count}")
print(f"Total Number of Single Employees: {single_count}")
print(f"Total Number of Married Employees: {married_count}")
print(f"Total Accumulated Salaries of ALL Employees: {total:,}")
