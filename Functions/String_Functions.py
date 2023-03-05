# Note: if string variable is s, then all string methods can be accessed by s.

# str function to store the string
s = str('Python')
print(s)

# len() - gives length of the string(length count will start from 1)
print(len(s))

# lower() - converts the given string to lowercase
l = s.lower()
print(l)

# upper() - converts the given string to uppercase
u = s.upper()
print(u)

# swapcase() - converts the case of the string
print(s.swapcase())

# startswith() - gives the result in boolean value
print(s.startswith("Py")) # case-sensitive

# endswith() - gives the result in boolean value
print(s.endswith("K")) # case-sensitive

# contains()
print(s.__contains__("off"))

# replace()
print(s.replace("on","off"))