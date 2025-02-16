# Inheritance:-
'''
It allows a class to inherit attributes and methods from another class
The class that inherits is called the subclass or derived class (child), and 
the class being inherited from is called the superclass or base class (parent).

Inheritance promotes code reusability and establishes a relationship 
between classes.
DRY concept 
Don't Repeat Yourself

'''
# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Derived class
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Derived class
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Usage
dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy says Woof!

cat = Cat("Whiskers")
print(cat.speak())  # Output: Whiskers says Meow!


# Types of Inheritance
# Single Inheritance: A subclass inherits from one superclass.

class A:
    pass

class B(A):
    pass
# Multiple Inheritance: A subclass inherits from more than one superclass.

class A:
    pass

class B:
    pass

class C(A, B):
    pass
# Multilevel Inheritance: A subclass inherits from another subclass.

class A:
    pass

class B(A):
    pass

class C(B):
    pass
# Hierarchical Inheritance: Multiple subclasses inherit from one superclass.

class A:
    pass

class B(A):
    pass

class C(A):
    pass
# Hybrid Inheritance: A combination of two or more types of inheritance.
# Inheritance helps in creating a well-structured and organized 
# codebase by promoting code reuse and establishing relationships 
# between classes.