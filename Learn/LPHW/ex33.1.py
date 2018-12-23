# Exercise

def counting_func(to_value, increment):
    i = 0
    numbers = []
    while i < to_value:
        print("At the top i is {}".format(i))
        numbers.append(i)

        i += increment

        print("Numbers now: ", numbers)
        print("At the bottom i is ", i)
    return numbers

numbers = counting_func(10, 2)

print("The numbers: ")
for num in numbers:
    print(num)
