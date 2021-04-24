# Create a record
# Update record
# Read record
# Delete record
# CRUD

import os
import validation
user_db_path = 'atm-data/user_record/'
# Find user by account number key

# Create a file
# Name of the file would be {acct_num}.txt
# Add the user details to the file
# Return true
def create(acct_num, user_details):
    print('Create a new record')
    completion_state = False
    try:
        f = open(user_db_path + str(acct_num) + '.txt', 'x')
    except FileExistsError:
        print('User already exists')
        # If saving to file fails, delete the file that was created
        # check file contents before deleting
        # delete(acct_num)
        return False
    else:
        f.write(str(user_details))
        completion_state = True
    finally:
        f.close()
        return completion_state


def update(acct_num):
    print('Update user record')
# Find user by account number
# Fetch contents of the file
# Update file content
# Save file

def read(acct_num):
    #print('Read user record')
    is_valid_acct_num = validation.acct_num_validation(acct_num)
    try:
        if is_valid_acct_num:
            f = open(user_db_path + str(acct_num) + '.txt', 'r')
        else:
            f = open(user_db_path + acct_num, 'r')

    except FileNotFoundError:
        print('User not found')
    except FileExistsError:
        print('User does not exist')
    except TypeError:
        print('Invalid account number format')
    else:
        return (f.readline())
# Find user by account number
# Fetch contents of the file

def delete(acct_num):
    print('Delete user record')
    is_delete_successful = False
    if os.path.exists(user_db_path + str(acct_num) + '.txt'):
        try:
            os.remove(user_db_path + str(acct_num) + '.txt')
            is_delete_successful = True
        except FileNotFoundError:
            print('User not found')
        finally:
            return is_delete_successful 
    return True
        
# Find user by account number
# Delete user record (file)
# Return true if deletion succeeds

def doesEmailExist(acct_num, email):
    #print('Find user')
    all_users = os.listdir(user_db_path)
    for user in all_users:
        print(read(user))

# Find user record in the data folder

doesEmailExist(2714355, 'heres@email.com')