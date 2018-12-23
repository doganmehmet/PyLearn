# More Variables and Printing

# format string


"""
You embed variables inside a string by using a special {} sequence and then put the
variable you want inside the {} characters. You also must start the string with the letter f for ”format”,
as in f"Hello {somevar}". This little f before the " (double-quote) and the {} characters tell Python
3, ”Hey, this string needs to be formatted. Put these variables in there.”
"""

name = "Mehmet"
age = 28
height = 1.75
weight = 80
eyes = "Black"
teeth = "White"
hair = "Black"

print(f"Let's talk about {name}")
print(f"He's is {age} years old.")
print(f"He has {eyes} eyes, {teeth} teets and {hair} hairs")
print(f"He's {weight} kilos and {height} meters")
