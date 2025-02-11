class Car: # class is a blueprint for creating objects
    # Constructor is a special method that is called when an object is created
    def __init__(self,brand,speed,color,price):
        # self is a reference to the current instance (object) of the class
        self.name = brand 
        self.speed = speed
        self.color = color
        self.price = price


car1 = Car('BMW',280,'Red',5000000)
car2 = Car('Fiat',160,'Blue',80000)

print(car1.name,car1.price)
print(car2.name,car2.price)

def summ(anything,y):
    return anything + y

print(summ(5,7))
