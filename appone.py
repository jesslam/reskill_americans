# Mock ATM Project
# Jess Lam

import datetime
dateTime = datetime.datetime.now()

name = input("What is your name? \n" )
allowedUsers = ["Seyi", "Mike", "Love"]

#print(allowedUsers.index('Seyi'))
allowedPassword = ["passwordSeyi", "passwordMike", "passwordLove"]


if (name in allowedUsers):
    userId = allowedUsers.index(name)
    password = input("Your password? \n")
    while (password == allowedPassword[userId]):
        print("\nWelcome %s," % name) 
        print("The current date and time is: ")
        print(dateTime, end="\n\n")
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
            break
               
        else:
            print("Invalid option selected, please try again.")
            break

    else:
        print("Password Incorrect, please try again.")
        
else:
    print("Name not found, please try again.")