

#class - classification of a type
#a class is a blueprint
#DATA + BEHAVIOUR
#fields + methods

#objects are the instances

#constructors - special methods that ensure our objects are ready to be used


class Account:

    def __init__(self, opening_amount):
        self.__balance = opening_amount

    def deposit(self, amount):
        self.__balance += amount


#    def withdraw(self, amount):
#        self.balance -= amount

#    def withdraw(self, amount):
#        if self.balance >= amount > 0:



    def withdraw(self, amount):
        if amount > 0 and self.balance - amount >= 0:
            self.__balance -= amount

    # getter
    def get_balance(self):
        return self.__balance

    # getter - READ
    def get_firstname(self):
        return self._firstname

    # setter = WRITE
    def set_firstname(self, firstname):
        self._firstname = firstname

#encapsulation - hiding stuff
# this is good because...
