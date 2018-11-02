# Printing, Printing

# creating a variable formatter to format 4 things
formatter = "{} {} {} {}"

# formatting 1,2,3 and 4
print(formatter.format(1,2,3,4))

# formating "one", "two", "three", "four" with .format() method
print(formatter.format("one", "two", "three", "four"))
# formatting boolleans with h.format() method.
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))

print(formatter.format("Ben", "bunu", "format", "yaptim"))
