# Abstraction
'''
It involves hiding the complex implementation details of 
a system and exposing only the necessary and relevant parts 
to the user. This helps in reducing complexity and allows the 
user to interact with the system at a higher level.
'''
# Interface:
# Implmintation

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

# Usage
dog = Dog()
print(dog.make_sound())  # Output: Bark

cat = Cat()
print(cat.make_sound())  # Output: Meow
'''
Animal is an abstract class with an abstract method make_sound.
Dog and Cat are concrete subclasses that implement the make_sound method.

This way, the Animal class provides a common interface for all animals, 
while the specific implementation details are hidden in the subclasses.
'''
