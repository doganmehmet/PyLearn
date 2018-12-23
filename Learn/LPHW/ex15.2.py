# Creating new files = Opening files in "w" or "x" mode

prompt = '> '
extention = ".txt"

print("Provide a file name you wanna create: ")

filename = input(prompt)
filename =  filename + extention

file = open(filename, mode = 'x')
# Note : 'x' and 'w' opens the files for writing only not for reading
# if we wanna open files for reading and writing we use r+ instead or r+ but the file should be existing already.

# writing something to the file
print("Write something to the file: ")
writing = input(prompt)
file.write(writing)

# closing the file first because we opened it in write format
file.close()

# now again opening it in read ('r') because we wanna read its content
file = open(filename)

# printing out the content of the file
print("Here is the content of your file: ")

print(file.read())

# closing the file
print("I'm closing the file")
file.close()
