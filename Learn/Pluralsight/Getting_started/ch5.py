# Object Oriented Programming

# 5.3. Defining a class in python

# class Student:
#     pass
#
# mehmet = Student()
# print(mehmet)
#
# new_student = Student()
# print(new_student)

# 5.4. Adding methods to our class

# students = []
#
# class Student:
#
#     def add_student(self, name, student_id): # self refers to the instance of the class
#         """
#         Adds the student to the student list.
#         :param name: string - student name
#         :param student_id: integer - student ID
#         """
#
#         student = {"name" : name, "student_id" : student_id}
#         students.append(student)
#
# student = Student()
# student.add_student("Mehmet", 12345)
# print(students)


# 5.4. Constractor and other special methods

# students = []
#
# class Student:
#
#     def __init__(self, name, student_id): # self refers to the instance of the class
#         student = {"name" : name, "student_id" : student_id}
#         students.append(student)
#
#     def __str__(self): # override method
#         return "Student"
#
#
# mehmet = Student("Mehmet", 4352)
#
# print('_' * 10)
# print(students)
# print('_' * 10)
# print(mehmet)


# here we are still using students list. However by using attributes we can access to the names and id's off the instances

# 5.5. Instance and class attributes

# students = []
#
# class Student:
#     """docstring for Student."""
#
#     school_name = "University of Warsaw"
#
#     def __init__(self, name, student_id):
#         self.name = name
#         self.student_id = student_id
#         students.append(self)
#
#     def __str__(self): # override method. instead of printing the location in memory it overrides it and gives "Student"
#         return "Student Class instance"
#
#     def get_name_capitalized(self):
#         return self.name.capitalize()
#
#     def get_school_name(self):
#         return self.school_name
#
# mehmet = Student("Mehmet", 3256453)
# print('_' * 10)
# print(mehmet)
#
# print('_' * 10)
# print(Student.school_name)
#
# print('_' * 10)
# print(mehmet.name)
# print('_' * 10)
# print(mehmet.student_id)
# print('_' * 10)
# print(mehmet.school_name)

# 5.6. Inheritance and Polymorphism

students = []

class Student:
    """docstring for Student."""

    school_name = "University of Warsaw"

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):  # override method. instead of printing the location in memory it overrides it and gives "Student"
        return "Student Class instance"

    def get_name_capitalized(self):
        """Returns the first letter of the student name capitalized"""
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

class HighSchoolStudent(Student):  # HighSchoolStudent is derived from parent (Student) class

    school_name = "High School"

    def __str__(self):
        """Overrides the instance memory position"""
        return "HighSchoolStudent Subclass of Student(Parent) Class"

    def get_name_capitalized(self):
        original_value = super().get_name_capitalized()
        return original_value + "-HS"

mehmet = HighSchoolStudent("mehmet", 34525)  # we're still required to provide parameters as it carries the futures of it's paren
# t(Student) class
print('_' * 10)
print(mehmet)

print('_' * 10)
print(mehmet.school_name)

print('_' * 10)
print(mehmet.get_name_capitalized())

print('_' * 10)


# when to use Inheritance?
# like the cases similar to above. in the situations new class should have very similar features and some more

# In Python there is no access modifiers (as in C++). All methods are public and there is no real way to change that although
# many Python developers use the underscore prefix for method name (i.e. "_get_name_capitalize(self):") to denote that a method
# should not be overriden or even used directly.


# 5.7. Breaking our app into modules


# 5.8. Comments
# is used for single line comment
# PEP 8 rules on comment
# if it is a single line comment "# Some comment" - one space after pound sign
# if it is after the code "some_code  ## some comment" - tow space after the code and once space after the pound sign
# Between functions (not class functions/methods) there should be two line space
