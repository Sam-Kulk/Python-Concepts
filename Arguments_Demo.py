# concept
def add(a,b):
    print(a+b)

add(2,4)  # 2 will be assigned to a & 4 to b, these are positional arguments

add(b=10,a=5)  # Keyword arguments

# Example 1 (Assigning default values to parameters)
def sub(a,b=1):  # default valued parameter should follow non default valued parameter
    print(a-b)

sub(10) # Default value i.e. 1 will be used
sub(10,2)  # Default value i.e. 1 will be overidden by 2

# Example 2 (Using combination of positional & keyword arguments)
def mul(a,b,c):
    print(a*b*c)

mul(1,b=2,c=3)  # Keyword arguments should follow positional agruments
