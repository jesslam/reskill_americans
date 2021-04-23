# Conditionals
""" age = -1
height = 6

if(age >= 18 and height > 5):
    print("This person can be admitted.")
elif(age > 0 and age < 18 and height > 5):
    print("Sorry dude, try again when you're old enough.")
else:
    print("You are not alive.") """

number = 15
if number > 10:
    print("Yes number is greater than or equal to 10")
elif number == 10:
    print("Yes number is equal to 10")
else:
    print(f"{number} is not greater than 10")
# Condense into one line!
print(True if number > 10 else False)
print("Yes number is greater than or equal to 10" if number > 4 else f"{number} is not greater than 10")


