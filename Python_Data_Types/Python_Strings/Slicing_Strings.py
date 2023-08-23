# Strings in Python are arrays
    # Square brackets can be used to access elements of the string.
    # indexing starts from '0' in python
v = "Samarth"
print(v[0])
print(v[1])

# String slicing
    # syntax: [start_index:stop_index:step]
    # By default step will be 1
    # If step is positive then cursor moves from left to right & vice versa
a = 'Python'
    # positive step(Cursor will move from left to right)
print(a[1:3]) # here it will stop_index -1 will be considered
print(a[1:]) # Here the string will be sliced till the end
print(a[:3]) # By-default '0' will be start_index
print(a[-4:-1]) # negative indexing starts from '-1' & it begins from right to left, but cursor will be moving from left to right.
        # Here alaways start point should be more than end

    # negative step(Cursor will move from right to left) It should be used when I want to fetch the string in reverse order
print(a[::-1]) # By-default the start index will be -1 & will go on till the end
print(a[-1:-4:-1]) # -stop_index+1= -1 will be considered
print(a[:-4:-1])
print(a[-1::-1])
    # Here if step is negative better to use negative start & stop index

# Note:
    # step is just for the cursor movement & indexing rules will remain same in both step cases.
    # if step is positive stop_index -1 will be considered & if step is negative, then stop_index +1, the whole idea is decrese the selection by 1
