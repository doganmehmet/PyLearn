# A Dictionary Example

# create a mapping of state to abbveriation
# defining states dictionary, the keys are "Oregon, "Florida", "California", "New York" and "Michigan"
states = {
    "Oregon" : "OR",
    "Florida" : "FL",
    "California" : "CA",
    "Ney York" : "NY",
    "Michigan" : "MI"
}


# create a basic set of states and some cities in them

#  defining cities dict, keys are "CA", "MI" and "FL"
cities = {
    "CA" : "San Fransisco",
    "MI" : "Detroit",
    "FL" : "Jacksonville"
}

# add some more cities
cities["NY"] = "New York" # adding "NY" : "New York" key value pair to cities dict
cities["OR"] = "Portland" # adding "OR" : "Portland" key value pair to cities dict

# print out some cities
print('_' * 40) # printing out _ fourty times
print("NY state has: ", cities["NY"]) # printing out the value pair of "NY" key in cities dictionary
print("OR state has: ", cities["OR"]) # printing out the value pair of "OR" key in cities dictionary

# do it by using the state then cities dict
print('_' * 40) # printing out _ fourty times
print("Michigan has: ", cities[states["Michigan"]]) # printing out the value for the key which is value passed from "Michigan" key in states dict as a key to cities dictionary.
# basically, states["Michigan"] gives the value pair of "Michigan" key in states dict. Then we pass the returning value to cities dict as a key
print("Florida has: ", cities[states["Florida"]]) # printing out the value for the key which is value passed from "Florida" key in states dict as a key to cities dictionary.

# print every state abbveriation
print('_' * 40) # printing out _ fourty times
for state, abrv in list(states.items()): # with for loop accessing the elements of returning list from list(states.items()) operation
    print(f"{state} is abbreviated as {abrv}") # printing out state name as a key and its abbreviation as a value

# now do both at the same time
print('_' * 40) # printing out _ fourty times
for state, abrv in list(states.items()): # states.items() creates a list with containing tuples. Each tupple consists of key-value pairs [(key, value), (key, value), ....]
    print(f"{state} is abbreviated as {abrv}") # printing out first key (represents state) and then its value pair
    print(f"and has city {cities[abrv]}") # and here printing out the city in that state. value in states dictionary is passed to as key in cities dictionary

# safely get an abbreviation by state that might not be there
print('_' * 40) # printing out _ fourty times
state = states.get("Texas") # safely, getting the value for "Texas" key
if not state: # printing out Sorry, no Texas in the case "Texas" key does not exist
    print("Sorry, no Texas")


# get a city with a default value
print('_' * 40) # printing out _ fourty times
city = cities.get("TX", "Does Not Exist") # safely, getting value for "TX" key from cities dict. We assign a default
# warning if "TX" key does not exist in cities dictionary.
print("The city for the state 'TX' is: {}".format(city)) # printing out the city for state "TX" ("TX" is key)
