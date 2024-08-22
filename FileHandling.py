# By default the python is having capability to handel txt file but not excel file.

# Writing data into txt file
file = open("C:\Demo Files\Python Practice.txt",'w') # windows format i.e. backward slash
# file will be opened in backend

file.write("First line...\n") # \n is for new line
file.write("Second line...\n")
file.write("Third line...\n")
file.write("Fourth line...\n")
file.close()

# here if i write the new line in the w mode then the existing data will be overriden

# Appending data in the txt file
file = open("C:\Demo Files\Python Practice.txt",'a')
file.write("Sixth line..\n")
# here if i write the new line in the w mode then the existing data will be overriden
# if file doesn't exists, then it will create a new one.
file.close()

# Reading the data from the txt file
file = open("C:\Demo Files\Python Practice.txt",'r')
print(file.read()) # will read & print all lines
# print(file.readline()) # will read & print first line
# print(file.readline(5)) # will read & print first five characters of the first line
file.close()

# If file is not present, then the error will be thrown.
# 'r' is default mode.
