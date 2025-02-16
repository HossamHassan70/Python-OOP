# Polymorphism: allows objects of different classes to be treated as objects 
# of a common superclass. It is the ability of different objects to respond 
# to the same method call in a way that is specific to their class. 
'''
Method Overriding
Method overriding occurs when a subclass provides a specific implementation 
for a method that is already defined in its superclass. The method in 
the subclass should have the same name, return type, and parameters as 
the method in the superclass. This allows the subclass to provide a specific 
behavior for the method.

****************
Method Overriding: Allows a subclass to provide a specific implementation 
for a method that is already defined in its superclass.
****************
'''
# Base class
class Animal:
    def speak(self):
        return "Some generic sound"

# Derived class
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Derived class
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Usage
animal = Animal()
dog = Dog()
cat = Cat()

print(animal.speak())  # Output: Some generic sound
print(dog.speak())     # Output: Woof!
print(cat.speak())     # Output: Meow!

'''
Method Overloading
Method overloading is a feature that allows a class to have more than one 
method with the same name, but different parameters. Python does not support 
method overloading by default. However, you can achieve similar behavior 
using default arguments or variable-length arguments.

******************
Method Overloading: Allows a class to have multiple methods with the 
same name but different parameters.
******************
Note:
Python does not support method overloading directly, but it can be achieved 
using default or variable-length arguments.
'''

# Example of Method Overloading in Python (Using Default Arguments)
class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c

# Usage
math_ops = MathOperations()
print(math_ops.add(1, 2))      # Output: 3
print(math_ops.add(1, 2, 3))   # Output: 6


