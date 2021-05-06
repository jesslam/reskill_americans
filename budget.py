class Budget:

    def __init__(self, savings_acct_bal, checking_acct_bal):
        # initialize the expense type and amount of expense 
        # self.account_type = account_type
        self.savings_acct_bal = savings_acct_bal
        self.checking_acct_bal = checking_acct_bal
        #self.amount = amount

    def check_balance(self, account_type):
        # check the current account balance
        if account_type == 'savings':
            print(self.savings_acct_bal)
        elif account_type == 'checking':
            print(self.checking_acct_bal)
        else:
            print('Please select \"savings\" or \"checking\"')
    
    def deposit(self, account_type, amount):
        # add a dollar amount to the existing account balance
        if account_type == 'savings':
            self.savings_acct_bal += amount
        elif account_type == 'checking':
            self.checking_acct_bal += amount
        else:
            print('Please select \"savings\" or \"checking\"')

    def withdraw(self, account_type, amount):
        # subtract an amount from the current balance
        if account_type == 'savings':
            self.savings_acct_bal -= amount
            return(self.savings_acct_bal) 
        elif account_type == 'checking':
            self.checking_acct_bal -= amount
            return(self.checking_acct_bal)
        else:
            print('Please select \"savings\" or \"checking\"')

    def transfer(self, trans_from_acct, trans_to_acct, amount):
        # transfer an amount from one account to another account
        if(trans_from_acct == 'savings'):
            self.savings_acct_bal -= amount
            self.checking_acct_bal += amount
        elif(trans_from_acct == 'checking'):
            self.savings_acct_bal += amount
            self.checking_acct_bal -= amount
            print('Transfer complete')
            print('Savings balance: ' + str(self.savings_acct_bal))
            print('Checking balance: ' + str(self.checking_acct_bal))

class Category(Budget):

    def debit_transaction(self, amount, account_type):
        if account_type == 'savings':
            super().withdraw('savings', amount)
        elif account_type == 'checking':
            super().withdraw('checking', amount)
        
    def food(self, amount, account_type):
        self.debit_transaction(amount, account_type)
        print('%.2f' %amount + ' withdrawn as a food expense from ' + account_type)
 
    def clothing(self, amount, account_type):
        self.debit_transaction(amount, account_type)
        print('%.2f' %amount + ' withdrawn as a clothing expense from ' + account_type)

    def car(self, amount, account_type):
        self.debit_transaction(amount, account_type)
        print('%.2f' %amount + ' withdrawn as a car expense from ' + account_type)


obj = Category(34, 753)
obj.deposit('checking', 345)
obj.check_balance('checking')
obj.clothing(34, 'checking')
obj.check_balance('checking')
obj.transfer('checking', 'savings', 453)




