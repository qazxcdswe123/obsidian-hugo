---
aliases: []
date created: Feb 5th, 2023
date modified: Apr 13th, 2023
---

# Java Class
A variable of a class type holds a reference to an object of that class.

- [[Java Interface]]

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

### What is `main` `static` in Java
The `main` method is `static`, which means that it doesn’t operate on an object.

- But why is `main` `void`  
A program terminates all its activity and _exits_ when one of two things happens:
- All the [[Thread|threads]] that are not daemon threads terminate.
- Some [[thread]] invokes the `exit` method of class `Runtime` or class `System` and the exit operation is not forbidden by the security manager.  
In other words, the program may exit before or after the `main` method finishes; a return value from `main` would therefore be meaningless. If you want the program to return a status code, call one of the following methods (note that all three methods never return normally):
