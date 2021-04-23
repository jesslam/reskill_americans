# LOOPS: statements that are executed sequentially
aList = [1, 2, 3, 4]

"""for i in aList:
    print(i)"""

"""" for i in range(5):
    print(i) """

"""for i in range(1, 5):
    print(i)"""

"""for i in range(6):
    if (i != 0):
        print(i)"""

# While loop
# Execute a set of statements as long as a condition is true
# Increment the loop or else it will become infinite
# Requires relevant variables to be ready, like an indexing variable
"""i = 1
while i < 4:
    print(i)
    i += 1"""

"""count = 5
while count > 0:
    print(count)
    count -= 1"""

# Break statements
# Stop the look even if the while condition is still true
"""i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1"""

# Continue statements
# Stop the current iterations and continue with the next
"""i = 1
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)"""

# Else statement
# Run a block of code when the condition is no longer true

"""i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer < 6")"""

# FUNCTIONS: A reusable block of code that only runs when it is called, 
# may have parameters passed and can return data

"""def my_function():
    print("Hello from a function")"""

"""def nameOfFunction(name, count):
    print("%s called a function numbered %d" % (name,count))
nameOfFunction("Dude", 5)"""

# Calling a function
"""my_function()"""

# Arguments: Info passed into functions, separated by commas
"""def fname_function(fname):
    print(fname + ", nice to meet you!")

fname_function("Jimothy")"""

"""def flname_function(fname, lname):
    print(fname + " " + lname + " is your name.")

flname_function("Jimothy", "Halpert")"""

# Default parameter value
"""def default_country(country = "Norway"):
    print("I am from " + country)

default_country("Luxembourg")
default_country()"""

# Passing a list as an argument
"""def food_stuffs(food):
    for i in food:
        print(i)

vegetables = ["broccoli", "lettuce", "squash"]

food_stuffs(vegetables)"""

# Return values
"""def return_it(x):
    return 17 / x

print(return_it(4))
print(return_it(74.3))"""

# Pass statement: Use to avoid getting an error

#DICTIONARY: Store data in {"key":"value"} pairs
# Ordered (as of Python 3.7), changeable and doesn't allow duplicate keys

# Dictionary items can be referred to by key name
"""dict_items = {
    "fruit": "Apple",
    "vegetable":"Cucumber",
    "dairy":"Cheese",
    "dairy":"Yogurt" # overwrites "dairy" value
}
print(dict_items["dairy"])"""

# Method 1
dictionaryOne = {
    'key1':'value1',
    'key2':'value2',
    'key3':'value3',
}

# Method 2
"""dictionaryTwo = {}
dictionaryTwo['key13'] = 'value2'
dictionaryTwo['key14'] = 'value14'
dictionaryTwo['key18'] = 'value18'
dictionaryTwo['key21'] = 'value1745'

print(dictionaryTwo)"""

# Delete a dictionary item
"""del dictionaryTwo['key14']
print(dictionaryTwo)

dictionaryOne.pop('key1')
print(dictionaryOne)"""

# Loop dictionary

