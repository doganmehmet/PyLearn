# Inheritance Versus Composition

# Alter Before or After

# The third way to use inheritance is a special case of overriding where you want to alter the behavior
# before or after the Parent class’s version runs. You first override the function just like in the last example,
# but then you use a Python built-in function named super to get the Parent version to call.

# defining class called Parent
class Parent:

    # defining method named altered that takes self argument
    def altered(self):
        print("PARENT altered()")

# defining class called Child inherits from Parent
class Child(Parent):

    # defining method named altered that takes self argument
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        # super(Child, self).altered(), which is aware of inheritance and will get the
        # Parent class for you. You should be able to read this as ”call super with arguments Child and
        # self, then call the function altered on whatever it returns.”
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()
