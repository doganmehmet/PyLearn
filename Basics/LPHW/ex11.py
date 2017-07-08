# INPUT/ ASKING QUESTIONS
# input() fuction takes inputs from the users
# check out more at https://docs.python.org/3/library/functions.html#input

# print the question and ask input to the users with input() fuction
print("How old are you?", end = ' ')
age = input()

# print the question and ask input to the users with input() fuction
print("How tall are you?", end = ' ')
tall = input()

# print the question and ask input to the users with input() fuction
print("How much do you weight?", end = ' ') # end = ' ' puts a space. This tells print to not end the line with a newline character and go to the next line.
weight = input()

# print the variables that we put input
print(f"So, you are {age} years old, {tall} tall, and {weight} weight\nyou look cool!")
