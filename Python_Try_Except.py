# Notes:
# -------------
# Exception is an event which causes the termination of the program(Then error message will be thrown)
# The exception is type of error in python
# The exception will occur when invalid input is received.
# The exceptions in the python can be handled by try & expect blocks
# The exception needs to be handled so to make the user understand about the error with an error message.
# The else & finally blocks can also be used along with try & expect, however else is not mandatory, but expect/finally are mandatory when try is used


# Brief on blocks
# ----------------------
# The try keyword is used to define a block code in which exception can happen
# The except block is used to define a block of code which needs to be executed when the try block raises an exception
# The else keyword is used to define a block of code that needs to be executed when try block doesn't raise any error
# The finally keyword is used to define a block of code that needs to be executed regardless of whether the try block raises exception or not.


# Example 1
print("Program starts")
try:
    X = int(input("divisior: "))
    print(10/X) # this statement can have exception - ZeroDivisionError
except:
    print("Invalid input received")
print("Program ends")


# Example2 : There can be multiple expect statements for handeling different exceptions
# print("Program starts")
# try:
#     X = int(input("divisior: "))
#     print(10/X)
# except ZeroDivisionError:
#     print("Invalid input received leading to ZeroDivisionError")
# except SyntaxError:
#     print("Invalid input received leading to SyntaxError")
# except:  # default one should be at last, to used is there is a chance of getting some other unknown exceptions
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


# Raise an exception if condition is true
# syntax :
    # if condition:
        # raise <ExceptionName("Error message")>
# here error message is optional & exception name is mandatory & can be anything
# If exception to raise is not specified, then it will raise a RunTimeError

# Example 1
# x = -1
# if x<0:
#     raise TypeError("Only positive numbers are allowed")


# def num(x):
#     if x<=0:
#         raise ValueError
#     elif x%2 == 0:
#         print("Even number")
#     else:
#         print("Odd number")
#
# try:
#     x = int(input("Please enter number to checked: "))
#     num(x)
# except:
#     print("Please enter a positive value")