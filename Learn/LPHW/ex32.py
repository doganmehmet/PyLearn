# Loops and Lists

the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quartes"]

# this first kind of for-loop goes through a list
for number in the_count:
    print("This is count {}".format(number))


# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")


# also we can go through mixed lists too
# notice we have to use {} since we do dont know what's in it
for i in change:
    print("I got {}".format(i))


# we can also built lists, first start with an empty one
#elements = []
elements = range(6)

# then use the range function to do 0 to 5 counts
#for i in range(6):
#    print("Adding {} to the list".format(i))
#    # append is a function that lists understand
#    elements.append(i)

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")
