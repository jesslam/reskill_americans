# Validation module for atm_auth.py

# check in acct number exists
# if acct number is 7 digits
# if acct numb is an integer
def acct_num_validation(account_number):
    if account_number:
        if len(str(account_number)) == 7:
            try:
                int(account_number)
                return True
            except ValueError:
                print('Invalid account number, account number should be an integer')
                return False
        else:
            print ('Account number must be 7 digits')

    else:
        print('Account number is required')
        return False

