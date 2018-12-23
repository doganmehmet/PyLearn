# Functions Can return Something

def add(a, b):
    print("Adding {} + {}".format(a, b))
    return a + b


def subtract(a, b):
    print("Subtractin {} - {}".format(a, b))
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Dividing {a} / {b}")
    return a / b

print("Let's do some math with jsut functions!")

age = add(20, 8)
height = subtract(200, 30)
weight = multiply(40, 2)
iq = round(divide(100, 1.5),2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
