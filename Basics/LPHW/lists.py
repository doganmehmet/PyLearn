# Lists
#   - vatiable-length
#   - mutable. their contents can be modified in-place
#   - definition : [] or list()

# creating a list of different data types
lst_all = [(1,2), 'haha', 1,5,7, False, None]
print(lst_all)

print("Replacing tuple wiht 0, \"haha\" wiht 100")
lst_all[0] = 0
lst_all[1] = 100
print(lst_all)

print("We were able to change our list's contents becasue it is mutable.")

# accessing its elements
print(f"It's last element is : {lst_all[-1]}")

# slicing
# printing out its first three eleents
print("It's first 3 elements {}".format(lst_all[:3]))

# printing out its every second elements
print("It's every second elements: ", lst_all[::2])

# printing out its elements in reversed order
print(f"It's eleents in reversed order {lst_all[::-1]}")

# concatenating list
lst2 = [1000000.0, 2000000.0]

# concatenating lists
print("Possible to combine lists")
lst_comb = lst_all + lst2
print(lst_comb)

# Methods
# .append() method. : adds element to the end
print("This is our list : {}".format(lst_all))
print("Adding ('A','B') to our list")
lst_all.append(('A', 'B'))
print(f"Our list, now, is: {lst_all}")

# .insert(position, value) method : adds value to an indicated position
print("Also adding ['M', 'e', 'h', 'm', 'e', 't'] for the very beginning of our list")
lst_all.insert(0, ['M', 'e', 'h', 'm', 'e', 't'])
print("Now, our list became {}".format(lst_all))

# .pop(position) method : the opposite of .insert(). pop method removes an element from indicated position
print("Now removing '0' from the list")
lst_all.pop(1)
print("Modified list is: {}".format(lst_all))

# .remove() method : removes a specified value
print("I didn't like it. I wanna remove ['M', 'e', 'h', 'm', 'e', 't'] from my list")
lst_all.remove(['M', 'e', 'h', 'm', 'e', 't'])
print(f"Removed : {lst_all}")


"""
Note : If performance is not a concern, by using append and remove,
you can use a Python list as a perfectly suitable "multiset" data structure.
"""

print("Performing a few checks")
print("Checking if our list contains the value \"100\"")
check = 100 in lst_all
print("Is '100' in our list {}".format(check))

# .extend() method : used to concatenate lists. It is more momory efficient than concatenating via +
print("I will not add to my list multiple elements. Cause' I am smart!!!, hahaha")
print("Adding 'I', 10, [True, False], 'cok' and False to my list")
lst_all.extend(['I', 10, [True, False], 'cok', False])
print("Already done!, here it is: {}".format(lst_all))

# Functions
# sort() function : sorts a list in-place. But, to be able to use it elements of list should be the same type.
print("I can't sort my list man becasue it's elements are not the same type", end = ' ')
print("But I'm smart and create a new list and sort")

new_lst = [5, 10, 1, 2, 0, 2, 2, 6, 0, 2, 7]
print(f"My new list is: {new_lst}")
print("Sorting my list now")
new_lst.sort()
print(f"Sorted : {new_lst}")

# reverse() function : reverses the list
print("You know I can also reverse the list.")
print("Reversing now...")
new_lst.reverse()
print("Already reversed: ",new_lst)


print("But do not forget my original list: ", lst_all)

# enumerate (numaralandirma) : returns a sequence of (i, value) tuples

print("I wanna print the indexes of elements")
print("The index numbers are: ",list(enumerate(lst_all)))

# It is easy to create a dictionary with key(index):value(elements of list) with this method
mapping = {}
for index, element in enumerate(lst_all):
    mapping[index] = element

print(mapping)
