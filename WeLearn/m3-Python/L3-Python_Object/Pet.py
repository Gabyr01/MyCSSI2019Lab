
'''
pet = {
  "name": "Doggo",
  "animal": "dog",
  "species": "labrador",
  "age": 5
}
'''

class Pet(object):
    def __init__(self, name, age, animal):
        self.name = name
        self.age = age
        self.animal = animal
        self.is_hungry = False
        self.mood = "happy"
        self.location = "room1"


    def eat(self):
        print("> %s is eating..." % self.name)
        if self.is_hungry:
            self.is_hungry = False
        else:
            print("> %s may have eaten too much." % self.name)
            self.mood = "lethargic"

    def move(self):
        print("> %s is moving..." % self.name)
        if self.location == "room1":
            self.location = "room2"
            print("> %s is in %s" % (self.name,self.location))
        else:
            self.location = "room1"
            print("> %s is in %s" % (self.name,self.location))

my_pet = Pet("Fido", 3, "dog")
#my_pet.is_hungry = True;
print("Is my pet hungry? %s " % my_pet.is_hungry)
print("My pet is feeling %s " % my_pet.mood)
my_pet.eat() #my_pet is the current object
print("How about now? %s" % my_pet.is_hungry)
print("My pet is feeling %s " % my_pet.mood)

my_pet.move()

'''
#obejevt.property_name
my_pet = Pet("Fido", 3)
print("My pet %s is %s years old" % (my_pet.name, my_pet.age))

pet2 = Pet("Lucy", 4)
print("My pet %s is %s years old" % (pet2.name, pet2.age))

pet3 = Pet("Angel", 5)
print("My pet %s is %s years old" % (pet3.name, pet3.age))
'''
