#  MORE FILES - COPY FROM ONE FILE TO ANOTHER

# copy from sample.txt to sample1.txt

# import argv module form sys package
from sys import argv
# imprtt exists module from os.path package to check if the file is exists
from os.path import exists

# assign argv to script, from_file, to_file for user to provide in command line
script, from_file, to_file = argv

# print info to user that the file is being copied
print(f"Copying from {from_file} to {to_file}")

# show user if the destination file is exis or not
print("Is the destination file existing?", exists(to_file))

# ask user if he wants this operation
print("Ready? hit RETURN to continue, CTRL+C to abort")
input('>')

# let's first open the file that we will copy from
file1 = open(from_file)
# take the content of the file and assign to infile variable later to copy it
infile = file1.read()

# now, open the another file that we'd like to copy to
file2 = open(to_file, 'w') # open the destination file in write mode

# let's write the content from first file stored in infile to the file2(to the destination file)
file2.write(infile)

# close the files
file1.close()
file2.close()

# give user info that it has been successfuly copied and file are closed.
print(len(infile), "bytes long input is copied and files are closed. Thanks!")
