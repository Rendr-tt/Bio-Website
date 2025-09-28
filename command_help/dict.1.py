#how to use dictionaries

#creating a dictionary
my_cars = {
    "color": "red",
    "brand": "Honda",
    "model": "Civic",
    "kilometers": 10000,
    "year": 2022
}

#accessing a value
print("color dictionary:",my_cars["color"])

#updating a value
my_cars["color"] = "blue"
print("modified color dictionary:",my_cars["color"])

#deleting a value
del my_cars["year"]
print("deleted year dictionary:",my_cars)

#looping through a dictionary
for key, value in my_cars.items():
    print(key, value)

#checking if a key exists
if "color" in my_cars:
    print("color exists")

#checking if a value exists
if "Honda" in my_cars.values():
    print("Honda exists")

