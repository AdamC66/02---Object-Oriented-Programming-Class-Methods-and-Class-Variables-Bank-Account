
# @classmethod def total_population(cls): # stuff

# Part 1: Bank Account Create a class called BankAccount. 
# Add a class variable called interest_rate that is a float representing the interest rate for all the accounts in the bank. 
# This is a class variable because it is the same value for all accounts. 
# Add another class variable called accounts that starts as an empty list. 
# This will eventually store the collection of all bank accounts in the bank. 
# Add an init() instance method that sets the bank account's balance to zero. 
# Balance is stored in an instance variable because the value needs to be different from account to account. 
# Add an instance method called deposit that accepts a number as an argument and adds that amount to the account's balance. 
# This needs to be an instance method because it pertains to a single, specific account. 
# Add an instance method called withdraw that accepts a number as an argument and subtracts that amount from the account's balance. 

# Add a class method called create that makes a new instance using BankAccount() and adds the new object to the accounts 
# class variable so that we can find it again in the future. This method should return the new account object. 
# This needs to be a class method because at the time we run it there is no single, specific account object that we are working on. 

# Add a class method called total_funds that returns the sum of all balances across all accounts in the accounts class variable. 
# This needs to be a class method because it does not pertain to any single, specific account. 
# 
# Add a class method called interest_time 
# that iterates through all accounts and increases their balances according to the class interest_rate. This needs to be a class method 
# because it operates on all bank accounts, not a single, specific account.

# Example output my_account = BankAccount.create() your_account = BankAccount.create() print(my_account.balance) # 0 
# print(BankAccount.total_funds()) # 0 my_account.deposit(200) your_account.deposit(1000) print(my_account.balance) # 200 
# print(your_account.balance) # 1000 print(BankAccount.total_funds()) # 1200 BankAccount.interest_time() 
# print(my_account.balance) # 202.0 print(your_account.balance) # 1010.0 print(BankAccount.total_funds()) # 1212.0 
# my_account.withdraw(50) print(my_account.balance) # 152.0 print(BankAccount.total_funds()) # 1162.0

class BankAccount:
    interest_rate = float(0.01)
    accounts = []
    def __init__(self):
        self.balance = 0

    def deposit(self,amount):
        self.balance += amount
        return self.balance
    def withdraw(self,amount):
        self.balance -= amount
        return self.balance
    @classmethod
    def create(cls):
        new_account = BankAccount()
        cls.accounts.append(new_account)
        return new_account
    @classmethod
    def interest_time(cls):
        for account in cls.accounts:
            account.balance *= (1+cls.interest_rate)
    @classmethod
    def total_funds(cls):
        total = 0
        for account in cls.accounts:
            total+= account.balance
        return total

my_account = BankAccount.create()
your_account = BankAccount.create()
print(my_account.balance) # 0
print(BankAccount.total_funds()) # 0

my_account.deposit(200)
your_account.deposit(1000)
print(my_account.balance) # 200
print(your_account.balance) # 1000
print(BankAccount.total_funds()) # 1200

BankAccount.interest_time()
print(my_account.balance) # 202.0
print(your_account.balance) # 1010.0
print(BankAccount.total_funds()) # 1212.0

my_account.withdraw(50)
print(my_account.balance) # 152.0
print(BankAccount.total_funds()) # 1162.0