from hogwartshouse import HogwartsHouse

gryffindor = HogwartsHouse("Gryffindor", "Lion", "Godric Gryffindor")
slytherin = HogwartsHouse("Slytherin", "Serpent", "Salazar Slytherin")
hufflepuff = HogwartsHouse("Hufflepuff", "Badger", "Helga Hufflepuff")
ravenclaw = HogwartsHouse("Ravenclaw", "Eagle", "Rowena Ravenclaw")

# because the class is encapsulated, you cannot change as protected
gryffindor.animal = "hamster"

# prints string of instance
print(gryffindor)
print(hufflepuff.get_animal())
print(slytherin.get_animal())
print(hufflepuff.get_founder())
