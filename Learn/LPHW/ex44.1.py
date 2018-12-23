# Inheritance Versus Composition

# Override Explicitly

# The problem with having functions called implicitly is sometimes you want the child to behave differently. In this case you
# want to override the function in the child, effectively replacing the functionality. To do this just define a function with the
# same name in Child.

class Parent:

    def override(self):
        print("PARENT override()")


class Child:

    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()
