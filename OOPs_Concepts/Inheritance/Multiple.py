# One multiple classes will be parent for a single child class

class A:
    a,b = 10,20
    def add(self):
        print(self.a+self.b)

class B:
    x,y = 10,20
    def sub(self):
        print(self.b-self.a)

class C(A,B):
    i,j = 10,20
    def mul(self):
        print(self.i*self.j)

# In class C
c = C()
c.mul()
c.sub()
c.add()