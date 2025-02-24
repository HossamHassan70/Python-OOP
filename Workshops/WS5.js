// Qustion 1
class PiggyBank {
    constructor() {
        this._balance = 0; // Private attribute using convention
    }
    addMoney(amount) {
        if (amount > 0) {
            this._balance += amount;
        }
    }
    checkBalance() {
        return this._balance;
    }
}
const myBank = new PiggyBank();
myBank.addMoney(100);
console.log(myBank.checkBalance()); // Output: 100

// Qustion 2
class Car {
    constructor(make) {
        this._make = make; // Private attribute using convention
    }
    getMake() {
        return this._make;
    }
    setMake(newMake) {
        this._make = newMake;
    }
}

const car = new Car("Toyota");
console.log(car.getMake()); // Output: Toyota
car.setMake("Honda");
console.log(car.getMake()); // Output: Honda

// Qustion 3
class Vehicle {
    constructor(brand) {
        this.brand = brand;
    }
    drive() {
        console.log("The vehicle is moving.");
    }
}
class MyCar extends Vehicle {
    constructor(brand, model) {
        super(brand);
        this.model = model;
    }
    honk() {
        console.log("Beep! Beep!");
    }
}
const myCar = new MyCar("Toyota", "Corolla");
myCar.drive(); // Output: The vehicle is moving.
myCar.honk(); // Output: Beep! Beep!

// Qustion 4
class Animal {
    sound() {
        console.log("Some generic animal sound");
    }
}
class Dog extends Animal {
    sound() {
        console.log("Woof!");
    }
}
const dog = new Dog();
dog.sound(); // Output: Woof!

// Qustion 5
class NewAnimal {
    sound() {
        // This method will be overridden in subclasses
    }
}
class TheDog extends NewAnimal {
    sound() {
        return "Woof!";
    }
}
class TheCat extends NewAnimal {
    sound() {
        return "Meow!";
    }
}
const animals = [new TheDog(), new TheCat()];
for (const animal of animals) {
    console.log(animal.sound());
}

// Qustion 6
class TheNewAnimal {
    constructor(name) {
        this.name = name;
    }
    makeSound() {
        throw new Error("This method must be overridden by a subclass");
    }
}
class TheNewDog extends TheNewAnimal {
    makeSound() {
        console.log("Woof!");
    }
}
class TheNewCat extends TheNewAnimal {
    makeSound() {
        console.log("Meow!");
    }
}
const myDog = new TheNewDog("Buddy");
const myCat = new TheNewCat("Whiskers");
myDog.makeSound(); // Output: Woof!
myCat.makeSound(); // Output: Meow!