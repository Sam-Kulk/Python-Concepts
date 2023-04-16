# Approach 1(Preffered)
import a
import b

obj1 = b.Bird()
obj2 = a.Animal()

obj1.bir()
obj2.ani()
print(b.g)  # Global Varaible
print(obj1.v)   # Class Variable

# Approach2
from a import *
obj3 = Animal()
obj3.ani()