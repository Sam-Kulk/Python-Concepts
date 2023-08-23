# type() function is used to get the data-type of the value stored in the variable.
# If variable name is 'x', then I can use print(type(x))

# 1. int
a = 100
b = -100
print(type(a))
print(type(b))

# 2. float
c = 100.12
d = -100.12
print(type(c))
print(type(d))

# 3. str i.e. String

e = "Python"
f = 'J'
print(type(e))
print(type(f))

    # Multiline Strings
m = """A
B
C
"""
    # Note: Here it should be triple quotes
print(m)
print(type(m))

    # To store the empty string varaible
e = ''
print(e)

# Type Conversion
x = 914
y = 863.9

    # int to float(Basically it will add '.0' to the number)
u = float(x)
print(u)
print(type(u))

    # float to int(Basically it will just remove the . & decimal numbers)
v = int(y)
print(v)
print(type(v))

    # Note : I can convert str type number into int or float type with int() & float(), provided the str should be any number

    # int,float,boolean to str
w = 1
x = 1.2
y = True
print(str(w),str(x),str(y))

# 4. bool i.e. boolean
g = True
h = False
    # Here T & F should be uppercase
    # The numeric values 1 & 0 will be assigned internally to bool values True & False respectively.

print(type(g))
print(type(h))

# 5. NoneType
i = None
    # Here N in None should be uppercase
    # This is used to represent null value
print(type(i))

# Other important data-types in Python are list, tuple, dict & set which are part of collections