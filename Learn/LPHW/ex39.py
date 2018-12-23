# Dictionaries, Oh Lovely Dictionaries

"""
A Dictionary (or ”dict”) is a
way to store data just like a list, but instead of using only numbers to get the data, you can use almost
anything. This lets you treat a dict like it’s a database for storing and organizing data.
"""

""" What a dict does is let you use anything, not just numbers.
Yes, a dict associates one thing to another, no matter what it is
"""

"""
In dictionary, we get the values by thir key names. Key might be any immutable object like string, int, floats, tuples etc.
"""

"""
A dictionary is used to map or associate things you want to store
to keys you need to get them.
"""


# creating dictionary
stuff = {"name" : "Mehmet", "age" : 28, "height" : 1.73, "weight" : 75} # defining stuff dictionary

print(stuff['name']) # printing out value pair of key name in stuff dict
print(stuff['age']) # printing out value pair of key age in stuff dict
print(stuff['height']) # printing out value pair of key height in stuff dict
print(stuff['weight']) # printing out value pair of key weight in stuff dict

# adding elements to the stuff dictionary
stuff["education"] = "MA" # adding key-value pair to stuff dict (key = education, value = MA)
stuff["degree"] = "QF" # # adding key-value pair to stuff dict (key = degree, value = QF)
print(stuff) # printing out stuff dict

# we can also add numeric key values as well
stuff[1] = "Suleyman Demirel University" # adding key - value pair to stuff dict (key = 1, value = ""Suleyman Demirel University"")
stuff[2] = "University of Warsaw" # adding key - value pair to stuff dict (key = 2, value = "University of Warsaw")

print("The fist university is {}".format(stuff[1])) # printing out the value pair of key 1 in stuff dict
print("The second university is {}".format(stuff[2])) # printing out the value pair of key 2 in stuff dictionary

print(f"stuff dict is:\n {stuff}") # printing out staff dictionary

# removing the universitites
del stuff[1] # removing the key 1 from stuff dictionary
del stuff[2] # removing the key 2 from stuffdictionary

# printing out stuff dictionary
print(f"stuff dict is:\n {stuff}")
