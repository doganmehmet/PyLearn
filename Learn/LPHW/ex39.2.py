# Dictionary Exercise

# creating cities dictionary
countries = {
    "Turkey" : ("Istanbul", "Antalya"),
    "Qatar" : "Doha",
    "Singapore" : "Singapore",
    "Hong Kong" : "Hong Kong",
    "UAE" : "Dubai"
}

currency = {
    "TRY" : "Turkey",
    "QAR" : "Qatar",
    "SGD" : "Singapore",
    "HKD" : "Hong Kong",
    "AED" : "UAE"
}

print('_' * 30)
print("Dogan Invest's offices around the globe: ")
for country, town in list(countries.items()):
    print(town)

print('_' * 30)
print(f"TRY is used in cities: {countries[currency['TRY']]}")
print(f"QAR is used in cities: {countries[currency['QAR']]}")

# Getting an item from a dict safely

# getting USA from the dict
print('_' * 30)
city = countries.get("USA")
print(city)

# getting USA from the dict with default
print('_' * 30)
city = countries.get("USA", "Does Not Exist")
print(city)
