
class Employee: # simple Employee class with no atrributes and methods
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"

# all thos things; first, last, email are attributes of our class

# adding some actions. To do that we can add methods to our class

# let's say we wanna add some functionallity (action) which dispalys the full name of the employee
    def fullname(self): # if we do not put self parameter here we have to pass an instance to method when we are calling
        return "{} {}".format(self.first, self.last)

# difference between class and instance of a class
# class is basically a blueprint for creating instances
# and each unique employee that we create using Employee class would be an instance of that class

emp_1 = Employee(first = "mehmet", last = "dogan", pay = 1000000) # an instance
emp_2 = Employee("test", "user", 999999) # an instance

print('_' * 20)
print(emp_1.first)
print(emp_1.last)
print(emp_1.email)

print('_' * 20)
print(emp_1.fullname()) # when we call method on instance Python automatically pass the instance to the method
print(emp_2.fullname())

print('_' * 20)
# if we wanna use the class name then we need to pass instance to the funciton
print(Employee.fullname(emp_1)) # we we call method on class Python does not now what to pass
print(Employee.fullname(emp_2))

print('_' * 20)
print(emp_2.first)
print(emp_2.last)
print(emp_2.email)



#emp_1.first = "mehmet"
#emp_1.last = "dogan"
#emp_1.email = "mehmet.dogan@company.com"
#emp_1.pay = 1000000

#emp_2.first = "test"
#emp_2.last = "user"
#emp_2.email = "test.user@company.com"
#emp_2.pay = 999999
