# ARGUMENT PASSING CON'T

""" What's the difference between argv and raw_input()?
The difference has to do with where the user is required to give input. If
they give your script inputs on the command line, then you use argv. If you
want them to input using the keyboard while the script is running, then use
raw_input().
"""

# impot the module to pass arguments
from sys import argv

script, first = argv

print(f"The argv[0] is {script}")
print(f"The argv[1] is {first}")

# ask input from user
name = input("What is your name?\n")
surname = input("and surname please\n")

print(f"Your name is {name}")
print(f"surname is {surname}")
