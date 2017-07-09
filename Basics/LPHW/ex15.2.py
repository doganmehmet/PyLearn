# OPENING AND READING FILES

# ask user to provide wiht the file name again
print("Type the file name to open you'd like to open")
file_name = input('>')

# open the file that user have given
txt = open(file_name)

# print the content from the file
print(txt.read())

# close the file
txt.close()

# check how to open a file from python shell in command line
