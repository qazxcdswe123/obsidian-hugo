Classes are in fact "special [functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)", and just as you can define [function expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function) and [function declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function), the class syntax has two components: [class expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/class) and [class declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class).
# [Class declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#class_declarations "Permalink to Class declarations")
```javascript
class Rectangle {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
}
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
## Hoisting
An important difference between **function declarations** and **class declarations** is that while functions can be called in code that appears before they are defined, classes must be defined before they can be constructed. Code like the following will throw a [`ReferenceError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError):
