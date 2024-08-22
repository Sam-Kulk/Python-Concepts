thisdict = {
  "brand": "Ford",
  "model": "Mustang",
   1: 1964
}

# way1
print(thisdict["brand"])

# way2(recommended)
print(thisdict.get(1))

# Note:
# 1. keys()
print(thisdict.keys())

# 2. values()
print(thisdict.values())

# 3. items()
print(thisdict.items())

# Check if key exists or not
if "model" in thisdict:
    print("yes")
else:
    print("no")


# two dict comrarison
if thisdict == thisdict1:
    print('yes')

# E
