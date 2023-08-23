import re

x = 'The rain in Spain'

# search()
a = re.search("The",x)  # acts as contains
b = re.search("^The",x) # acts as starts with
print(a)
if a:
    print('There is a match')
else:
    print('There is no match')

print(b.span())
print(b.group())

# findall()
c = re.findall("ai",x)
print(c)

# split()
d = re.split("\s",x)
print(d)

e = re.split("\s",x,1)
print(e)

# sub()
print(re.sub("\s","-",x))

print(re.sub("\s","-",x,2))

# Note: All the RegEx should be a passed as string, as it is searched in the string