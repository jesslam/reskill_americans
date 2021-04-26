# Mock ATM Project - Authentication
# Jess Lam

#import datetime
import random
import validation
import database
from getpass import getpass
#dateTime = datetime.datetime.now()

def init():
    print("~~~Welcome to TNT ATM~~~")
    acct_exist_ask = input('Do you have an account? (Y or N) ')
    if acct_exist_ask == 'Y':
        login()
    elif acct_exist_ask == 'N':
        register()
    else:
        print('Invalid option')
        init()

def login():
    print('----- L o g  i n -----')
    acct_num = input('Please enter your account number: ')
    is_acct_num_valid = validation.acct_num_validation(acct_num)

    if is_acct_num_valid:
        pass_entered = getpass('Please enter your password: ')
        auth_user = database.authenticated_user(acct_num, pass_entered)
        #print(auth_user)
        if auth_user:
            database.create_user_log(acct_num)
            bankingOptions(acct_num, auth_user)
        else:
            print('Invalid account or password')
            invalid_login = int(input('\nSelect one:\n1. Retry Login\n2. Register\n'))
            if (invalid_login == 1):
                login()
            elif invalid_login == 2:
                register()
            else:
                print('Please try again')
                init()
    else:
        print('Account number invalid') 
        init()

"""         for acct_num, user_details in database.items():
            if acct_num == int(user_acct_entered):
                if user_details[3] == user_pass_entered:
                    print('Login Successful. \n')
                    bankingOptions(user_details) """

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
    password = getpass('Password: \n')

    acct_num = createAcctNum()
    
    #print('\nThe current date and time is: ')
    #print(dateTime, end="\n\n")
    #database[acct_num] = [first_name, last_name, password, email, balance]
    check_for_acct = database.create(acct_num, first_name, last_name, password, email)

    # Use the database module to create a new user record
    # Create a file
    if check_for_acct:
        print('Welcome %s %s, your new account number is %d' %(first_name, last_name, acct_num))
        print('Please log in to continue: \n')
        login()
    else:
        print('Something went wrong, please try again')
        register()

def bankingOptions(acct_num, user_info):
    print("These are the available options:")
    print("1. Withdrawal")
    print("2. Deposit")
    print("3. Complaint")
    print("4. Log out")
    
    selectedOption = int(input("Please select an option: ")) 
    # this needed to be converted to an int because input defaulted to a str
    if (selectedOption == 1):
        withdrawal(acct_num, user_info)

    elif (selectedOption == 2):
        deposit(acct_num, user_info)

    elif (selectedOption == 3):
        print(input("\nWhat issue would you like to report? "))
        print("Thank you, we appreciate you contacting us.\n")
        bankingOptions(acct_num, user_info)

    elif (selectedOption == 4):
        database.delete_user_log(acct_num)
        print("Thank you, goodbye.\n")
        exit()
            
    else:
        print("Invalid option selected, please try again.\n")
        bankingOptions(acct_num, user_info)

def createAcctNum():
    return random.randrange(1000000, 9999999)

def getAcctNum():
    return database.key()

def deposit(acct_num, user_info):
    print('++++Deposit++++')
    user_acct_balance = int(user_info[4])
    print('Your current balance is: $%d' % user_acct_balance)
    deposit_amt = int(input("How much would you like to deposit? "))
    user_acct_balance += deposit_amt
    user_info[4] = user_acct_balance
    user_info = user_info[0] + ',' + user_info[1] + ','+ user_info[2] + ','+user_info[3] + ',' + str(user_info[4])
    database.update(acct_num, user_info)
    user_info = user_info.split(',')
    print("\nYour deposit of $%d has been accepted. Your new balance is: $%d\n" % (deposit_amt,user_acct_balance))    
    bankingOptions(acct_num, user_info)

def withdrawal(acct_num, user_info):
    print('----Withdrawal----')
    user_acct_balance = int(user_info[4])
    print('Your current balance is: $%d' % user_acct_balance)
    withdraw_amt = int(input("How much would you like to withdraw? "))
    if withdraw_amt > user_acct_balance:
        print('\nInsufficient funds, transaction cannot be completed')
    else:
        user_acct_balance -= withdraw_amt
        user_info[4] = user_acct_balance
        user_info = user_info[0] + ',' + user_info[1] + ','+ user_info[2] + ','+user_info[3] + ',' + str(user_info[4])
        database.update(acct_num, user_info)
        user_info = user_info.split(',')
        print('\nYour new balance is $%d. Please take your cash totaling: $%s\n' % (user_acct_balance,withdraw_amt))
    bankingOptions(acct_num, user_info)



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



