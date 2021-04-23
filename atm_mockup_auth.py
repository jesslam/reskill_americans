# Mock ATM Project - Authentication
# Jess Lam

#import datetime
import random
import validation
#dateTime = datetime.datetime.now()

database = {
    7891789: ['Seyi', 'Super', 'seyi@email.com', 'passwordSeyi', 8620],
    4856947: ['Mike', 'Duper', 'mike@email.com', 'passwordMike', 34],
    2559367: ['Love', 'Rumer', 'love@email.com', 'passwordLove', 956]
    }


def init():
    print("~~~Welcome to TNT ATM~~~")
    acct_exist_ask = input('Do you have an account? (Y or N) ')
    if acct_exist_ask == 'Y':
        login()
    elif acct_exist_ask == 'N':
        register()

def login():
    user_acct_entered = input('Please enter your account number: ')
    is_acct_num_valid = validation.acct_num_validation(user_acct_entered)

    if is_acct_num_valid:
        user_pass_entered = input('Please enter your password: ')
        for acct_num, user_details in database.items():
            if acct_num == int(user_acct_entered):
                if user_details[3] == user_pass_entered:
                    print('Login Successful. \n')
                    bankingOptions(user_details)

        print('Invalid account or password')
        login()
    
    else: 
        init()
"""                 else:
                    print('Your password is incorrect.')
                    exit()
            else:
                print('Your account cannot be located.')
                exit() """


def register():
    print('*** Please complete your registration ***')
    email = input('Email address: \n')
    first_name = input('First Name: \n')
    last_name = input('Last Name: \n')
    password = input('Password: \n')
    balance = 0

    try:
        acct_num = createAcctNum()
    except OverflowError:
        print('Account could not be created')
        init()
    
    #print('\nThe current date and time is: ')
    #print(dateTime, end="\n\n")
    database[acct_num] = [first_name, last_name, password, email, balance]
    print('Welcome %s %s, your new account number is %d' %(first_name, last_name, acct_num))
    print('Please log in to continue: \n')
    login()


def createAcctNum():
    return random.randrange(1000000, 9999999)

def getAcctNum():
    return database.key()

def deposit(user):
    print('++++Deposit++++')
    # check the user's current balance and add the deposit
    user_acct_balance = user[4]
    print('Your current balance is: $%d' % user_acct_balance)
    deposit_amt = int(input("\nHow much would you like to deposit? "))
    user_acct_balance += deposit_amt
    print("Your deposit of $%d has been accepted. Your new balance is: $%d" % (deposit_amt,user_acct_balance))
    bankingOptions(user)

def withdrawal(user):
    print('----Withdrawal----')
    user_acct_balance = user[4]
    print('Your current balance is: $%d' % user_acct_balance)
    withdraw_amt = int(input("\nHow much would you like to withdraw? "))
    user_acct_balance -= withdraw_amt
    print('Your new balance is $%d. Please take your cash totaling: $%s' % (user_acct_balance,withdraw_amt))
    bankingOptions(user)

def bankingOptions(user):
    print("These are the available options:")
    print("1. Withdrawal")
    print("2. Deposit")
    print("3. Complaint")
    print("4. Exit")
    
    selectedOption = int(input("Please select an option: ")) 
    # this needed to be converted to an int because input defaulted to a str
    if (selectedOption == 1):
        withdrawal(user)

    elif (selectedOption == 2):
        deposit(user)

    elif (selectedOption == 3):
        print(input("\nWhat issue would you like to report? "))
        print("Thank you, we appreciate you contacting us.\n")
        bankingOptions(user)

    elif (selectedOption == 4):
        print("Thank you, goodbye.\n")
        exit()
            
    else:
        print("Invalid option selected, please try again.\n")
        bankingOptions(user)

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



