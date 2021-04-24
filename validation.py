# Validation module for atm_auth.py

# check if acct number exists
# if acct number is 7 digits
# if acct numb is an integer
def acct_num_validation(account_number):
    if account_number:
        try:
            int(account_number)
            if len(str(account_number)) == 7:
                return True
            else:
                print ('Account number must be 7 digits')
        except ValueError:
            #print('Invalid account number, account number should be an integer')
            return False
        except TypeError:
            #print('Invalid account type')
            return False
    else:
        print('Account number is required')
        return False

