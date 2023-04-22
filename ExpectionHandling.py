# Notes:
# Exception is an event which causes the termination of the program
# The exception will occur when invalid input is received.
# The exception is a type of error in python
# The exceptions in the python can be handled by try & expect blocks
# The else & finally blocks can also be used along with try & expect, however else is not mandatory, but expect/finally are mandatory when try is used


# Example 1
# print("Program starts")
# try:
#     X = int(input("divisior: ")) # this statement will/can have exception - ZeroDivisionError
#     print(10/X)
# except:
#     print("Invalid input received")
# print("Program ends")


# Example2 : There can be multiple expect statements for handeling different exceptions
# print("Program starts")
# try:
#     X = int(input("divisior: "))
#     print(10/X)
# except ZeroDivisionError:
#     print("Invalid input received leading to ZeroDivisionError")
# except SyntaxError:
#     print("Invalid input received leading to SyntaxError")
# except:  # default one should be at last
#     print("Invalid input received")
# print("Program ends")


# Example 3: else & finally blocks
# print("Program starts")
# try:
#     X = int(input("divisior: ")) # It will be always be executed
#     print(10/X)
# except: # Executed if exception is received
#     print("Invalid input received")
# else: # Executed only if there are no exceptions
#     print("No exceptions received, so executing further statements")
# finally: # It will be always be executed
#     print("Program ends")


# Example 4 : User defined exception
def num(x):
    if x<=0:
        raise ValueError
    elif x%2 == 0:
        print("Even number")
    else:
        print("Odd number")

try:
    x = int(input("Please enter number to checked: "))
    num(x)
except:
    print("Please enter a positive value")