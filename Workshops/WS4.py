# Qustion 1
class Student:
    # Class attribute
    school_name = "WE-School"
    # Instance attributes
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    # Method to display student details
    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Grade: {self.grade}")
        print(f"School: {Student.school_name}")
        
# Creating objects of the Student class
student1 = Student("Ahmed", "2nd")
student2 = Student("Ali", "3rd")

# Calling methods on those objects
student1.display_info()
student2.display_info()

# Question 2
class Book:
    """Constructor with instance attributes"""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False # Initially, the book is not borrowed
    """Method to borrow the book"""
    def borrow_book(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"{self.title} by {self.author} has been borrowed.")
        else:
            print(f"{self.title} is currently not available.")
    """Method to return the book"""
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} was not borrowed.")

# Creating a Book object
book1 = Book("Python Programming", "Ahmed Ali")
# Borrowing and returning the book
book1.borrow_book()
book1.return_book()