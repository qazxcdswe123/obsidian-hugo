- `this` 
It's a pointer
You can use keyword "`this`" to refer to _this_ instance inside a class definition.
One of the main usage of keyword `this` is to resolve ambiguity between the names of data member and function parameter. For example,
```cpp
class Circle {
private:
   double radius;                 // Member variable called "radius"
   ......
public:
   void setRadius(double radius) { // Function's argument also called "radius"
      this->radius = radius;
         // "this.radius" refers to this instance's member variable
         // "radius" resolved to the function's argument.
   }
   ......
}
```
Return the reference of the object (return this), 套娃