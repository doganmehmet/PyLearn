# Names, Variables, Code, Functions

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1 : {arg1}, arg2 : {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1 : {arg1}, arg2 : {arg2}")

def print_one(arg1):
    print("arg1 : {}".format(arg1))

def print_none():
    print("I got nothin'.")


print_two("Mehmet", "Dogan")
print_two_again("Mehmet", "Dogan")
print_one("First!")
print_none()
