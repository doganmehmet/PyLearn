# Classses are like modules

# You can think about a module as a specialized dictionary that can store Python code so you can access
# it with the . operator. Python also has another construct that serves a similar purpose called a class. A
# class is a way to take a grouping of functions and data and place them inside a container so you can
# access them with the . (dot) operator.

# If I were to create a class just like the mymodule module, I’d do something like this:

class Mymodule(object):
    def __init__(self):
        self.mehmet = "Hahahahahha"

    def apple(self):
        print("I'm apples")

# That looks complicated compared to modules, and there is definitely a lot going on by comparison,
# but you should be able to make out how this is like a ”mini-module” with MyStuff having an apple()
# function in it. What is probably confusing is the __init__() function and use of self.tangerine for
# setting the tangerine instance variable.

# Here’s why classes are used instead of modules: You can take this MyStuff class and use it to craft many
# of them, millions at a time if you want, and each one won’t interfere with each other. When you import
# a module there is only one for the entire program unless you do some monster hacks.
