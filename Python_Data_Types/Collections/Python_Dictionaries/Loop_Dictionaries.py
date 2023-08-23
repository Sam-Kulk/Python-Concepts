dict1 = {'A':1,'B':2,'C':3}

# for keys
for x in dict1:
    print(x)

# for values
for x in dict1:
    print(dict1.get(x))

# for key-value pairs
for x,y in dict1.items():
    print(x,y)
