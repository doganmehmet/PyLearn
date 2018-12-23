
students = []

class Student:
    """docstring for Student."""

    school_name = "University of Warsaw"

    def __init__(self, name, last_name, student_id):
        self.name = name
        self.last_name = last_name
        self.student_id = student_id
        students.append(self)

    def __str__(self):  # override method. instead of printing the location in memory it overrides it and gives "Student"
        return "Student Class instance"

    def get_name_capitalized(self):
        """Returns the first letter of the student name capitalized"""
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name
