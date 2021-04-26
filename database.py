# Create a record
# Update record
# Read record
# Delete record
# CRUD

import os
import validation
import datetime
user_db_path = 'atm-data/user_record/'
user_log_path = 'atm-data/auth_session/'
dateTime = datetime.datetime.now()
# Find user by account number key

# Create a file <acct_num>.txt
# Add the user details to the file, return true
# If saving to file fails, check file contents and 
# delete the file that was created via acct_num

def create(acct_num, first_name, last_name, password, email):
    user_details = first_name + ',' + last_name + ',' + password + ',' + email + ',' + str(0)
    print('Create a new record')
    if doesEmailExist(email):
        return False
    completion_state = False
    try:
        f = open(user_db_path + str(acct_num) + '.txt', 'x')
    except FileExistsError:
        print('User already exists')
        if is_file_empty(acct_num) == True:
            delete(acct_num)
    else:
        f.write(str(user_details))
        completion_state = True
    finally:
        f.close()
        return completion_state


# Find user by account number
# Fetch contents of the file
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
# Update file content
# Save file

def update(acct_num, user_info):
    if doesAcctExist(acct_num):
        f = open(user_db_path + str(acct_num) + '.txt', 'w')
        f.write(user_info)
        f.close()
        return True
    print('record not updated')
    return False


# Find user by account number
# Delete user record (file)
# Return true if deletion succeeds

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


# When user login succeeds, create file and track
# When user logs out, delete log file that was created

def create_user_log(acct_num):
    try:
        f = open(user_log_path + str(acct_num) + '.txt', 'x')
        f.write('Account number <' + acct_num + '> last logged in successfully at ' + str(dateTime) + '.')
    except FileExistsError:
        delete_user_log(acct_num)
        print('A duplicate session has been detected.  You have been logged out as a precaution, please log in again.')
        exit()

def delete_user_log(acct_num):
    if os.path.exists(user_log_path + str(acct_num) + '.txt'):
        try:
            os.remove(user_log_path + str(acct_num) + '.txt')
        except FileNotFoundError:
            print('No active session found')

def doesEmailExist(email):
    #print('Find user')
    all_users = os.listdir(user_db_path)
    for user in all_users:
        user_list = str.split(read(user), ',')
        if email in user_list:
            return True
    return False

def doesAcctExist(acct_num):
    all_users = os.listdir(user_db_path)
    for user in all_users:
        if user == str(acct_num) + '.txt':
            return True

def is_file_empty(acct_num):
    #print(os.stat(user_db_path + str(acct_num) + '.txt'))
    if os.stat(user_db_path + str(acct_num) + '.txt').st_size == 0:
        return True

def authenticated_user(acct_num, password):
    if doesAcctExist(acct_num):
        user_info = str.split(read(acct_num),',')
        if password == user_info[2]:
            return user_info
    return False

    
"""     all_users = os.listdir(user_db_path)
    for user in all_users:
        if email in (read(user)):
            print('first')
            return True
    return False """

""" def doesAcctExist(acct_num):
    #print('Find user')
    all_users = os.listdir(user_db_path)
    for user in all_users:
        if user == str(acct_num) + '.txt':
            print('here')
            print(user)
            #return True
    return False """
# Find user record in the data folder

#doesEmailExist(2714355, 'secondex@email.com')
