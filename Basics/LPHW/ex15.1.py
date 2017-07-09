# READING FILES

# import the module
from sys import argv

# assign argv to script and file_name variables
script, file_name = argv

# open the file passed in terminal
txt = open(file_name)

# print the file name
print(f"Here is your file: {file_name}")
# show the content of the file via read()
print(txt.read())
