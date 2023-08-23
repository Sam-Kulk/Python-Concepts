tuple1 = (1,2,3,4,5)
tuple2 = (5,6,7,8,9)

# By using positive index
print(tuple1[0])
print(tuple1[2])

# By using negative index
print(tuple1[-1])
print(tuple1[-2])

# By using positive range index
print(tuple1[1:3])
print(tuple1[:3])
print(tuple1[1:])

# By using negative range index
print(tuple1[-3:-1])
# The selection when using negative index should be from left to right, as cursor moves from left to right, if done followed empty tuple will be returned

print(tuple1[-3:])
print(tuple1[:-3])

# Check element exists or not in the tuple
if 7 in tuple1:
    print('yes')
else:
    print('no')

# how to reverse a tuple
rev = tuple1[::-1]
print(rev)

# How to comapre two tuples
if tuple1 == tuple2:
    print("tuples are equal")
else:
    print("tuples are not equal")