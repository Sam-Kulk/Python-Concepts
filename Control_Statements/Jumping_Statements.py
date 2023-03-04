'''
Jumping statements/keywords in python are break & continue
These are used to jump out of the loop, if certain condition is achieved
'''

# break keyword is used to exit the loop as per the condition specified
for i in range(1, 11):
    if i==6:
        break
    print(i)
print("Jumped out of loop")

# Note: for loop along with the break keyword can be used as an alternative of the while loop

# continue keyword is used skip a particular iteration(s) as per the condition specified
for i in range(12, 19):
    if i==12 or i==15:
        continue
    print(i)
print("Jumped out of loop")
