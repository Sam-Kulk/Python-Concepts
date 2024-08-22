# I cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

List1 = [1,2,3,4]
List2 = List1.copy()

List1[0] = 9
print(List1,List2)

List3 = []
List3 = List1.copy()
print(List3)

# Note: if i try to copy into the list which is already having some elements in it  then its existing elementswill be overriden

List4 = [5,6,7]
List4 = List1.copy()
print(List4)
