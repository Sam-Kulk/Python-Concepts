# Python built-in methods for string
# Refer W3S's Python Strings/String Methods for all the methods
# Note: Most of the string methods can be accessed like s.stringMethod()

s = 'Hi there, hello'

# Miscellaneous methods(Most commonly used)

# 1. startswith() - gives the result in boolean value
print(s.startswith("Hi")) # case-sensitive

# 2. endswith() - gives the result in boolean value
print(s.endswith("oo")) # case-sensitive

# Special methods

# 1.len()
    # length of string starts from 1
    # I need to used it as below
print(len(s))

# 2. contains() # It is constructor
print(s.__contains__("off"))