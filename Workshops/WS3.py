# Question: 1
class Robot:
    def __init__(self, name, color):
        self.name = name
        self.color = color

# Create an object of the Robot class
robot1 = Robot("Zumba", "red")
print(robot1.name) # Output: Zumba
print(robot1.color) # Output: red

# Question: 2
class Smartphone:
    # Constructor method to initialize attributes
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    # A method to display smartphone information
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

# Creating an object of the Smartphone class
my_phone = Smartphone("Apple", "iPhone 12")
# Calling a method of the object
my_phone.display_info()
