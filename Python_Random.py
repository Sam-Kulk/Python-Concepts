# random module is used to generate random numbers.
# it has different functions to generate different types of random numbers.

import random

print(random.randrange(1,999))  # o/p number can repeat

x = [1,2,3,5,5,77,87]
random.shuffle(x)
print(x)
