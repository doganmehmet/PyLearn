# Types, Statements and Other Goodies
    # Data types
    # Flow control
    # Loops
    # Dictionaries
    # Exceptions
    # Other data types

# 3.3. Integers and floats
int_value = 33
print(type(int_value))

float_value = 33.3
print(type(float_value))

# we can convert an integer to float and a flot to integer if we really need to do so
print(type(float(int_value)))
print(type(int(float_value)))

# 3.4. Strings
string_value = "I'm a string"
print(type(string_value))

# some string methods
# .capitalize()
print("hello".capitalize())
# .replace()
print("hello".replace('o', 'a'))
# .isalpha()
print("hello".isalpha())
# .isdigit() - useful when converting to int
print("123".isdigit())
# .split()
print("some, csv, values".split(','))
# .format()
print("My name is {}, surname is {}".format('mehmet', 'dogan'))
print("My name is {0}, surname is {1}".format('mehmet', 'dogan'))
print("My name is {1}, surname is {0}".format('machine', 'car'))
# f"" - string interpolation
print(f"My name is {'mehmet'} surname is {'dogan'}")


# 3.5. Boolean and None
python_course = True
java_course = False
none_value = None

print(type(python_course))
print(type(java_course))
print(type(none_value))

# True represents 1 and False represents 0 in integer form
print(int(True))
print(int(False))

# similarly if we cast 0 to Boolean we get False, and casting 1 will yield to True
print(bool(1))
print(bool(0))

# 3.6. If Statements
number = 5
if number == 5:
    print("The number is 5")
else:
    print("The number is not 5")

# Truty and Falsy values
# Any value other than zero has Truty value
number = 5
if number: # this evaluates to True as number is truty
    print("Number is defined and truty")

number = 0
if number: # this evaluates to False as number is NOT truty
    print("Number is defined and truty")
else:
    print("Number is NOT defined and falsy")

# similarly a string that has any value or any text is truty. As long as it is not an empty string it is truty
text = "Python"
if text:
    print("Text is defined and truty")

text = ""

if text:
    print("Text is defined and truty")
else:
    print("Text is NOT defined and falsy")

alliens_found = None
if alliens_found:
    print("This will NOT execute")

if True:
    print("I m always turty")

if not True:
    print("This will NOT execute too")

# Ternary if Statements  - this is quite useful in list/dict comprehensions
print("Bigger") if 5 > 3 else print("smaller")
print("Bigger") if 3 > 5 else print("smaller")


# 3.7. Lists
student_names = []
student_names = ["Mehmet", "Dilara", "Derya", "Ahmet"]
print(student_names)

# Getting list elements
# index in python starts from 0
print(student_names[0])
print(student_names[1])
print(student_names[-1])
# replacing an element
student_names[-1] = "James"
print(student_names)


# List methods
# .append() - adding items to the list
student_names.append("Mery")
print(student_names)
# if some element is in a list
print("Mery" in student_names)
print("George" in student_names)
# length of list
print(len(student_names))
# deleting of an element from a list
del student_names[3]
print(student_names)
# also possible to remove an element via .pop() method
student_names.pop(1) # removing the element at index 1
print(student_names)

# if we do not provide any index value it removes the last element from the list
# Be careful!!!
student_names.pop()
print(student_names)


# slicing
print(student_names[1:]) # skips the 0th idexed element and gives the rest
print(student_names[:1]) # gives the elements till index 1-1
print(student_names[:]) # gives everything


# 3.8. Loops
# looping over list elements
student_names = ["Dilara", "Kemal", "Pinar", "Jing", "Yu", "Yong", "Mehmet"]
print(student_names)
for name in student_names:
    print(name)

print('_' * 10)
x = 0
for i in range(10):
    x += 10
    print("The value of x is {}".format(x))

print('_' * 10)

for i in range(5,10):
    print(i)

print('_' * 10)
for i in range(2,21, 2):
    print(i)

print('_' * 10)

