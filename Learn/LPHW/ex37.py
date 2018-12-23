# Symbol Review

# assert: ensures that something is True, if False throws an error
name_surname = "mehmet.dogan"
name_surname_splited = name_surname.split('.') # this will return a list
name, surname = name_surname_splited # this will unpack the list an assign the first element to name, second to surname

name == "amokachi" # this will return False
result = name == "amokachi"
print(f"Is name == \"amokachi\": {result}")
assert name == "mehmet" # this will return True
assert name == "amokachi" # but this will return error. To avoid error, name should be correct; name == "mehmet"
# so it ensures that something is True

numbers = "12345"
numbers_splited = numbers.split('.')[:3] # split the numbers by . and take the first three elements
# the thing with above is, elements of the returning numbers_splited list is strings. We need to convert them to integers/floats
x, y, x = numbers_splited # first, unpacking the list
x, y, z = int(x), int(y), int(z) # then tupple-like assigning the variables to themself by coercing to integers
print("The x is: {}, y is: {} and z is: {}".format(x,y,z))
print(f"The type of x is: {type(x)}, y is: {type(y)} and z is: {type(z)}")

# or another smart way is
x, y, z = list(map(int, numbers.split('.')[:3])) # this is automatically coerced to integer and assigned to x, y and z


# try except: try this block, and if exception, go to except

# the try block will generate an exception becasue alfa is not defined
try:
    print(alfa) # here it will not give error instead will generate exception even do alfa is not defined
except:
    print("An exception has occured")

# but
print(alfa) # will generate an error becasue x is not defined. This is a NameError

#
try:
    print(alfa)
except NameError: # since alfa is not defined and is normally a NameError this except block will be executed.
    print("Variable alfa is not defined")
except:
    print("something else went wrong")


# finally : the finally block, if specified, will be executed regardless if the try block raises an error or not.
# but if there is an error except block will be excecuted too.
try:
    print(alfa)
except NameError:
    print("Variable alfa is not defined") # this will be executed since try block will raise NameError
except:
    print("something else went wrong")
finally:
    print("This will be executed no matter what") # this will be excecuted too since finally block excecutes no matter what.


# warning module : Warning messages are typically issued in situations where it is useful to alert the user of some
# condition in a program, where that condition (normally) doesn’t warrant raising an exception and terminating the program.

# Python programmers issue warnings by calling the warn() function defined in this module.

# warnings.warn(message, category=None, stacklevel=1, source=None)
# Issue a warning, or maybe ignore it or raise an exception. The category argument, if given, must be a warning category
# class (see above); it defaults to UserWarning.

import warnings

version = "124"

if version != "123": # since this will evaluate to True the below warning will get printed
    warning = "Old version of this package  is {} not good!, I didn't like that.".format(version)
    warnings.warn(warning, category = None)

# exec : run a string as Python

# This function supports dynamic execution of Python code. object must be either a string or a code object. If it is a string,
# the string is parsed as a suite of Python statements which is then executed (unless a syntax error occurs). If it is a code
# object, it is simply executed.
exec("a = 2") # 2 will be assigned to a even do "a = 2" is a string
print(a)


# raise : Raise an exception when things go wrong.
# The raise statement allows the programmer to force a specified exception to occur
raise NameError("Hi there!")
raise ValueError("Value error occured ulan")

# with : With an expression as a variable do.



# yiled : 
