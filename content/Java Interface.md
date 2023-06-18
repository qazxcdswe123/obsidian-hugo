---
aliases: []
date created: Jun 7th, 2023
date modified: Jun 7th, 2023
---
An `interface` is a completely "**abstract class**" that is used to group related methods with empty bodies:

```java
interface Animal {
  public void animalSound(); // interface method (does not have a body)
  public void run(); // interface method (does not have a body)
}
```

To access the interface methods, the interface must be "implemented" (kinda like inherited) by another class with the `implements` keyword (instead of `extends`). The body of the interface method is provided by the "implement" class:

```java
// Pig "implements" the Animal interface
class Pig implements Animal {
  public void animalSound() {
    // The body of animalSound() is provided here
    System.out.println("The pig says: wee wee");
  }
  public void sleep() {
    // The body of sleep() is provided here
    System.out.println("Zzz");
  }
}

class Main {
  public static void main(String[] args) {
    Pig myPig = new Pig();  // Create a Pig object
    myPig.animalSound();
    myPig.sleep();
  }
}
```

## Interface vs Abstract Class
- An interface _cannot_ have state, whereas the abstract class can have state with instance variables.

## Abstract Class
An abstract class in Java is a class that cannot be instantiated, but can be subclassed. 
It can have both abstract and non-abstract methods. A normal (non-abstract) class cannot have abstract methods.

## `Comparable`
Used with `compareTo`
```java
public class Person implements Comparable<Person> {
    private int age;

    public Person(int age) {
        this.age = age;
    }

    public int getAge() {
        return age;
    }

    @Override
    public int compareTo(Person otherPerson) {
        return this.age - otherPerson.getAge();
    }
}
```