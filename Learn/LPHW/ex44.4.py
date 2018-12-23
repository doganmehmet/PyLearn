# Inheritance Versus Composition

# Composition

# Inheritance is useful, but another way to do the exact same thing is just to use other classes and modules,
# rather than rely on implicit inheritance. If you look at the three ways to exploit inheritance, two of the
# three involve writing new code to replace or alter functionality. This can easily be replicated by just
# calling functions in a module.


class Other:

    def implicit(self):
        print("OTHER implicit()")

    def override(self):
        print("OTHER override()")

    def altered(self):
        print("OTHER altered()")

class Child():

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")


son = Child()

son.implicit()
son.override()
son.altered()


# In this code We're not using the name Parent, since there is not a parent-child is-a relationship. This is
# a has-a relationship, where Child has-a Other that it uses to get its work done.


# We can see that most of the code in Child and Other is the same to accomplish the same thing. The
# only difference is that We had to define a Child.implicit function to do that one action. We could then
# ask ourselves if we need this Other to be a class, and could we just make it into a module named other.py?
