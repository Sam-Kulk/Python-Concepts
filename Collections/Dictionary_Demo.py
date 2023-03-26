# How to create a dictionary
Dic1 = {"X":100, "Y":200,"Z":100}
Dic2 = {}

# How to print the data stored in dictionary
print(Dic1)
print(Dic2)

# How to access the items in the dictionary
print(Dic1["Y"])
print(Dic1.get("Y")) # Using get()

# How to read the items from the dictionary using loop
for i in Dic1:
    print(i)  # This will print only Keys
    print(Dic1.get(i))  # This will print the Key's Value

for x, y in Dic1.items():
    print(x,y)  # This will print Key,Value

# How to check whether a particular Key is present in the Dictionary or not
if "X" in Dic1:
    print("Exists")
else:
    print("Not exists")

# How to find the total number of items in the dictionary
print(len(Dic1))

########################### Mutable ##########################################
# How to change the value of the key in the dictionary
Dic1["Z"] = 500
print(Dic1)

# How to add items to dictionary
Dic1["OOPs_Concepts"] = 900
print(Dic1)

# How to perform delete operation on dictionary
Dic1.pop("OOPs_Concepts") # Just to delete one item(Key:value)
print(Dic1)

del Dic1["X"]
print(Dic1)   # Using the del keyword

# Dic1.clear()
# print(Dic1)   # To delete all the items in the Dictionary

# del Dic1       # To delete the Dictionary variable
# print(Dic1)

# How to copy the items in one dictionary to another
Dic3 = Dic1   # without using copy()
print(Dic3)

Dic4 = Dic1.copy() # Using copy()
print(Dic4)

# Here i cannot do concatination operation to combine two dictionaries, if i try to
# do it will throw TypeError: unsupported operand type(s) for +: 'dict' and 'dict'