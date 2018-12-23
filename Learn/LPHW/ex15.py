# Reading files

# we import argv feature from sys module
from sys import argv

# we use argv feature so that it will take two names
# the first, as always, script name and the second is the name of the file that we will open
this_script, filename = argv

# opends the file a person passes to the filename and assigns the result to txt variable
txt = open(filename)

# printing out the name of the file user has passed in command line
print("Here is your file: {}".format(filename))
# printing out the content of the file which its name provided by the user.
# showing the content of the file with .read() function.
print(txt.read())

# closing the file
print("closing the file")
txt.close()

# open() : opens the file
# .read() : reads the file
# .close() : closes the file


# sys.argv contains command line arguments.
