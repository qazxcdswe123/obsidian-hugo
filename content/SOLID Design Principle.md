---
aliases: []
date created: Jul 28th, 2023
date modified: Jul 28th, 2023
---

## Single Responsibility Principle (SRP)
The single responsibility principle states that a class, module, or function should have only one reason to change, meaning it should do one thing.

```js
class Animal {
  constructor(name) {
    this.name = name;
  }

  nomenclature() {
    console.log(`The name of the animal is ${this.name}`);
  }
}

let animal1 = new Animal('Elephant');
animal1.nomenclature(); // The name of the animal is Elephant

// Sound class
class Sound {
  constructor(name, soundMade) {
    this.name = name;
    this.soundMade = soundMade;
  }

  sound() {
    console.log(`${this.name} ${this.soundMade}s`);
  }
}

let animalSound1 = new Sound('Elephant', 'trumpet');
animalSound1.sound(); //Elephant trumpets

// Feeding class
class Feeding {
  constructor(name, feedingType) {
    this.name = name;
    this.feedingType = feedingType;
  }

  feeding() {
    console.log(`${this.name} is a/an ${this.feedingType}`);
  }
}

let animalFeeding1 = new Feeding('Elephant', 'herbivore');
animalFeeding1.feeding(); // Elephant is a/an herbivore

```

## Open Closed Principle (OCP)
Classes, modules, and functions should be open for extension but closed for modification.

## Liskov Substitution Principle (LSP)