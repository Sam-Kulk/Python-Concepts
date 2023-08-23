List1 = ['A','B','C']
List2 = ['D','E','F']

# List1.append('D')
# print(List1)

List1.extend(List2)
print(List1)

# insert() : Push the existing elements to right & inserts the new element in the specified index
List1.insert(0,'F')
print(List1)

# Add Any Iteratable

thislist = ['A','B','C']
thistuple = ('D','E','F')
thislist.extend(thistuple)  # I use even dict & set as well