---
aliases: []
date created: Feb 5th, 2023
date modified: Apr 13th, 2023
---

# Java Class
A variable of a class type holds a reference to an object of that class.

## Interface
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

## Nested Class
- Non-static nested classes (inner classes) are members of their enclosing class and have access to other members of the enclosing class, while static nested classes are not members of their enclosing class and do not have access to the instance variables and methods of the enclosing class.
- Non-static nested classes can access non-static members of the enclosing class directly, while nested static classes cannot and need to create an instance of the enclosing class to access them

___

# Java Object

## Overview
To construct an object, you use the `new` operator, followed by a call to the constructor. 

```java
new Greeter("World")
```

The `new` operator returns the constructed object, or, more precisely, **a reference to that object**—we will discuss that distinction in detail in the section on object references.

## Class Vs Object
**_Class is a user-defined datatype that has its own data members and member functions whereas an object is an instance of class by which we can access the data members and member functions of the class._**

## Static
Also called a class variable (in contract to a instance variable)

### Why is `main` `static` in Java
The `main` method is `static`, which means that it doesn’t operate on an object. After all, when the application first starts, there aren’t any objects yet. It is the job of the main method to construct the objects that are needed to run the program.

- But why is `main` `void`  
A program terminates all its activity and _exits_ when one of two things happens:
- All the threads that are not daemon threads terminate.
- Some [[thread]] invokes the `exit` method of class `Runtime` or class `System` and the exit operation is not forbidden by the security manager.  
In other words, the program may exit before or after the `main` method finishes; a return value from `main` would therefore be meaningless. If you want the program to return a status code, call one of the following methods (note that all three methods never return normally):

## `equals()` And `hashCode()` Contracts
- If two objects are equal according to the `equals()` method, then their hash codes must be equal as well.
- If two objects have the same hash code, they may or may not be equal according to the `equals()` method.

## Boxing and Unboxing
Boxing in Java refers to the process of converting a primitive data type into its corresponding wrapper class (e.g., `int` to `Integer`, `double` to `Double`, etc.). Unboxing is the reverse process, converting a wrapper class object back into its corresponding primitive data type (e.g., `Integer` to `int`, `Double` to `double`, etc.)

```java
// boxing
List<Integer> li = new ArrayList<>();
for (int i = 1; i < 50; i += 2)
    li.add(i);

// unboxing
public static int sumEven(List<Integer> li) {
    int sum = 0;
    for (Integer i: li)
        if (i % 2 == 0)
            sum += i;
        return sum;
}
```