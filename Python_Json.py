# In Python there is a built-in module 'json' which can be used to work with JSON type of data.

# If I hit request to API with python, then the response obtained will be JSON str
    # Ex : '{"name":"John","age":30, "city":"New York","male":true,"case":null}'
        # Here JSON will be within quotes internally, in above exmaple it is just for representataion.
        # key will be in ""
        # bool values will be true & false
        # null will represent empty data.
    # I cannot apply python on this JSON str, so to apply the python to this I need to convert this JSON str to Python Object i.e. dict & it is called as parsing

import json
x = '{"name":"John","age":30, "city":"New York","male":true,"case":null}'
y = json.loads(x)
print(y)
print(type(y))
print(y['age'])

# If I want to hit the request to any API with python, then JSON passed should be in JSON str not python object i.e. dict, this conversion is called as serialization
z = json.dumps(y)
print(z)
print(type(z))

# # formatting
# 1. indent parameter
a = json.dumps(y,indent=4) # also gives line breaks after each object/item
print(a)

# # 2. sort_keys
b = json.dumps(y,indent=4,sort_keys=True)
print(b)



