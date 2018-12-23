# Functions and Variables

# The variables in our function are not connected to the variables in your script.

# defining cheese_and_crackers function with two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You've {cheese_count} cheeses!") # printing amount of cheeses
    print("You've {} boxes of crackers".format(boxes_of_crackers)) # printing amount of crackers
    print("Man that's enough for a party!") # printing out smth
    print("Get a blanket. \n") # printing our smth


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30) # we are calling functions by giving values to arguments directly

print("OR, we can use variables from our script:")
amount_of_cheese = 10 # defining amount_of_cheese variable and assingning value of 10 to it
amount_of_crackers = 50 # defining amount_of_crackers variable and assingning value of 50 to it

# calling cheese_and_crackers function by passing above variables to arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6) # calling our function by giving values of some math to arguments

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) # combining values and variables to pass to arguments
