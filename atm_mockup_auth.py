# Mock ATM Project - Authentication
# Jess Lam

import datetime
import random
dateTime = datetime.datetime.now()


#init: greeting, ask if acct exists

# If YES:
# LOGIN: check the database for the email address
# if the email address if found, print name, ask for password
# use the email address as key to verify password
# if password is incorrect, invalid msg, exit
# if email address is not found, invalid msg, exit

# When log in is successful:
# SHOW USER OPTIONS: ask for user to select an option
# if user selects valid option, redirect them to that option function
# if user selects invalid option, redirect them to SHOW USER OPTIONS

# If NO:
# REGISTER: ask for email address, first name, last name, password
# Add these values to the database, using email as key
# GENERATE RANDOM ACCT NUM, associate with key and redirect to log in

#name = input("What is your name? \n" )
#allowedUsers = ["Seyi", "Mike", "Love"]
#print(allowedUsers.index('Seyi'))
#allowedPassword = ["passwordSeyi", "passwordMike", "passwordLove"]

userInfo = []
database = {
    'seyi@email.com': {'Seyi', 'Super', 'passwordSeyi'},
    'mike@email.com': {'Mike', 'Duper', 'passwordMike'},
    'love@email.com': {'Love', 'Rumer', 'passwordLove'}
    }


def init():
    print("~~~Welcome to TNT ATM~~~")
    checkForAcct = input('Do you have an account? (Y or N) ')
    if checkForAcct == 'Y':
        login()
    elif checkForAcct == 'N':
        register()

def login():
    checkForEmail = input('Please enter your email address: ')
    if checkForEmail in database:
        email = database.get(checkForEmail)
        #print(email)
        checkForPass = input('Please enter your password: ')
        #print(email)
        #print(database.get(email[2]))
        if (checkForPass in database.get(checkForEmail)):
            print('Login Successful. \n')
            userOptions()
        else:
            print('Your password is incorrect.')
            exit()
    else:
        print('Your account cannot be located.')
        exit()

def register():
    print('*** Please complete your registration ***')
    userEmail = input('Email address: \n')
    userFirstName = input('First Name: \n')
    userLastName = input('Last Name: \n')
    userPass = input('Password: \n')
    newAcctNum = createPass()
    print('\nThe current date and time is: ')
    print(dateTime, end="\n\n")
    print('Welcome %s %s, your new account number is %d' %(userFirstName, userLastName, newAcctNum))
    database[userEmail] = {userFirstName, userLastName, userPass}
    print('Please log in to continue: \n')
    login()


def createPass():
    return random.randrange(1000000, 9999999)
    
def userOptions():
    print("These are the available options:")
    print("1. Withdrawal")
    print("2. Cash Deposit")
    print("3. Complaint")
    print("4. Exit")
    
    selectedOption = int(input("Please select an option: ")) 
    # this needed to be converted to an int because input defaulted to a str
    if (selectedOption == 1):
        print("You selected %s." % selectedOption)
        withdrawAmt = int(input("\nHow much would you like to withdraw? "))
        print("Please take your cash totaling: $%s" %withdrawAmt)

    elif (selectedOption == 2):
        print("You selected %s." % selectedOption)
        depositAmt = int(input("\nHow much would you like to deposit? "))
        print("Your deposit of $%d has been accepted. Your current balance is: $" %depositAmt + str(depositAmt + 150))

    elif (selectedOption == 3):
        print("You selected %s." % selectedOption)
        print(input("\nWhat issue would you like to report? "))
        print("Thank you, we appreciate you contacting us.")

    elif (selectedOption == 4):
        print("Thank you, goodbye.")
        exit()
            
    else:
        print("Invalid option selected, please try again.")
        userOptions()

init()

"""else:
    print("Password Incorrect, please try again.")
    
else:
print("Name not found, please try again.")"""

"""if (name in allowedUsers):
    userId = allowedUsers.index(name)
    password = input("Your password? \n")
    while (password == allowedPassword[userId]):
        print("\nWelcome %s," % name) 

        """



