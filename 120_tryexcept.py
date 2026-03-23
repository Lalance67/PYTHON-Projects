# try and except
# else then finally

# x = 10

# try:
#     print(x)
# except NameError: 
#     print("var x not defined")
# except ValueError:
#     print("invalid input try again")
# else:
#     print("Nothing went wrong")
# finally:
#     print("end of program")


# try: 
#     dividend = int(input("enter dividend: "))
#     divisor = int(input("enter divisor: "))
#     quotient = dividend / divisor
#     print(f"quotient is {quotient}")
# except ValueError:
#     print("invalid input. try again")
# except ZeroDivisionError:
#     print("zero in divisor in invalid")
# # except Exception as e:
# #     print("something went wrong")
# #     print(f"{e}")
# else:
#     print("all input are valid")
# finally:
#     print("ending the program")



# raise

# x = "hello"

# if not type(x) is int:
#     raise TypeError("error")