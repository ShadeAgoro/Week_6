from account import Account
# from the module (file) import the Class




# create some object instances
# instantiation

lisa_account = Account(500) # we are calling a special method called the constructor
bart_account = Account(100)

# object dot field
# object dot method()

#lisa_account.
print(lisa_account)
print(bart_account)

lisa_account.deposit(100)
bart_account.deposit(20)
print(lisa_account.get_balance())
print(bart_account.get_balance())

lisa_account.withdraw(-25000)
#bart_account.withdraw(10)
print(lisa_account.get_balance())
print(bart_account.get_balance())

bart_account.__balance = 1000000
print(bart_account.get_balance())

bart_account.set_firstname('Bart')
print(bart_account.get_firstname())

lisa_account.set_firstname('Lisa')
print(lisa_account.get_firstname())
