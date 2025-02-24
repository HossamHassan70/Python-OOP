// Define the Car class
class Car {
    constructor(name, color, price, speed) {
        this.name = name;
        this.color = color;
        this.price = price;
        this.speed = speed;
    }
}
// Create car objects
const car1 = new Car("Car1", "Red", 20000, 150);
const car2 = new Car("Car2", "Blue", 25000, 160);
const car3 = new Car("Car3", "White", 30000, 180);
const car4 = new Car("Car4", "Black", 35000, 200);
const car5 = new Car("Car5", "Silver", 40000, 220);
// Example: Access car details
console.log(`${car1.name}, ${car1.color}, ${car1.price}, ${car1.speed}`);