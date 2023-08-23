# Note: From API, the response received will be a JSON string & if i need to pass the JSON to API, it should be a JSON string

import json,Python_Inheritance.Types.SingleLevel

x = '{"name":"John","age":30, "city":"New York","male":true,"case":null}'
# Note:
# Here '' is just for representation of str here
# In Json format false,true & null will be there instead of True,False & None
# "" is valid in JSON not '' for string


# parse i.e. JSON str to dict
y = json.loads(x)
print(y)
print(y['age'])

# dict to JSON str
z = json.dumps(y)
print(z)

# formatting
# 1. indent parameter
a = json.dumps(y,indent=4) # also gives line breaks after each object/item
print(a)

# 2. seperator parameter
b = json.dumps(y,indent=4,separators=('.',"- "))
print(b)

# 3. sort_keys
c = json.dumps(y,indent=4,sort_keys=True)
print(c)


