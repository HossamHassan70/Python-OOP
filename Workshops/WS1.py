# Qustion 1
num1 = 5
num2 = 6
result = num1 + num2
print(result)
print("Total is " + str(result))
print("Total is " + format(result))
first_name = "Mohamed"
score = 90
print(f"Welcome {first_name} Your Score is : {score}")

# Question 2
n1 = input("Enter First number: ")
n2 = input("Enter Second number: ")
total = n1 + n2
print("Total is : " + str(total))
total = int(n1) + int(n2)
print("Total is : " + str(total))
total = float(n1) + float(n2)
print("Total is : " + str(total))

# Question 3
employee = "Ramy"
rate = 5
experience = 3
salary = 10000
if rate >= 5:
    print("Your Rate Is Excellent")
elif rate >= 3:
    print("Your Rate Is Good")
elif rate >= 2:
    print("Your Rate Is Bad")
else:
    print("Your Rate Is Very Bad")

# Question 4
num = int(input("Enter a number: "))
print("Multiplication Table for", num)
for i in range(1, 11):
    the_result = num * i
    print(f"{num} x {i} = {the_result}")

# Question 5
n = int(input("Enter the value of n: "))
sum_even = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even += i
print("The sum of even numbers from 1 to", n, "is", sum_even)

# Question 6
count_num = int(input("Enter a number: "))
print("Countdown:")
while count_num >= 0:
    print(count_num)
    count_num -= 1
print("Countdown complete!")

# Question 7
correct_password = "Python123"
password = ""
while password != correct_password:
    password = input("Enter password: ")
    if password != correct_password:
        print("Incorrect password, try again.")
print("Access Granted!")

# Question 8
numbers = [10, 20, 30, 40, 50]
sum_of_numbers = 0
for number in numbers:
    sum_of_numbers += number
print("Sum of numbers:", sum_of_numbers)

# Question 9
new_numbers = [23, 1, 56, 3, 98, 45]
maximum = new_numbers[0] # Initialize maximum with the first element
minimum = new_numbers[0] # Initialize minimum with the first element
for number in new_numbers:
    if number > maximum:
        maximum = number
    if number < minimum:
        minimum = number
print("Maximum:", maximum)
print("Minimum:", minimum)

# Question 10
student1 = {"name": "Mohamed", "age": 16, "grade": "A"}
key = "age"
if key in student1:
    print(f"The student's {key} is {student1[key]}.")
else:
    print(f"Key '{key}' not found in the dictionary.")
    
# Question 11
student2 = {"name": "Ahmed", "age": 15, "grade": "B"}
for key, value in student2.items():
    print(f"{key}: {value}")
    
# Question 12
cars = [
    {"name": "Car1", "color": "Red", "price": 20000, "speed": 150},
    {"name": "Car2", "color": "Blue", "price": 25000, "speed": 160},
    {"name": "Car3", "color": "White", "price": 30000, "speed": 180},
    {"name": "Car4", "color": "Black", "price": 35000, "speed": 200},
    {"name": "Car5", "color": "Silver", "price": 40000, "speed": 220},
]
# Example: Access car details
for car in cars:
    print(car["name"], car["color"], car["price"], car["speed"])