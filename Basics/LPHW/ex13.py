# PARAMETERS, UNPACKING, VARIABLES

""" You know how you type python3.6 ex13.py to run the ex13.py file? Well the
ex13.py part of the command is called an "argument." What we'll do now is
write a script that also accepts arguments.
"""

""" When known to the interpreter, the script name and additional arguments
thereafter are turned into a list of strings and assigned to the argv
variable in the sys module. You can access this list by executing import
sys. The length of the list is at least one; when no script and no arguments
are given, sys.argv[0] is an empty string. When the script name is given as
'-' (meaning standard input), sys.argv[0] is set to '-'. When -c command is
used, sys.argv[0] is set to '-c'. When -m module is used, sys.argv[0] is set
to the full name of the located module. Options found after -c command or -m
module are not consumed by the Python interpreter’s option processing but
left in sys.argv for the command or module to handle.
"""

from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("The first variable is:", first)
print("The second variable is:", second)
print("The third variable is:", third)

# also possible in this way
print(f"The script is called: {script}")
print(f"The first variable is: {first}")
print(f"The second variable is: {second}")
print(f"The third variable is: {third}")

# print argv[0] = script, argv[1] = first etc.
print(argv[0])  # print from the argument list

""" If we wanna check some documentation from python we can write i.e. pydoc
sys in terminal to check the documentation for sys module.
"""
