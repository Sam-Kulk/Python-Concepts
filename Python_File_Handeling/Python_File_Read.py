# file = open("File_Handling.txt",'r')
# print(file.read())
# file.close()

# options
# 1. No of characters to read
# ------------------------------------
# file = open("File_Handling.txt",'r')
# print(file.read(8)) # 8 is not index, basically it is number of characters to read from beginning)
# file.close()

# 2. readline()
# ---------------------
# file = open("File_Handeling",'r')
# print(file.readline())
# print(file.readline())
# file.close()

# 3. loop
# ----------------------
# file = open("File_Handeling","r")
# for x in file:   # Every time a new line is assigned to x
#     print(x)
# file.close()

# Note : It is not suggested to use read(), read(n) & readlines in combo, as it will not give expected results
