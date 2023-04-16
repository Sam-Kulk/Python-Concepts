# Calling function in another module
    # Approach 1(Preffered)
# import Calculator
# Calculator.add(2,2)
# Calculator.mul(3,3)

   # Approach 2
# from Calculator import *
# add(2,3)
# mul(3,2)

# Calling a function which is common in more than one module
    # Approach 1(Preffered)
# import Animal
# import Bird
# Animal.fly()
# Bird.fly()

    # Approach 2
from Animal import *
fly()
from Bird import *
fly()
