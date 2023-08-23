thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# way1
print(thisdict["brand"])

# way2(recommended)
print(thisdict.get("brand"))

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

