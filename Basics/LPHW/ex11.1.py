# MORE EXERCISE WITH input()

# check more at https://docs.python.org/3/library/functions.html#input

""" input(): if the prompt argument is present, it is written to standard
output without a trailing newline. The function then reads a line from input,
converts it to a string (stripping a trailing newline), and returns that. When
EOF is read, EOFError is raised. -> basically input() function converts user input to string """

# how to convert a number to an integer then. check this out!
print("What is your name?") # since we did not use end = ' ' it will go one line down
name = input()

print("Also surname please!") # since we did not use end = ' ' it will go one line down
surname = input()

# put a numerical input. it will be first converted to as string via input() function then will be converted to an interher via int()
print("How old are you?") # since we did not use end = ' ' it will go one line down
age = int(input())

print(f"Your name is {name}, surname is {surname}, and you re {age} years old!\t thank you for info you have provided!!!")
