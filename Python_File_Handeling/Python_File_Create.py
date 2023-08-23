# Syntax : open("filepath","mode")
# File path/name & mode both should be given as str

open("File_Handeling", "x")

# Note :
# I can specify the relative path of the file or absolute path of the file.
# Relative path of the file is basically the path of the file relative to the current working directory ex : File_Handeling.txt, since currently the control will be in Python_File_Handeling folder.
# Absloute path of the file is basically the path of the file from the root directory i.e. C:/Users/samarth.kulkarni/PycharmProjects/PythonConcepts/Python_File_Handeling/File_Handeling.txt
# By default the control will be in PWD.
# Use of Relative path is preferred over absolute
# I need to use '/' for navigation
# If file extension is not specified, by default it will create .txt file