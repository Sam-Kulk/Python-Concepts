# Non-Parametrized constructor
class MyClass1:
    def __init__(self):
        print("This is constructor")

MC = MyClass1()  # This will call the constructor

# Parametrized constructor
class MyClass2:
    def __init__(self,name):
        print(name)

MyClass2("Samarth")

# Example 1
class MyClass3:
    eid,ename,esal = "","",""

    def __init__(self,eid,ename,esal):
        self.eid = eid
        self.ename = ename
        self.esal = esal

    def empdetails(self):
        print("Employee ID:",self.eid,"Employee name:",self.ename,"Employee salary:",self.esal)

MC3 = MyClass3(7697,"Samarth",30000)
MC3.empdetails()