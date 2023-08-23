# Overriding method & variables, basically it is done to improve the code without affecting the code in the super class
# The properties & functions i.e. methods in the child class will override the same properties & functions i.e. methods in the parent class
# It is even true with respect to the __init__() function as well

class A:
    x = 100
    def myFunction1(self):
        print(self.x)

class B(A):
    x = 120
    def myFunction1(self):
        print(self.x**2)

b = B()

print(b.x)
b.myFunction1()