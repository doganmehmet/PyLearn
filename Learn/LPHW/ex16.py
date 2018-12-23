# Reading and Writing Files

# List of some useful commants for working wiht files

# close : closes the file. Like File->Save.. in your editor
# read : reads the contents of the file. You can assign the result to a variable
# readline : reads just one line of a text file
# truncate : empties the file. Watch out if you care about the file.
# write('stuff') : writes 'stuff' to the file
# seek(pasition) : goes to the specific positon in the file. i.e, seek(0) goes to the beginning.


from sys import argv

this_script, filename = argv

print(f"We're going to erase {filename}")
print("If you don't want that, hit CTRL-C(^C).")
print("If you do want that, hit RETURN.")

input('?')

print("Opening the file....")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print("And finally, we close it.")
target.close()
