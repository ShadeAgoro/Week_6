from account import Account
# from the module (file) import the Class

# we created a class for Harry Potter Hogwarts Houses to understand classes better, then created multiple instances
# So here the class is called HogwartsHouse, 3 attributes: name, animal, and founder.
# __init__ a special method is called when a new instance of the class is created.

class HogwartsHouse:
    def __init__(self, name, animal, founder):
        self.name = name
        self.animal = animal
        self.founder = founder

# __str__ a special method that shows a string representation of the instance.
    def __str__(self):
        return f"{self.name}, Animal: {self.animal}, Founder: {self.founder}"

gryffindor = HogwartsHouse("Gryffindor", "Lion", "Godric Gryffindor")
slytherin = HogwartsHouse("Slytherin", "Serpent", "Salazar Slytherin")
hufflepuff = HogwartsHouse("Hufflepuff", "Badger", "Helga Hufflepuff")
ravenclaw = HogwartsHouse("Ravenclaw", "Eagle", "Rowena Ravenclaw")

# prints string of instance
print(gryffindor)
print(slytherin.animal)
print(hufflepuff.founder)

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
