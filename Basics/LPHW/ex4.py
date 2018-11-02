# Variables and Names

# defining cars variable and assigning value of 100
cars = 100
# defining space_in_a_car variable and assigning value of 4.0
space_in_a_car = 4.0
# defining drivers variable and assigning value of 30
drivers = 30
# defining passangers variable and assigning value of 90
passangers = 90
# calculating not driven cars and assigning the result to cars_not_driven variable
cars_not_driven = cars - drivers
# defining cars_driven variable and assigning drivers variable's value to it
cars_driven = drivers
# calculating carpool capacity and assigning the result to carpool_capacity variable
carpool_capacity = cars_driven * space_in_a_car
# calculating average pasangers per car
average_passengers_per_car = passangers / cars_driven


# printing out available cars
print("There are", cars, "cars available.")
# printing out value of drivers
print("There are only", drivers, "drivers available.")
# prin out empty cars
print("There will be", cars_not_driven, "empty cars today.")
# prin out carpool capacity
print("We can transport", carpool_capacity, "people today.")
# printing out how may passangers we have today
print("We have", passangers, "to carpool today.")
# printing out how many passangers we need to place to each car.
print("We need to put about", average_passengers_per_car, "in each car.")
