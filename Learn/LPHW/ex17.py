# More Files

from sys import argv
from os.path import exists

this_script, from_file, to_file = argv

print("Copying from {} to {}".format(from_file, to_file))

file_copy_from = open(from_file)
txt_to_copy = file_copy_from.read()

print(f"The input file is {len(txt_to_copy)} bytes long.")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# closing first file
file_copy_from.close()

# now let's open the file in write mode to copy the text to
file_to_copy = open(to_file, mode = 'w')

# Copying
file_to_copy.write(txt_to_copy)

# closing second file
file_to_copy.close()
