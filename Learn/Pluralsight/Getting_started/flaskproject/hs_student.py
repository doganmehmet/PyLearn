
class HighSchoolStudent(Student):  # HighSchoolStudent is derived from parent (Student) class

    school_name = "High School"

    def __str__(self):
        """Overrides the instance memory position"""
        return "HighSchoolStudent Subclass of Student(Parent) Class"

    def get_name_capitalized(self):
        original_value = super().get_name_capitalized()
        return original_value + "-HS"
