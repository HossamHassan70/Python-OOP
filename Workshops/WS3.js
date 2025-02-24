// Question 1
class Robot {
    constructor(name, color) {
    this.name = name;
    this.color = color;
    }
}

// Creating an object of the Robot class
let robot1 = new Robot("Zumba", "red");
// Printing the object's properties
console.log(robot1.name); // Output: Zumba
console.log(robot1.color); // Output: red

// Question 2
class Smartphone {
    // Constructor method to initialize attributes
    constructor(brand, model) {
        this.brand = brand;
        this.model = model;
    }
    // A method to display smartphone information
    displayInfo() {
        console.log(`Brand: ${this.brand}, Model: ${this.model}`);
    }
}
// Creating an object of the Smartphone class
const myPhone = new Smartphone("Apple", "iPhone 12");
// Calling a method of the object
myPhone.displayInfo(); 