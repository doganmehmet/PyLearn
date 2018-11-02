# Parameters, Unpacking, Variables

from sys import argv
# read the WYSS section for how to run this

# this is a kind of unpacking. Instead of keeping all variable names in argv
# we are assigning them to different variables
script, first, second, third = argv

# script is the name of this script; ex13.py
# first, second and third are the variable names that we will pass when we are running
# from the terminal.

""" when we are running the script from the terminal we can put any variable names
for the first, second and third.
"""

print("The name of this script is {}".format(script))
print(f"The first variable is {first}")
print("The second variable is", second)
print("The third is {}".format(third))
