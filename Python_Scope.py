# The scope of a variable is basically the region within which I can access the variable
# By default the scope of any variable is within the region in which it is created

# 1. Local variable
# Created within the function or method

# 2. Global Variable
# Variable created outside of a function/method is global & it's scope is everywhere i.e. inside & outside the function

global_variable = 200
print(global_variable) # accessible
def myFunction1():
    local_variable = 100 # Local variable
    print(local_variable) # accessible
    print(global_variable) # accesible

# print(local_variable) # Not accessible

myFunction1()


# Useful example(Local & Global variable are different even though the name is same)
# This is a defualt behaviour

a = 1
def myFunction2():
    a = 2
    print(a)
print(a)

myFunction2()

# Global Keyword
# Use1 - This is basically used to create a global varaible from within the method/function

def myFunction3():
    global x
    x = 123
    print(x)

myFunction3()

print(x)

# Use2 - Updating the global variable from function
c = 7
def myFunction4():
    global c
    c = 5
    print(c)

myFunction4()

print(c)

# Note: SyntaxError: name 'abc' is assigned to before global declaration, will get this error if I declare & assign value to variable befor global declaration
# def myFunction4():
#     c = 6
#     global c

# Once I use global, after that if I assign any value to the variable, it will be referring to the global varibale