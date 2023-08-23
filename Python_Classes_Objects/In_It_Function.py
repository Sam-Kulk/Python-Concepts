# __init__() is a built-in function & is also constructor
# This can exist in two types Non-Parametrized & Parametrized
# This or any constructor will be executed whenever a new object is created

# 1. Non-Parametrized constructor
class MyClass1:
    def __init__(self):
        print("This is constructor")

MC = MyClass1()  # This will call the constructor

# Parametrized constructor
class MyClass2:
    def __init__(self,name):
        print(name)

MyClass2('Samarth')

# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
class MyClass3:
    # eid,ename,esal = "","","", this is not mandatory

    def __init__(self,eid,ename,esal):
        self.eid = eid
        self.ename = ename
        self.esal = esal

    def empdetails(self):
        print("Employee ID:",self.eid,"Employee name:",self.ename,"Employee salary:",self.esal)

MC3 = MyClass3(7697,"Samarth",545000)
MC3.empdetails()