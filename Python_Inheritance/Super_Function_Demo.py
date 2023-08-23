# Case 1(Calling the super class method & variable from child class method)
class C:
    name = 'John'
    def m1(self):
        print("This is the method of class C")

class D(C):
    name = 'Sam'
    def m1(self):
        print("This is the method of class D")

        super().m1()
        # or C.m1(self)  Here I need to mention all the parameters including self
        print(super().name)
        # or print(C.name)
# Note : I can directly use the Class Name i.e. here C instead super() function, when the child class have multiple parents

d = D()

d.m1()