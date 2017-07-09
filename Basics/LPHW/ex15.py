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

# ask user to provide wiht the file name again
print("Type the file name again")
file_again = input('>')

# again open the file that user have given
txt_again = open(file_again)
print(txt_again.read())


""" Documentation for open() can be found at
https://docs.python.org/3/library/functions.html#open
"""
