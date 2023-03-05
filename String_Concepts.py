# To store the empty string varaible
e = ''
print(e)

# * usage with string
print("Python "*3)

'''
slicing
-----------
syntax: [start_index:stop_index:step]
1. here stop_index-1 will be considered
2. by default step will be 1
3. If step is positive then the cursor will move from left to right & if it negative
the cursor will move from right to left
4. By default start_index will be 0 or -1 based on step
5. By default stop_index will be last index, here last index will be included
'''
a = 'Python'
print(a[1:3])
print(a[1:])
print(a[:3])
print(a[:-1]) # last index in the specified string will be ignored
print(a[1:2:1])
print(a[-1:-3:-1])

# in operator use with string
b = 'Java'
h = 'Ja' in b
print(h) # T
print('Py' in b) # F

# not in operator use with string
print('Ja' not in b) # F
print('Py' not in b) # T

# string comparison
x = 'Python'
y = 'Java'
print(x == y)
print(x != y)

