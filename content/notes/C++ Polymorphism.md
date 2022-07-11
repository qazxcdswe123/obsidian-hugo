---
title: C++ Polymorphism
---
[[C++ Override and Final]]
# Virtual
## Pure Virtual
[SO](https://stackoverflow.com/questions/1306778/virtual-pure-virtual-explained)
[GFG](https://www.geeksforgeeks.org/pure-virtual-functions-and-abstract-classes/)
A pure virtual function is implemented by classes which are derived from a Abstract class.
## Virtual Function
```cpp
/* Test Substituting a subclass instance to a superclass reference.
   (TestSubstitution.cpp) */
#include <iostream>
#include "MovablePoint.h"   // included "Point.h"
using namespace std;
 
int main() {
   // Substitute a subclass instance to a superclass reference
 
   // Using Object Pointer
   Point * ptrP1 = new MovablePoint(11, 12, 13, 14);   // upcast
   ptrP1->print(); // MovablePoint @ (11,12) Speed=(13,14)
                   //   - Run subclass version!!
   cout << endl;
   delete ptrP1;
 
   // Using Object Reference
   MovablePoint mp2(21, 22, 23, 24);
   Point & p2 = mp2;  // upcast
   p2.print();     // MovablePoint @ (21,22) Speed=(23,24)
                   //   - Run subclass version!!
   cout << endl;
 
   // Using object with explicit constructor
   Point p3 = MovablePoint(31, 32, 33, 34);  // upcast
   p3.print();     // Point @ (31,32) - Run superclass version!!
   cout << endl;
}
```
Take note that virtual functions work on **object pointers (and references)**, but not on regular objects.
When you refer to a derived class object using a pointer or a reference to the base class, you can call a virtual function for that object and execute the derived class’s version of the function.

For non-virtual function, the compiler selects the function that will be invoked at compiled-time (known as static binding). 
For virtual functions, the selection is delayed until the runtime. The function selected depends on the actual type that invokes the function (known as dynamic binding or late binding).

## Virtual Class
[Src](https://www.geeksforgeeks.org/virtual-base-class-in-c/)
![](https://s2.loli.net/2022/05/24/mHTkifFn6BwpSI5.png)

Using Polymorphism:
1.  Create instances of concrete subclass.
2.  Declare superclass (possibly abstract) pointers (or references).
3.  Aim the superclass pointers to the subclass instances.
4.  Invoke virtual function, with implementation provided by subclass.