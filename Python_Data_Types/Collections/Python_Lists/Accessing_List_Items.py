List1 = ["Banana",'Apple','Mango','Kiwi','Orange']

print("*Positive Index*")
print(List1[0])
print(List1[2])
# Note : If I try to access the element in the list that doesn't exits, then I will get the error - IndexError: list index out of range
# print(List1[7])

print("*Negative Index*")
print(List1[-1])
print(List1[-2])

print("*Positive Index Range*")
print(List1[1:2]) # Last index-1

# Note: Here I will not get the index error, basically withing the specified range, whatever
# elements matches, the result will be provided, not matched or not present will be ignored
# print(List1[-10:23])
print(List1[:3])
print(List1[0:])

print("*Negative Index Range*")
print(List1[-4:-1])
''' here the cursor moves from left to right, so my selection must & should start from 
left & it should proceed to right, else it will return empty list '''

# Check if Item Exists
if "Kiwi" in List1: # Here "in" will form condition & return T or F
    print("Yes")

# how to reverse a tuple
rev = List1[::-1]
print(rev)

List1 = [1,2]
List2 = [1,2]

if List1 == List2:
    print("Lists are equal")
else:
    print("Lists are not equal")