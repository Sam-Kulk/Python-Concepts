"""
Variable is container to store data/value

1. Variable definition means declaring the variable with specific name & data type i.e. int x
2. Variable initialization means assigning value to the defined variable according to its data type i.e. int x = 100
3. In Python is a dynamically typed language, which means you don't need to specify the data type explicitly when
defining a variable, in the runtime it will be determined by the value assigned to it i.e.
I can just write a = 100

Rules for Python variables
============================
Refer W3schools Python Variables/Variable Names
"""

# Ways of defining & initializing the variables
# Way 1
x = 100

# Way 2
a,b = 100, "Python"

# Way 3
p=q=r = 100

# The variable reinitialization can be done with a new value of same, as well as of different data type
f = 123
print(f)
f = 12345
print(f)
f = True
print(f)