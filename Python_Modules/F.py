from A import myFunction,list1
from E import myFunction

# In this case the recent one will overide the earlier imported one

myFunction('Samarth')

# Not in the below case
# import A,E
#
# A.myFunction('Samarth')
# E.myFunction('Samarth')