# STRINGS AND TEXT
# f before the quotes and .format() -> this is a format syntax. however this formating method works with python3.6 and not compatible with 3.5 version

# Variable definitions
typs_of_people = 10
x = f"There are {typs_of_people} types of people"  # this formating method works with python3.6 and not compatible with 3.5 version.
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# print the variables
print(x)
print(y)

# print the text with formated x variable in it
print(f"I said: {x}")
# print the text with formated y variable in it
print(f"I also said: '{y}'")

# define a hilarious variable and assign False to it.
hilarious = False
# create a joke_evaluation variable assign the text to it
joke_evaluation = "Isn't that joke so funny?! {}"

# print the joke_evaluation and use the .format() method to format the string
print(joke_evaluation.format(hilarious)) # check what .format() does here

# definition of w and e variables
w = "This is the left side of...."
e = "a string with a right side."

# print the sum of w + e.
print(w + e)
