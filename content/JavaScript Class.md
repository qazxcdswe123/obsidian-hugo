---
aliases: []
date created: Apr 20th, 2022
date modified: Dec 17th, 2022
---
Classes are in fact "special [functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)", and just as you can define [function expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function) and [function declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function), the class syntax has two components: [class expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/class) and [class declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class).

## [Class declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#class_declarations "Permalink to Class declarations")
```javascript
class Rectangle {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
}

const R1 = new Rectangle();
```

```javascript
// unnamed
let Rectangle = class {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
};
console.log(Rectangle.name);
// output: "Rectangle"

// named
let Rectangle = class Rectangle2 {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
};
console.log(Rectangle.name);
// output: "Rectangle2"
```

## Static Properties
[_Static properties_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static) are a group of class features that are defined on the class itself, rather than on individual instances of the class. These features include:
- Static methods
- Static fields
- Static getters and setters

## Super
In JavaScript, `super` refers to the parent class constructor. (In our example, it points to the `React.Component` implementation.)  
Importantly, you can’t use `this` in a constructor until _after_ you’ve called the parent constructor. JavaScript won’t let you:


[[JavaScript Hoisting]]
