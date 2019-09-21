
# dog.py
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    # Methods are defined as their own named
    def bark(self):
        print("Woof!")
        
# my-dogs.py
import dog #specify what i need
        
my_dog = Dog("Tucker", "SuperDog")
my_dog.bark()

my_other_dog = dog.Dog("Anna", "SuperDog")
print(my_other_dog.name)