# 3.9. Break and Continue
# print the elements untill we find 20
for i in range(100):
    print(i)
    if i == 20:
        break

print('_' * 10)
# skip  the elements 5, 10, 15
for i in range(20):
    if (i == 5) | (i == 10) | (i == 15):
        continue
    print(i)


print('_' * 10)

# 3.10. While Loops

x = 0
while x < 10: # will be executed while it is True
    print(f"Count is {x}")
    x += 1

# 3.11. Dictionaries - key/value pairs
student = {
            "name":     "Mehmet",
            "surname":  "Dogan",
            "id":       12354,
            "feedback": None
          }

print('_' * 10)
print(student)


all_students = [
    {"name": "Mehmet", "surname": "Dogan", "id": 12354, "feedback": None},
    {"name": "James", "surname": "Black", "id": 12355, "feedback": None},
    {"name": "Ceyda", "surname": "Klarnet", "id": 12356, "feedback": None},
    {"name": "Tayyip", "surname": "Erdogan", "id": 12357, "feedback": None}
]

print('_' * 10)
print(all_students)

print('_' * 10)
# getting the names of all students
for i in all_students:
    print(i["name"])

# if a key is not exist we will get a KeyError exeption if we use i["key"]
# But we can safely get a value for key using .get() method and we can assing default value in the case the key does not exist
print('_' * 10)
for i in all_students:
    print(i.get("name", "Unkown key"))

print('_' * 10)
for i in all_students:
    print(i.get("score", "Unkown key, score does not exist!"))


print('_' * 10)
# getting all keys from a dictionary - .keys() method
print(student.keys())

# getting all values from dictionary - .values() method
print(student.values())

print('_' * 10)
# deleting keys/values form dictionary
print(student)
del student["surname"]
print(student)



# 3.12. Exeptions
student = {
            "name":    "Mehmet",
            "surname": "Dogan",
            "id":      12354,
            "feedback": None
          }
# we handle exeptions in python wiht try/except
print('_' * 10)

try:
    print(student["score"])
except KeyError:
    print("Score is not defined!!!, please provide a valid key")


print('_' * 10)
print("This code executes")

# normally if we dont handle exeptions if program encounters an error it will stop running
# but if we handle it in the above way (with try/except) it will countinue to run the rest of the code and
# will just print the error
print('_' * 10)

try:
    print(student["surname"])
    print(student["name"] + 3)
except KeyError:
    print("surname is not defined!!!, please provide a valid key")
except TypeError:
    print("String and numbers can't be added!!!")
# adding a generic expection
except Exception: # this will handle all the errors but usually not good idea since it does not say what error is
    print("Unknown error!!!")

print('_' * 10)
print("This code executes")


# also possible to print default error messages
print('_' * 10)

try:
    print(student["surname"])
    print(student["name"] + 3)
except KeyError as error:
    print("surname is not defined!!!, please provide a valid key")
    print(error)
except TypeError as error:
    print("String and numbers can't be added!!!")
    print(error)
# adding a generic expection
except Exception: # this will handle all the errors but usually not good idea since it does not say what error it is
    print("Unknown error!!!")

print('_' * 10)
print("This code executes")

# but still we are not able to get the line number
# to get and print the line number where we've encountered error we need to use Traceback module
import traceback
print('_' * 10)

try:
    print(student["surname"])
    print(student["name"] + 3)
except KeyError:
    print("surname is not defined!!!, please provide a valid key")
    print(error)
    traceback.print_exc()
except TypeError as error:
    print("String and numbers can't be added!!!")
    print(error)
    traceback.print_exc()
# adding a generic expection
except Exception: # this will handle all the errors but usually not good idea since it does not say what error it is
    print("Unknown error!!!")
    traceback.print_exc()

print('_' * 10)
print("This code executes")



# 3.13. Other data types
# complex
# long - only in python 2
# bytes - squence of integers in the range of 0 to 255, sequence of strings, other objects etc.
# bytearray - similar to bytes
# tuple
# set
