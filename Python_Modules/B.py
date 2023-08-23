# One module contents can be used in the other module by import statement
# syntax: import module_name1,module_name2, so on ...
# syntax to use the functions/variables/classes from the imported module is -> module_name.function_name/variable_name/class_name.something inside class

import A,E
A.myFunction('Samarth')

print(A.list1[0:2])

print(E.a)

# Note: print(dir(A))
# This is not possible - print(dir(B))

