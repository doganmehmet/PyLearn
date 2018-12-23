# Inheritance Versus Composition

# Inheritance is used to indicate that one class will get most or all of its features from a parent class

# Implicit Inheritance : implicit actions that happen when you define a function in the parent but not in the child.

# defining class called Parent
class Parent:

    # defining method called implicit that takes self parameter
    def implicit(self):
        print("PARENT implicit()")

# defining class called Child which inherites from Child
class Child(Parent):
    # This shows you that if you put functions in a base class (i.e., Parent), then all subclasses (i.e., Child) will
    # automatically get those features. Very handy for repetitive code you need in many classes.
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
