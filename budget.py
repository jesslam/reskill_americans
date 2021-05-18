class Category:

    def __init__(self, category, amount):
        # initialize the expense type and amount of expense 
        self.category = category
        self.amount = amount

    def display_balance(self):
        return ('Your {} balance is {}.'.format(self.category, self.amount))

    def check_balance(self, amount):
        # check the current account balance
        if self.amount >= amount:
            return True
        else:
            return False
    
    def deposit(self, amount):
        # add a dollar amount to the existing account balance
        self.amount += amount
        return ('You have deposited {} into your {} budget.  The balance is now {}.'.format(amount, self.category, self.amount))

    def withdraw(self, amount):
        # subtract an amount from the current balance
        self.amount -= amount
        return ('You withdrawn {} from your {} budget.  The balance is {}.'.format(amount, self.category, self.amount))

    def transfer(self, amount, category):
        # transfer an amount from one account to another account
        if self.check_balance(amount) == True:
            self.amount -= amount
            category.amount += amount
            return('Transfer successful.  Your {} balance is {} and your {} balance is {}'.format(self.category, self.amount, category.category, category.amount))
        else:
            return('Insufficient funds to perform this transaction.')

food_budget = Category('Food', 300)
car_budget = Category('Car', 1000)
print(food_budget.withdraw(250))
print(food_budget.deposit(100))
print(food_budget.display_balance())
print(food_budget.transfer(150, car_budget))
