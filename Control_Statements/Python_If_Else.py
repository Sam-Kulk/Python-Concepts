a = 1
b = 1

# 1. if
# ----------
# if a == b:
#     print('a is equal than b')

# 2. elif
# ----------
# if a > b:
#     print('a is greater than b')
# elif a < b:
#     print('a is less than b')

# 3. else
# ------------
# if a > b:
#     print('a is greater than b')
# elif a < b:
#     print('a is less than b')
# else:
#     print('a is equal to b')

# Note :
# 1. if & else keywords or statements can be used only once, elif can be used any number of times
# 2. elif & else should be used only after if is used

# short hand if(when I want to use only if)
# if a == b : print('a is equal to b')

# short hand if else(when I want to use only if & else)
# print('a is equal to b') if a == b else print('a is not qual to b')

# AND operator
a = 200
b = 33
c = 500
# if a > b and c > a:
#   print("Both conditions are True")

# OR operator
# if a > b or c < a:
#   print("Both conditions are True")

# Not operator
# if not b > a:
#     print('hi')

# Nested if
# if a > b:
#     print('a is greater than b')
#     if a > 100:
#         print('a is greater than 100')
#     elif a > 50:
#         print('a is greater than 50')
#     else:
#         print('a is less than 50')
# Note here I can use the if & others within elif & even if else scope

# pass statement
if a > b:
    pass
elif a == b:
    pass
else:
    pass
