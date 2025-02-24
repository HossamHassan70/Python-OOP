# Question 1
def usd_to_eur(amount, exchange_rate=0.85):
    return amount * exchange_rate
print(usd_to_eur(100, 0.85))

# Qustion 2
def calculate_total(price, tax_rate):
 return price + (price * tax_rate)
print(calculate_total(100, 0.07)) # Output: 107.0
#using keyword arguments
print(calculate_total(price=200, tax_rate= 0.05)) # Output: 210.0
print(calculate_total(tax_rate= 0.10, price=300)) # Output: 330.0

# Question 3
def max_num(n1 , n2 , n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    if n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3
print(max_num(45 , 19 , 14))

# Question 4
class Car:
    def __init__(self, name, color, price, speed):
        self.name = name
        self.color = color
        self.price = price
        self.speed = speed

# Create car objects
car1 = Car("Car1", "Red", 20000, 150)
car2 = Car("Car2", "Blue", 25000, 160)
car3 = Car("Car3", "White", 30000, 180)
car4 = Car("Car4", "Black", 35000, 200)
car5 = Car("Car5", "Silver", 40000, 220)

# Example: Access car details
print(car1.name, car1.color, car1.price, car1.speed)