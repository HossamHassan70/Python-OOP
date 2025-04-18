class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
    def borrow(self):
        if self.is_available:
            self.is_available = False
            return True
        return False
    def return_book(self):
        self.is_available = True


class Patron:
    def __init__(self,name):
        self.name = name
        self.borrowed_books = []
        
    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            return f'{self.name} Borrowed "{book.title}"'
        return f'{book.title} is not available'

    def return_book(self, book):  
        if book in self.borrowed_books:  
            book.return_book()  
            self.borrowed_books.remove(book)  
            return f"{self.name} returned '{book.title}'."  
        return f"{self.name} does not have '{book.title}'." 






book1 = Book('Mission Impossible', 'Taha Hussin')
book2 = Book('Atomic Habit', 'Jems Clear')
patron1 = Patron('Abduelrahman')
patron2 = Patron('Ehab')

print(patron1.borrow_book(book1))  # Output: Abduelrahman Borrowed Mission Impossible
print(patron2.borrow_book(book1)) # Output: Mission Impossible is not available
print(patron1.return_book(book1)) # Output: Abduelrahman returned 'Mission Impossible'
print(patron2.borrow_book(book1)) # Output: Ehab Borrowed "Mission Impossible"
print(patron2.borrow_book(book2)) # Output: Ehab Borrowed "Atomic Habit"
print(patron1.borrow_book(book2)) # Output: Atomic Habit is not available
print(patron1.return_book(book2)) # Output: Abduelrahman does not have 'Atomic Habit'
