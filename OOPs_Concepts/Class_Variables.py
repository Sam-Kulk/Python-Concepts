# Example 1(How to define & use class variables)
class MyClass1:
    a,b = 20,30
    def sum(self):
        return self.a*self.b   # I cannot directly use the class variable inside the method for that i need to use self keyword which represents the class

print(MyClass1().sum())

# Example 2(How to access the Local,Global & Class variables inside the method)
c = 5
class MyClass2:
    d = 10
    def add(self,e):
        print(e+0)     # Local variable in method
        print(c+0)     # Global variable in method
        print(self.d+0)  # Class valiable in method

MyClass2().add(15)

# How to access the local,global & class variables inside the method, when their names are same
x = 2
y = 4
class MyClass3:
    x = 3
    def oh(self,x):
        print(x)
        print(self.x)
        print(globals()['x']+globals()['y'])

MyClass3().oh(5)

