# Functions, Files, Yield, and Lambda
    # Functions
    # Function arguments
    # Adding students to App
    # Nested functions and closures
    # Opening, Reading, and Writing Files
    # Yield
    # Lambda Functions

# 4.3. Functions

students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student.title()
    return students_titlecase

def print_students_titlecase(): # this function does not return anything, just prints.. If we assign it to a variable we get
# nothing.
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

def add_student(name):
    students.append(name)

print('_' * 10)
print(students)

print('_' * 10)
student_list = get_students_titlecase()
print(student_list)

print('_' * 10)
add_student("Mehmet")
print(students)



# 4.4. Function arguments

# function arguments are local and only valid variables within the function. They are not accessible outside of function


students = []

# modifying add_student function
def add_student(name, student_id = None):
    student = {"name" : name, "student_id": student_id}
    students.append(student)

print('_' * 10)
add_student("Mehmet", student_id = 234)
print(students)

print('_' * 10)
add_student("Hello")
print(students)


# using args in the function
def var_args(name, *args):
    print(name)
    print(args)


print('_' * 10)
var_args("Mehmet", None, 1, 100, "Hello", "World", True)


# using kargs in the function
def var_kwargs(name, **kwargs):
    print(name)
    print(kwargs)

print('_' * 10)
# the difference of kwargs is that we need to use keywoards when we are calling the function
var_kwargs("Mehmet", desctiption = None, exam_passed = 1, score = 100, msg = "Hello, World", yobaz = False)



# 4.5. Adding students to our app

students = []

# modifying add_student function
def add_student(name, student_id = None):
    student = {"name" : name, "student_id": student_id}
    students.append(student)

print('_' * 10)
student_name = input("Enter student name:\n>")
id = int(input("Enter student ID:\n>"))
add_student(name = student_name, student_id = id)
print(students)



print('_' * 10)
def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student['name'].title() # added ["name"] since our list contains integers too (ID)
    return students_titlecase

print_students_titlecase()



# 4.6. Nested functions and closures


def get_students():
    students = ["Mark", "James"]

    def get_students_titlecase():
        students_titlecase = []
        for student in students:
            students_titlecase.append(student.title()) # nested functions have access to the variables defined in outher
            # function. Like students which was defined outside the nested function. This is clousure.
        return students_titlecase

    students_titlecase_names = get_students_titlecase()
    print(students_titlecase_names)

print('_' * 10)
get_students()



# 4.7. Opening, reading, and writing files

students = []


def add_student(name, student_id = None):
    student = {"name" : name, "student_id": student_id}
    students.append(student)


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student['name'].title()) # added ["name"] since our list contains integers too (ID)
    return students_titlecase


def print_students_titlecase(): # this function does not return anything, just prints.. If we assign it to a variable we get
# nothing.
    students_titlecase = get_students_titlecase()
    print(students_titlecase)



def save_file(student):
    try:
        f = open("students.txt", 'a')
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")

def read_file():
    try:
        f = open("students.txt", 'r')
        for students in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")



print('_' * 10)
read_file()
print_students_titlecase()


student_name = input("Enter student name:\n>")
id = int(input("Enter student ID:\n>"))

add_student(student_name, id)

save_file(student_name)


# 4.8. Yield - Generator functions

# we can use yield instead of return in order for us to create a generator function instead of a regular function


print('_' * 10)

students = []

def read_file():
    try:
        f = open("students.txt", "a")
        for student in read_students(f):
            students.append(student)
        f.close()
    except Exception:
        print("Could not read file")

def read_students(f):
    for line in f:
        yield line

read_file()
print(students)


# 4.9. Lambda functions

# they are generally useful in hiararchical functions. in functions which takes another functions as arguments
double = lambda x : x*2
print(double(10))
