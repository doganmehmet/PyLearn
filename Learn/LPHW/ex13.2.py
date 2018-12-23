# importing argv from the sys module
from sys import argv

# variables that we will pass value in terminal
this_script, second_var, third_var, fourth_var, fifth_var = argv

# printing out the name of this script
print("This script is {}".format(this_script))

# we ask user to provide a number
value = input("Please provide a number: ")

print("The sum of my second, third, fourth, fifth variables and user given value is:", end = ' ')
# even do we pass integer values into those variables in terminal they are formatted as strings
print(int(second_var) + int(third_var) + int(fourth_var) + int(fifth_var) + int(value))


"""
What’s the difference between argv and input()? The difference has to do with where the user is required
to give input. If they give your script inputs on the command line, then you use argv. If
you want them to input using the keyboard while the script is running, then use input().
"""
