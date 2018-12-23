# Car Dictionary Example


# defining car dictionary

cars = {
    "brand" : ["Tesla", "Wolswagen", "Tofas", "Tesla"],
    "model" : ["Models S", "BMW", "Haci Murat", "Model X"],
    "fuel type" : ["Electricity", "Diesel", "Gasoline", "Electricity"],
    "doors" : [4, 4, 5, 6],
    "year" : [2020, 2007, 2021, 2020]
}

car_brand = {
    "Tesla" : ["Model S", "Model X"],
    "Tofas" : ["Dogan", "Haci Murat"]
}





print("Brand")
brand = input("> ")
print(car_brand.get(brand, "{brand} doesn't exist"))
print('_' * 35)

print("Model")
model = input("> ")
print(cars[brand][cars[brand].index(model)])
print('_' * 35)

# my_list = ['a', 'b', 'a']
# indices = [i for i, x in enumerate(my_list) if x == "a"]
# print(indices)
# #print(my_list[for i in indices])
# print(my_list[0,2])
