import os

# function for initial opening of bank accoutns
def initial():
    # declaration and initialization of initial variables
    lsacc = []
    # for loading exissting accs from file to check duplicatess
    if os.path.exists("Accounts.txt"):
        with open("Accounts.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) > 0:
                    lsacc.append(parts[0])

    while 1:
        try:
            print("\n+---------- OPENING OF BANK ACCOUNTS ----------+")
            # input for accno
            accno = input("Enter Account Number: ")
            if not accno.isdigit() or len(accno) != 5:
                raise ValueError("Input must be exactly 5 digits.")
            
            # check for duplicate
            if accno in lsacc:
                print("\"Account Already Exist!\" Please try again...")
                continue # Skip the rest of the inputs and loop back to the start
            
            # input for accna
            accna = input("Enter Account Name: ")
            if not accna.replace(" ", "").isalpha():
                raise ValueError("Name should only contain letters and spaces.")
            if len(accna) == 0 or len(accna) > 30:
                raise ValueError("Name length must be between 1 and 30 characters.")

            # input for pin 
            pin = input("Enter PIN: ")
            if not pin.isdigit() or len(pin) != 4:
                raise ValueError("pin should contain exactly 4 digits")
            
            # input for initial balance
            bal = float(input("Enter Initial Balance: "))
            if bal < 0:
                raise ValueError("Initial balance cannot be negative")
            
            # writing to file 
            with open("Accounts.txt", "a") as file:
                # comma separated system for easy reading
                file.write(f"{accno},{accna},{pin},{bal}\n")
            
            # Add to current session list to prevent duplicates without restarting
            lsacc.append(accno)

            # create another stuff
            print()
            isexit = 0
            while 1:
                check = input("Create another account [Y/N]: ").upper()
                
                if check == 'Y':
                    break
                elif check == 'N':
                    isexit = 1
                    break
                else: 
                    print("invalid input. try again")
                    continue

            if isexit: 
                print("\"End of Program\"")
                break

        # excepsions
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.\n\n")
            
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n\n")


# function for atm simulation (phase 2)
def atm():
    try:
        # Prevent running atm if database doesn't exist
        if not os.path.exists("Accounts.txt"):
            print("No accounts exist yet. Please run initial() first.")
            return

        # read all data into a file using a lists of lists huhu
        with open("Accounts.txt", "r") as file:
            # splits each line by the comma so we can access individual pieces of data
            account_data = [line.strip().split(',') for line in file if line.strip()]

        attempts = 0
        account_found = False
        user_index = -1 

        # Accno verification (Max 3 attempts)
        while attempts < 3:
            search_acc = input("Enter Account Number: ")
            
            # loop to find accout
            for i in range(len(account_data)):
                if account_data[i][0] == search_acc:
                    account_found = True
                    user_index = i
                    break
            
            if account_found:
                break
            else:
                print("\"Sorry the Account doesn't exist!\"")
                attempts += 1
                
        if not account_found:
            print("Maximum attempts reached. Program automatically exiting.")
            return

        # verification of pin no.
        input_pin = input("Enter PIN: ")
        if input_pin != account_data[user_index][2]:
            print("Incorrect PIN. Program automatically exiting.")
            return

        # main menu for atm
        while 1:
            print("\nWelcome to PUP On-Line Banking Systems")
            print("1. Balance Inquiry")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Cancel")
            
            choice = input("Press the desired transaction: ")
            
            if choice == '1':
                # Convert the saved string balance to a float to display
                current_bal = float(account_data[user_index][3])
                print(f"Your Balance is P{current_bal:.0f}")
                
            elif choice == '2':
                try:
                    dep = float(input("Enter Amount: "))
                    if dep > 0:
                        new_bal = float(account_data[user_index][3]) + dep
                        # Save the updated balance back to our data list as a string
                        account_data[user_index][3] = str(new_bal) 
                    else:
                        print("Invalid amount.")
                except ValueError:
                    print("Invalid input. Please enter numbers.")
                    
            elif choice == '3':
                try:
                    wit = float(input("Enter Amount: "))
                    current_bal = float(account_data[user_index][3])
                    if 0 < wit <= current_bal:
                        new_bal = current_bal - wit
                        account_data[user_index][3] = str(new_bal)
                    else:
                        print("Invalid amount or insufficient funds.")
                except ValueError:
                    print("Invalid input. Please enter numbers.")
                    
            elif choice == '4':
                # OVERWRITE the text file with the new balances before exiting
                with open("Accounts.txt", "w") as file:
                    for acc in account_data:
                        file.write(f"{acc[0]},{acc[1]},{acc[2]},{acc[3]}\n")
                break
            else:
                print("Invalid choice. Please try again.")

    except Exception as e:
        print(f"An unexpected ATM error occurred: {e}")

# --- MAIN EXECUTION ---
initial()
atm()