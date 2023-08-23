# function defination
# ------------------------
# def my_function():
#     # block of code
#     print('Hi there, hello!!')

# function calling
# -------------------
# my_function()

# function with parameter(s)
# ------------------------------
# def my_function(x,y):
#     print(x,y)
#
# my_function(1)

# M: function returning value(s) with return statement
# ------------------------------------
# def my_function1(x,y):
#     mul = x*y
#     return mul
# # or return x*y can also be used
#
# print(my_function1(2,3))

# def my_function2(a,b):
#     if a > b:
#         return a,b
#     else:
#         return b,a
#
# print(my_function2(2,4))  # returns tuple


# Arbitrary Arguments, *args
# def my_function(*kids):
#     print(kids[2])
# my_function('Sam','Ram','Cam')

# Arbitrary Keyword Arguments, **kwargs
# def my_function(**kids):
#     print(kids['fname'])
# my_function(fname ='Samarth',lname='Kulkarni')

# Passing List as an argument
# def my_function(my_list):
#     for x in my_list:
#         print(x)
#
# my_list = [1,2,3,4,5]
# my_function(my_list)

# pass statement
# def my_function():
#     pass