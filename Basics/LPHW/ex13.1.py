# importing argv from sys module

from sys import argv

# let's umpack 2 variables
# the first one is always the name of this script

this_script, second_var = argv

print(f"I firstly unpacked {this_script}")
print("Later on, unpacked {}".format(second_var))


# sys - System-pecific parameters and functions


"""
This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.
"""

"""
sys.argv
The list of command line arguments passed to a Python script. argv[0] is the script name (it is operating system dependent whether this is a full pathname or not). If the command was executed using the -c command line option to the interpreter, argv[0] is set to the string '-c'. If no script name was passed to the Python interpreter, argv[0] is the empty string.
"""
