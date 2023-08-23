import os

# if os.path.exists("File_Handeling"):
#     os.remove("File_Handeling")
# else:
#     print("File doesn't exists")

# or

try:
    os.remove("File_Handling")
except:
    print("File doesn't exists")
