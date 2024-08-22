# Strings in Python are arrays
    # str[index] can be used to access elements of the string.
    # indexing starts from '0' in python
v = "Samarth"
print(v[0])
print(v[1])

# String slicing
    # syntax: [start_index:stop_index:step]
    # Note :stop_index:step is not mandatory

# Default-values
# =======================
# By default step will be 1(cursor moves from left to right)
# By default start_index will be 0(i.e. first index)
# By default last_index will be last_index+1(i.e. last character will be considered)
# stop_index:step is not mandatory

# Note :If step is negative then cursor moves from right to left.

a = 'Python'
    # positive step(Cursor will move from left to right)
print(a[1:3]) # here it will stop_index -1 will be considered
print(a[1:]) # Here the string will be sliced till the end
print(a[:3]) # By-default '0' will be start_index
print(a[-4:-1])
# Note:
# negative indexing starts from '-1' & it begins from right to left, but cursor will be moving from left to right.
# if the start index is negative, better to use stop index also as negative
# when step is positive, stop index should be alaways +1, while considering -1 will be considered.
# if step is negative stop_index-1 will be done irrespective of stop_index being positive or negative.

    # negative step(Cursor will move from right to left) It should be used when I want to fetch the string in reverse order
print(a[::-1]) # By-default the start index will be -1 & stop index will go on till the end i.e. -x-1.

# Note:
    # step is just for the cursor movement & indexing rules will remain same in both step cases for a given  string
    # if step is positive stop_index -1 will be considered & if step is negative, then stop_index +1, the whole idea is decrese the selection by 1

print(a[-1:-4:-1]) # -stop_index+1= -1 will be considered
print(a[:-4:-1])
print(a[-1::-1])

# I need to give the indexing based on step, the indexes should be in the way of cursor movement.

# Enough