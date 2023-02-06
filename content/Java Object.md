---
aliases: []
tags: []
date created: Feb 5th, 2023
date modified: Feb 5th, 2023
---
To construct an object, you use the new operator, followed by a call to the constructor. 
- `new Greeter("World")`  
The `new` operator returns the constructed object, or, more precisely, **a reference to that object**—we will discuss that distinction in detail in the section on object references.

## Static

### Why is `main` Static in Java
The `main` method is `static`, which means that it doesn’t operate on an object. After all, when the application first starts, there aren’t any objects yet. It is the job of the main method to construct the objects that are needed to run the program.