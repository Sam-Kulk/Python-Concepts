class A:
    x,y = 10,20
    def add(self):
        print(self.x+self.y)

class B(A):
    i,j = 20,30
    def sub(self):
        print(self.j-self.i)

class C(B):  # This is multi-level inheritance, C has var & methods of classes C, B & A
    p,q = 3,6
    def mul(self):
        print(self.p*self.q)

c = C()
print(c.q)
print(c.i)
print(c.x)
c.mul()
c.sub()
c.add()