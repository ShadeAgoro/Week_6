# we created a class for Harry Potter Hogwarts Houses to understand classes better, then created multiple instances
# So here the class is called HogwartsHouse, 3 attributes: name, animal, and founder.
# __init__ a special method is called when a new instance of the class is created.

# protected class by double underscore

class HogwartsHouse:
    def __init__(self, name, animal, founder):
        self.__name = name
        self.__animal = animal
        self.__founder = founder

    def get_animal(self):
        return self.__animal

    def get_name(self):
        return self.__name

    def get_founder(self):
        return self.__founder

# __str__ a special method that shows a string representation of the instance.
    def __str__(self):
        return f"{self.get_name()}, Animal: {self.get_animal()}, Founder: {self.get_founder()}"
