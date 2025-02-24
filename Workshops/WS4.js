// Qustion 1
class Student {
    // Class attribute
    static get school_name() {
        return "WE-School";
    }
    // Constructor for instance attributes
    constructor(name, grade) {
        this.name = name;
        this.grade = grade;
    }
    // Method to display student details
    displayInfo() {
        console.log(`Student Name: ${this.name}`);
        console.log(`Grade: ${this.grade}`);
        console.log(`School: ${Student.school_name}`);
    }
}
// Creating objects of the Student class
let student1 = new Student("Ahmed", "2nd");
let student2 = new Student("Ali", "3rd");
// Calling methods on those objects
student1.displayInfo();
student2.displayInfo();

// Qustion 2
class Book {
    constructor(title, author) {
        this.title = title;
        this.author = author;
        this.isBorrowed = false; // Initially, the book is not borrowed
    }
    /* Method to borrow the book */
    borrowBook() {
        if (!this.isBorrowed) {
            this.isBorrowed = true;
            console.log(`${this.title} by ${this.author} has been borrowed.`);
        } else {
            console.log(`${this.title} is currently not available.`);
        }
    }
    /** Method to return the book */
    returnBook() {
        if (this.isBorrowed) {
            this.isBorrowed = false;
            console.log(`${this.title} has been returned.`);
        } else {
            console.log(`${this.title} was not borrowed.`);
        }
    }
}
// Creating a Book object
const book1 = new Book("Python Programming", "Ahmed Ali");
// Borrowing and returning the book
book1.borrowBook();
book1.returnBook();