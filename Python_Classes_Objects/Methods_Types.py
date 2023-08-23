class MyClass():
    def MyMethod1(self,a,b): # Instance Method
        print(a*b)

    @staticmethod
    def MyMethod2(a,b): # static method,there will not be default parameter self here
        print(a*b)

# calling the method
    # instance method
x = MyClass()
x.MyMethod1(2,4)

    # static
MyClass.MyMethod2(2,4)   # Can be called without the object
