# PRINTING CON'T.

# define a variable called formatter. and assign a text that has four {}s in it to be formatted.
formatter = "{} {} {} {}"

# print 1 2 3 4. with format() function turn to formatter variable into a string
print(formatter.format(1,2,3,4))

# print one two three four
print(formatter.format("one", "two", "three", "four"))

# print True False False True
print(formatter.format(True, False, False, True))

# print four times {} {} {} {}
print(formatter.format(formatter, formatter, formatter, formatter))

# print the txt I'm Mehmet I love python
print(formatter.format(
        "I'm Mehmet",
        "I",
        "love",
        "python"
))
