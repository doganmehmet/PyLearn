# READING AND WRITING THE FILES

"""
*   close -- Closes the file. Like File->Save.. in your editor.
*   read -- Reads the contents of the file. You can assign the result to a
variable.
*   readline -- Reads just one line of a text file.
*   truncate -- Empties the file. Watch out if you care about the file.
*   write('stuff') -- Writes "stuff" to the file.
"""

""" For now these are the important commands you need to know. Some of them
take parameters, but we do not really care about that. You only need to
remember that write takes a parameter of a string you want to write to the
file.
"""
# imprt argv module form sys package
from sys import argv

# assign argv to scrpt and filename for direct input in command line
script, filename = argv

# worn that the content in the file will be erased
print(f"We re going to erase {filename}")
# ask if user sure or not. if yes ask user to hit RETURN if not CTRL+C
print("If you do not want that, hit CTRL -C (C^).")
print("If you want that hit RETURN")

# if the user doesnt want and presses CTRL+C the program will stop if presses RETURN it will continue
input('>')
# open the file with write access
target = open(filename,'w')

# say user that the file is being trincated
print("Truncating the file. Goodbye!")
# truncate the file
target.truncate()   # truncate: fil'in icindekileri siler.

# say user that he needs to provide three line input
print("Now I'm going to ask you three lines.")

# ask for three line's input
line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

# say user that his input will be written to the file.
print("I'm going to write these to the file")

# write to the first line
target.write(line1)
target.write("\n") # go to next line

# write to the second line
target.write(line2)
target.write("\n") # go to next line

# write to the third line
target.write(line3)
target.write("\n") # go to next line

# say user that the file is being closed
print("And finally we close it.")
target.close() # close the file

# check sample.txt file used in this example to see how it has changed.
