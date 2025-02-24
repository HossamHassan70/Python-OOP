# Question: 1
class PiggyBank:
    def __init__(self):
        self.__balance = 0 # Private attribute
    def add_money(self, amount):
        if amount > 0:
            self.__balance += amount
    def check_balance(self):
        return self.__balance

my_bank = PiggyBank()
my_bank.add_money(100)
print(my_bank.check_balance()) # Output: 100

# Question: 2
class Car:
    def __init__(self, make):
        self.__make = make # Private attribute
    def get_make(self):
        return self.__make
    def set_make(self, new_make):
        self.__make = new_make

car = Car("Toyota")
print(car.get_make()) # Output: Toyota
car.set_make("Honda")
print(car.get_make()) # Output: Honda

# Question: 3
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def drive(self):
        print("The vehicle is moving.")

class My_Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    def honk(self):
        print("Beep! Beep!")

my_car = My_Car("Toyota", "Corolla")
my_car.drive() # Output: The vehicle is moving.
my_car.honk() # Output: Beep! Beep!

# Question: 4
class Animal:
    def sound(self):
        print("Some generic animal sound")
class Dog(Animal):
    def sound(self):
        print("Woof!")

dog = Dog()
dog.sound() # Output: Woof!

# Question: 5
class My_Animal:
    def sound(self):
        pass
class My_Dog(My_Animal):
    def sound(self):
        return "Woof!"
class My_Cat(My_Animal):
    def sound(self):
        return "Meow!"

animals = [My_Dog(), My_Cat()]
for animal in animals:
    print(animal.sound())
# Output:
# Woof!
# Meow!

# Question: 6
class New_Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        pass # We don't know what sound every animal makes
class New_Dog(New_Animal):
    def make_sound(self):
        print("Woof!")

class New_Cat(New_Animal):
    def make_sound(self):
        print("Meow!")

my_dog = New_Dog("Buddy")
my_cat = New_Cat("Whiskers")
my_dog.make_sound() # Output: Woof!
my_cat.make_sound() # Output: Meow!