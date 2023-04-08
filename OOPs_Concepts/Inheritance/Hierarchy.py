# One class will be parent for the multiple child classes

class A:
    a,b = 10,20
    def add(self):
        print(self.a+self.b)

class B(A):
    x,y = 10,20
    def sub(self):
        print(self.b-self.a)

class C(A):
    i,j = 10,20
    def mul(self):
        print(self.i*self.j)

# In class B
b = B()
b. add()
b. sub()

# In class C
c = C()
c.mul()
c.add()