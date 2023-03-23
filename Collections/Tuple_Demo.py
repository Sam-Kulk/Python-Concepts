# How to create a Tuple
tuple1 = (10, 10.5, 'Java', False)
tuple2 = ()

# How to print the tuple values
print(tuple1)
print(tuple2)

# How to access the individual tuple elements
print(tuple1[2])
print(tuple1[3])
print(tuple1[-2])

# How to access the range of the tuple elements
print(tuple1[0:3])
print(tuple1[-4:-1])

# How to access all the tuple  elements one by one with a loop
for i in tuple1:
    print(i)

# How to check whether a particular element is present in the list
if 'Python' in tuple1:
    print("Yes, element is present in the tuple")
else:
    print("No, element is not present in the tuple")

# How to get the length of the tuple
length_tuple = len(tuple1)
print(length_tuple)

# How to copy a tuple elements of a tuple into another tuple
tuple3 = tuple1
print(tuple3)

# How to convert the tuple to list, then perform actions & again convert list to tuple
myList = list(tuple1)
myList[0] = 12
tuple1 = tuple(myList)
print(tuple1)

# How to join two tuples to form a new one
tuple4 = (10, 12, 13)
tuple5 = ('A', 'B', 'C')
tuple6 = tuple4 + tuple5
print(tuple6)

# How to comapre two tuples
if tuple3 == tuple1:
    print("tuples are equal")
else:
    print("tuples are not equal")