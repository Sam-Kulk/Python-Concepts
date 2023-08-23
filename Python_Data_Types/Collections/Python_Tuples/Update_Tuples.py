tuple1 = (1,2,3,4,5)

list1 = list(tuple1)
print(list1)
# Now I can use the list concepts to add, edit & delete the elements
# later i can convert the list back to tuple

# add
list1.append(6)
print(list1)

# update
list1[4] = 3
print(list1)

# delete
list1.remove(1)
print(list1)

tuple1 = tuple(list1)
print(tuple1)