import datetime
x = datetime.datetime.now()
print(x)


print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)
print(x.microsecond)

# I can continue even after now() like now().year

# I cannot store a datetime value directly in a varaible, since datetime is not a datatype in python, instead I can just catch the returning datetime value from any method/function

# Formatting the datetime value by strftime() Method
print(x.strftime('%A')) # format code
print(x.strftime('%c'))
print(x.strftime('%X'))

# Creating date with the datetime() class constructor
y = datetime.datetime(2023,7,24)
print(y)