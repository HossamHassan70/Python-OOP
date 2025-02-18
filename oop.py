class Car: # class is a blueprint for creating objects
    # Constructor is a special method that is called when an object is created
    no_of_obj = 0 # Class attribute
    
    def __init__(self,brand,speed,color,price):
        # self is a reference to the current instance (object) of the class
        self.__name = brand  # Instance attribute 
        self.speed = speed
        self.color = color
        self.price = price
        Car.no_of_obj += 1 # Keep track number of created objects 
    def get_brand_and_speed(self): # Instance Method
        print(f"My brand is {self.name} and my speed is {self.speed}")
    
    @classmethod
    def get_no_of_objects(cls): # Class Method
        return f"Total number of Car objects created: {cls.no_of_obj}"


car1 = Car('BMW',280,'Red',5000000)

car2 = Car('Fiat',160,'Blue',80000)
car3 = Car('Fiat',160,'Blue',80000)
print(car2)
print(car3)

print(car1.__name)
car1.name = 'Ferarry'
print(car1.name)
print(car2.name,car2.price)
print(car1.get_brand_and_speed())

# Calling the class method
print(Car.get_no_of_objects())  # Output: Total number of Car objects created: 2

def summ(anything,y):
    return anything + y

print(summ(5,7))
