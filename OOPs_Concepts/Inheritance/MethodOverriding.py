# Overriding method & variables, basically it is done to improve the code without affecting the code in the super class
class A:
    name = "Samarth"
    def m1(self):
        print("This is the method of class A")

class B(A):
    name = "Naveen"
    def m1(self):
        print("This is the method of class B")

b = B()
b.m1() # Here the method in sub class will override the method in the superclass
print(b.name)  # Here the variable in sub class will override the variable in the superclass