# Defination of Class
class MyClass:    # Class name should be CamelCase
    def name(self):  # self is a default parameter & is part of the syntax
        print("Hello")

    def add(self,a,b):
        return a+b

# Defination of Objects
MyClass().name()   # Here MyClass() is an on object
print(MyClass().add(2,4))

v1 = MyClass()  # This is preffered way
v1.name()
print(v1.add(3,4))

# Instance & static method
class MyClass2:
    def greet(self):    # Instance method
        print("Bye")

    @staticmethod
    def mul(a,b):      # static method,there will not be default parameter self here
        return a*b

    # This is how i need to call instance method
v2 = MyClass2()
v2.greet()

    # The static method can be called without the object
print(MyClass2.mul(2,4))


# Single class can have multiple objects
class MyClass3:
    def oh(self):
        print("Hi")

Obj1 = MyClass3()
Obj1.oh()

Obj2 = MyClass3()
Obj2.oh()
