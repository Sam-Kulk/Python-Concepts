# str i.e. String
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
a = ''
print(a)

# Looping through a string is done with for loop.

x = 'banana'
for i in x:
    print(i)

# length of a string
print(len(x))

# check the presence/absence of a sub-string in a string
x = 'Hi there, hello!!!'

print('Hi' in x)
print('abc' not in x)


# quotes are not allowed inside, but there is work around,to insert quotes inside a string simply I can use '' within ""  or vice-versa
a = "Hi there, 'asd' 'asd' jsb"
print(a)

# Enough