List1 = [1,2,3,4]
List2 = List1.copy()
print(List2)

List3 = []
List3 = List1.copy()
print(List3)

# Note: if i try to copy into the list which is already having some elements in it,
# then its existing elements will be overriden

List4 = [5,6,7]
List4 = List1.copy()
print(List4)
