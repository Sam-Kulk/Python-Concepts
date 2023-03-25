global_variable = 10
print(global_variable)


def func():
    local_variable = 20
    print(local_variable)
    print(global_variable)


func()

# print(local_variable) # local variable cannot be accessed outside the function

# Example 1(Local & Global variable are different even though the name is same)
a = 200

def func1():
    a = 100
    print(a)     # Here local variable will be considered

func1()  # 100
print(a)  # Here global varaible will be considered i.e. 200

# Example 2 (Creating a global variable inside the function)
def func2():
    global x
    x = 108
    print(x)

func2()
print(x)

# Example 3 (Updating the global variable from function)
y = 250
print(y)
def func3():
    global y
    y = 500
    print(y)

func3()
print(y)