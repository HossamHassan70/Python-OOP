class Person:
    def __init__(self, name, age):
        self.__name = name  # private attribute
        self.__age = age    # private attribute

    # Getter method for name
    def get_name(self):
        return self.__name

    # Setter method for name
    def set_name(self, name):
        if isinstance(name, str) and name: # name should be a non-empty string value
            self.__name = name
        else:
            raise ValueError("Invalid name")

    # Getter method for age
    def get_age(self):
        return self.__age

    # Setter method for age
    def set_age(self, age):
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            raise ValueError("Invalid age")

# Usage
person = Person("John", 30)
print(person.get_name())  # Output: John
print(person.get_age())   # Output: 30
person.set_age(31)
print(person.get_age())   # Output: 31

# Protected Members
'''
Access: Intended to be accessed within the class and its 
subclasses. It is a convention indicating that the member 
should not be accessed from outside the class, but it is 
not strictly enforced.
'''
class Base:
    def __init__(self):
        self._protected_member = "I am protected"

class Derived(Base):
    def __init__(self):
        super().__init__()
        print(self._protected_member)  # Accessible in subclass

base = Base()
print(base._protected_member)  # Accessible, but not recommended

# Private Members
'''
Access: Intended to be accessed only within the class. 
Python performs name mangling to make it harder to access 
private members from outside the class.
'''
class Base:
    def __init__(self):
        self.__private_member = "I am private"

    def get_private_member(self):
        return self.__private_member

base = Base()
print(base.get_private_member())  # Accessible via getter method
# print(base.__private_member)    # Raises AttributeError

