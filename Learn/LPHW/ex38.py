# Doing Things to Lists

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are 10 things in that list. Let's fix that.")

stuff =  ten_things.split(' ')

more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() # if no index is provided it removes the last item in the list. Here it assings the removed item to the next one.
    print("Adding: ", next_one)
    stuff.append(next_one) # so we expect it should add Boy, Girl, Banana and Corn
    print(f"There are {len(stuff)} items in stuff list now.")


print("There we go: ", stuff)

print("Let's do some things with stuff.")

"""
Note: In lists we can only use index numbers to get items out of a list.
"""
print(stuff[1]) # printing the 2n element. Don't forget index starts from 0 in Python
print(stuff[-1]) # printing out the last element. Negative indexing starts from -1 and from the right
print(stuff.pop())  # printing out the last element - so it is dropped
print(' '.join(stuff)) # it should print out the join of ' ' (a space) with the stuff list
print('#'.join(stuff[3:5])) # it should print out the join of # with the stuff list's 4th to 5th elements

# .join() method: The join() method is a string method and returns a string in which the elements of sequence have been joined by str separator.

"""string_name.join(iterable)

string_name: It is the name of string in which
            joined elements of iterable will be
            stored."""
