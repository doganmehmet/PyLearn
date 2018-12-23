# Objects Are Like Import

class Mymodule(object):
    def __init__(self):
        self.mehmet = "Hahahahahha"

    def apple(self):
        print("I'm apples")

# If a class is like a ”mini-module,” then there has to be a concept similar to import but for classes. That
# concept is called ”instantiate”, which is just a fancy, obnoxious, overly smart way to say ”create.” When
# you instantiate a class what you get is called an object.
# You instantiate (create) a class by calling the class like it’s a function, like this:

thing = Mymodule()

thing.apple()
print(thing.mehmet)


# That’s the basics of how Python does this ”mini-import” when you call a class like a function. Remember
# that this is not giving you the class but instead is using the class as a blueprint for building a copy of that
# type of thing.
