# List is mutable i.e. the elements/values stored in it can be changed

# How to create a list
List1 = [10,10.2,'Python',True] # Can contain any number & any type of data
List2 = [] # Empty list

# How to print the data in the list
print(List1)
print(List2)

# How to access the individual list elements
print(List1[0])
print(List1[3])
print(List1[-2])

# How to access the range of the list elements
print(List1[0:3])
print(List1[-4:-1])

# How to access all the list elements one by one with a loop
for i in List1:
    print(i)

# How to check whether a particular element is present in the list
if 'Python' in List1:
    print("Yes, element is present in the list")
else:
    print("No, element is not present in the list")

# How to get the length of the list
list_length = len(List1) # I need to use len function
print(list_length)

# How to change the list element
List1[0] = 'Java' # Any type of data can be replaced by any other type of data
print(List1)

# How to add the element into the list
List1.append("C#") # By-default the append function will add the element at the end of the list
print(List1)

List1.insert(1,'JavaScript')  # The insert function will add the element in the specified index position
print(List1)

# How to delete the existing element from the list
List1.pop(2) # By using pop function
print(List1)

del List1[3]  # By using del keyword
print(List1)

# List1.clear()  # It will clear all the list elements but still the list variable will be present
# print(List1)

# del List1 will delete the entire variable

# How to copy a list elements of a list into another list
# List2 = List1.copy()
List2 = List1
print(List2)

# How to combine two lists
List3 = [1,2,3]
List4 = ['OOPs_Concepts', 'B', 'C']
List5 = List3 + List4
print(List5)

# How to comapre two Lists
if List1 == List2:
    print("Lists are equal")
else:
    print("Lists are not equal")