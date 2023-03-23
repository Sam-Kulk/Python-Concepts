# How to create a set
Set1 = {10, 10.5, 'Python', True}
Set2 = {}

# How to print the values/elements in the Set
print(Set1) # Unordered
print(Set2)

# Accessing the elements in the list(This is the only way)
for i in Set1:
    print(i)

# How to check if a particular element is present in the list or not
if 'Python' in Set1:
    print("Yes, the element is present")
else:
    print("No, the element is not present")

# How to add items to the set
Set1.add("Java") # To add a single element into the set
print(Set1)

Set1.update(['C#', 'Ruby']) # To add multiple values
print(Set1)

# How to find number of elements in the set
print(len(Set1))

# How to perform delete operation on set
Set1.remove("C#")
print(Set1)

Set1.discard(10)
print(Set1)

'''
Note : The only difference between the remove() & discard() is that when i try to
delete an element which is not present in the set by remove(), then i will get error
whereas if i do the same thing with update(), then error will not be throw 
'''
# Set1.clear()
# print(Set1)

#  del Set1
# print(Set1)

# How to join two sets
S1 = {'a','b','c'}
S2 = {'d', 'e', 'f'}
S3 = S1.union(S2)
print(S3)