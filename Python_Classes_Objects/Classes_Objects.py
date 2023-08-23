# create class with properties x & y
class MyCar:
    Color = 'Blue'   # Here x & y are properties i.e. a variables within the class
    Brand = 'Ford'   # Class variables

    def MyMethod(self):
        print('Hi there, hello car')


# create object
x = MyCar()   # Here MyCar() is an object
print(x.Brand)

x.MyMethod()

# Note : Single class can have multiple objects, but usually it is preffered to use a single object unless it is necessary
y = MyCar()
print(y.Brand)

# Pass statement
class MyClass:
    pass
