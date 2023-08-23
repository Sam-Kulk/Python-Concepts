class A:
    a,b = 2,4

    def myFuction(self):
        print(self.a*self.b)

# class B(A):
#     pass

class B(A):
    c = 6
    def myFuction1(self):
        print(self.c)

b = B()

# From class B I can access the properties & Functions of

print(b.a)
b.myFuction()

print(b.c)
b.myFuction1()














# class A:
#     a,b = 4,6
#
#     def add(self):
#         print(self.a+self.b)
#
# class B(A):
#     x,y = 6,4
#     def mul(self):
#         print(self.x*self.y)
#
# b = B()
#
# # I can use the methods & variables of the classes A & B from class B
# b.add()
# b.mul()
# print(b.a,b.b,b.x,b.y)