class Car:
    def __init__(self, brand, color, speed):
        self.brand = brand
        self.color = color
        self.speed = speed

car1 = Car('BMW', 'Red', 300)
print(car1.brand)