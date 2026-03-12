# Write a python code that will input record of student 
# that will be stored in a classList. The record of each
# student consist of name and final grade stored as tuple values.
# e.g. classList = [ ('John', 1.00), ('Alice', 1.25), ('Bob', 1.00),   
#                   ('David', 1.75), ('Eve', 5.00), ('Frank', 3.00), ('Grace', 4.00) ]


#declarations of required varibles
classList = []
passedList = []
failedList = []

#looping for error handling
while 1:
    #input of name
    name = input("Enter student name: ")
    if not name:
        print("name cannot be empty\n")
        continue
    
    #input of grade
    try:
        grade = float(input("Enter student grade: "))
    except ValueError:
        print("invalid input. try again\n")
        continue

    #using conditionals to determine passed and failed studs
    if grade < 3.00 and grade > 0.99:
        passedList.append((name, grade))
    elif grade < 5.01 and grade > 2.99:
        failedList.append((name, grade))
    else: 
        print("invalid input try again\n")
        continue
    
    #overall list
    classList.append((name, grade))

    #ask the user for more (with validation)
    choice = input("\nEnter more: [Y/N] ").upper()

    if choice == 'Y':
        continue
    elif choice == 'N':
        break
    else: 
        print("invalid")
        continue

#sort values
classList.sort()
passedList.sort()
failedList.sort()

#printing of required outputs
print("\n+--------------------------------------------------+")
print(f"Class list:\n{classList}")
print(f"total number of students: {len(classList)}")
print("+--------------------------------------------------+")
print(f"Passed Students:\n{passedList}")
print(f"total number of passed students: {len(passedList)}")
print("+--------------------------------------------------+")
print(f"Failed Students:\n{failedList}")
print(f"total number of failed students: {len(failedList)}")
print("+--------------------------------------------------+")
