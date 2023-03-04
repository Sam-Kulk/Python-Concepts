# To store the empty string varaible
e = ''
print(e)

# * usage with string
print("Python "*3)

# slicing
a = 'Python'
print(a[1:3]) # from y to t(3-1)
print(a[1:]) # by default last index of the specified string will be considered as last index
print(a[:3]) # By default start index will be considered as 0
print(a[:-1]) # last index in the specified string will be ignored

# in operator use with string
b = 'Java'
h = 'Ja' in b
print(h) # T
print('Py' in b) # F

# not in operator use with string
print('Ja' not in b) # F
print('Py' not in b) # T

