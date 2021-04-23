import copy

# Dictionary

fruit_basket = {
    "mango" : 40,
    "oranges": 30,
    "pawpaw": 3,
    "pineapple": [40, 30, 50, 70]
}

print("Original fruit basket: ", fruit_basket)

# Use a key to find the value
""" mangoes = fruit_basket["mango"] 
print("We have {} mangoes".format(mangoes)) """

# Get
""" apples = fruit_basket.get("apples", 34) # KeyError since this is not in dict
print("We have {} apples".format(apples)) """

# List all keys
""" all_fruit_keys =  fruit_basket.keys()
print(all_fruit_keys) """

# Remove from a value
""" fruit_basket["mango"] = fruit_basket["mango"] - 1
print("This is the new fruit basket: ", fruit_basket) """

# Add to dictionary
fruit_basket.update({"apples": 100})

# List of tuples
# Tuples store multiple items in a single variable, ordered and unchangeable
# This list is iterable and unpack with a key value and print 
# print(fruit_basket.items())

# Check if a key exists
""" if "apples" in fruit_basket:
    print(True) """

# Delete a value from the dictionary
""" fruit_basket.pop("pineapple")
print(fruit_basket) """

# Clear vs delete
# Clear empties the dictionary
""" fruit_basket.clear()
print(fruit_basket) """
# Delete can deletes the dictionary completely, so be careful using this!
""" del fruit_basket
print(fruit_basket) """


""" ------------ """
fruit_basket = {
    "mango" : 40,
    "oranges": 30,
    "pawpaw": 3,
    "pineapple": {"bad": 10, "good": 44}
}

# Copying dictionary
# Copying variable
""" new_fruit_basket = fruit_basket
print("New Fruit Basket: ", new_fruit_basket) """
# These both point to the same memory reference
""" print(id(new_fruit_basket)) # Pointer to fruit_basket
print(id(fruit_basket)) """

# Shallow copy constructs a new compound object, 
# inserts references in the object to those in the original
# Different memory obj reference but same values, 
# even if value in original is changed, ex: in nested op below

# Nested operation to access a dictionary within a dictionary
""" fruit_basket["pineapple"]["bad"] = 30 
new_fruit_basket = fruit_basket.copy()
print(fruit_basket) 
print(new_fruit_basket) # Both change "bad" value from 10 to 30 """

""" new_fruit_basket = fruit_basket.copy()
print(id(new_fruit_basket)) 
print(id(fruit_basket)) """


# Deep copy constructs a new compound object and recursively inserts
# copies of the objects found in the original
# This ch
new_fruit_basket = copy.deepcopy(fruit_basket)

fruit_basket["pineapple"]["bad"] = 30 

print(fruit_basket)
print(new_fruit_basket) # This retains the original value 10, not changed to 30
