# Case 1(Calling the super class method & variable from child class method)
class C:
    name = 'John'
    def m1(self):
        print("This is the method of class C")

class D(C):
    name = 'Sam'
    def m1(self):
        print("This is the method of class D")
        super().m1()  # or C().m1()
        print(super().name) # or print(C().name)

d = D()
d.m1()