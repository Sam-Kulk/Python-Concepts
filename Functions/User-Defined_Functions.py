# How to define & call the function
# Defination
def myFun():
    print("Hello")

    # Calling
myFun()

# Example 1(When function is expecting arguments)
def naming(name, age):
    print("The name is", name)
    print("The age is", age)

naming("Samarth", 24)


# Example 2(When function returns some result)
def add(a, b):
    return a + b

# sum = add(2, 4)
# print(sum)

print(add(2, 4))

# Example 3(When function returns more than one value)
def demo(a,b):
    if a>b:
        return a,b
    else:
        return b,a

result = demo(2,4)
print(result)
print(type(result))  # values will be stored in a tuple variable