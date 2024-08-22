# RegEx can be used to check if a string contains the specified search pattern.

import re

x = 'The rain in Spain'

# search()
a = re.search("The",x)  # acts as contains
b = re.search("^The",x) # acts as starts with
c = re.search("in$",x) # acts as ends-with
d = re.search("The rain in.Spain",x) # any charcter including space
e = re.search('The.*pain',x) # any character any number of times
f = re.search('rain|xyz',x) # or search

# metacharacters ^,$,.,>*,|

print(a)
if f:
    print('There is a match')
else:
    print('There is no match')

print(b.span())
print(b.group())

# findall()
c = re.findall("ai",x)
print(c)

# split()
d = re.split("\s",x)  # note : \s is single white space
print(d)

e = re.split("\s",x,1)
print(e)

# sub()
print(re.sub("\s","-",x))

print(re.sub("\s","-",x,2))

# Note: All the RegEx should be a passed as string, as it is searched in the string

# E