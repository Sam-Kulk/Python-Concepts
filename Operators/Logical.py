'''
These operators are used to combine two conditions
Each condition will boolean value as output & these operators compare the output of two conditions
These operators return boolean values as output
In python there are no symbols for these operators, these are keywords here
'''

x = 2
y = 4

# 1. and
print(y>x and x<y) # Returns true if both the conditional statements are true

# 2. or
print(x==y or x<y) # Returns true if any one of the conditional statements is true

# 3. not
print(not(y>x and x<y)) # Reverses the result, returns False if the result is True & vice versa