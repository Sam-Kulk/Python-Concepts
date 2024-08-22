# A date in Python is not a data type of its own, so I can't assign date-time of a varaible and work with it.

import datetime
x = datetime.datetime.now()
# print(x)

print(x.year)
# print(x.month)
# print(x.day)
# print(x.hour)
# print(x.minute)
# print(x.second)
# print(x.microsecond)

# I can continue even after now() like now().year


# Creating date with the datetime() class constructor
# y = datetime.datetime(2023,7,24)
# print(y)
# Note : I can even give time (2024,5,26,13,13,13,1233)

# Formatting the datetime value by strftime() Method using format codes.
print(x.strftime('%A')) # format code
print(x.strftime('%c'))
print(x.strftime('%X'))
