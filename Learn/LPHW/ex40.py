# Modules, Classes, and Objects

import mymodule

mymodule.apple()

print(mymodule.mehmet)

# Refer back to the dictionary, and you should start to see how this is similar
# to using a dictionary, but the syntax is different.

# let's compare
mydict = {'apple': "I'm apples!"}
print(mydict['apple'])

mydict['apple'] # get apple from dict
mymodule.apple() # get apple from the module
mymodule.mehmet # same thing, it's just a variable


# This means we have a very common pattern in Python:
    # 1. Take a key=value style container.
    # 2. Get something out of it by the key’s name.

# In the case of the dictionary, the key is a string and the syntax is [key]. In the case of the module, the
# key is an identifier, and the syntax is .key. Other than that they are nearly the same thing.
