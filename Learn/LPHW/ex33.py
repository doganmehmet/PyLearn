# While Loops

"""A while-loop will keep executing the code block under it as long as a boolean expression is True."""

""" Here’s the problem with while-loops: Sometimes they do not stop. This is great if your intention is to just keep looping until the end of the universe. Otherwise you almost always want your loops to end eventually."""

""" To avoid these problems, there are some rules to follow: 1. Make sure that you use while-loops sparingly. Usually a for-loop is better. 2. Review your while statements and make sure that the boolean test will become False at some point. 3. When in doubt, print out your test variable at the top and bottom of the while-loop to see what it’s doing. """

i = 0
numbers = []

while i < 6:
    print("At the top i is {}".format(i))
    numbers.append(i)

    i += 1

    print("Numbers now: ", numbers)
    print("At the bottom i is ", i)

print("The numbers: ")

for num in numbers:
    print(num)
