
# class named Animal
class Animal():
    pass

# Dog is-an Animal
# class Dog has-a __init__ that takes self and name parameters
class Dog(Animal):

    def __init__(self, name):
        self.name = name

# Cat is-an Animal
# class Cat has-a __init__ that takes self and name parameters
class Cat(Animal):

    def __init__(self, name):
        self.name = name

# class named Person
# class Person has __init__ that takes self and name parameters
class Person:

    def __init__(self, name):
        self.name = name

        # person has-a pet of some kind
        self.pet = None


# class named Employee is-a Person
# class Employee has-a __init__ that takes self, name and salary parameters
class Employee(Person):

    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

# class named Fish
class Fish:

    def __init__(self, name):
        self.name = name


# class Salmon is-a Fish
class Salmon(Fish):

    def swim(self):
        return "{} is-a Salmon and swimming on sea and ocean".format(self.name)

# class Halibut is-a Fish
class Halibut(Fish):

    def swim(self):
        return "{} is-a Halibut and swimming on sea and ocean".format(self.name)

# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# marry is-a Person
marry = Person("Marry")

# marry has-a pat
marry.pet = satan

# Frank is-an Employee is-a Person and has-a 1000000 salary
frank = Employee("Frank", 1000000)

# Frank has-a pet rover
frank.pet = rover

# Flipper is-a Fish
flipper = Fish("alabalik")

# Crouse is-a Salmon is-a Fish
crouse = Salmon("crouse")
print('_' * 15)
print(crouse.name)
print(crouse.swim())

# Harry is-a Halibut is-a Fish
harry = Halibut("Harry")
print('_' * 15)
print(harry.name)
print(harry.swim())
