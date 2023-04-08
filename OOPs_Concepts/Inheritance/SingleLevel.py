class A:
    a,b = 4,6
    def add(self):
        print(self.a+self.b)

class B(A):
    x,y = 6,4
    def mul(self):
        print(self.x*self.y)

b = B()

# I can use the methods & variables of the classes A & B from class B
b.add()
b.mul()
print(b.a,b.b,b.x,b.y)