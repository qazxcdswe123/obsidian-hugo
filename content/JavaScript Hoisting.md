[Hoisting - MDN Web Docs Glossary: Definitions of Web-related terms | MDN](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting)

JavaScript **Hoisting** refers to the process whereby the interpreter appears to move the _declaration_ of functions, variables or classes to the top of their [[Variable Scope]], prior to execution of the code.

An important difference between **function declarations** and **class declarations** is that while functions can be called in code that appears before they are defined, classes must be defined before they can be constructed. Code like the following will throw a [`ReferenceError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError):

## Function hoisting
One of the advantages of hoisting is that it lets you use a function before you declare it in your code.

```js
catName("Tiger");

function catName(name) {
  console.log(`My cat's name is ${name}`);
}
/*
The result of the code above is: "My cat's name is Tiger"
*/
```

## Exceptions
[Function expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function) and [class expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#class_expressions) are not hoisted.

```js
notHoisted(); // TypeError: notHoisted is not a function

let notHoisted = function () {
  console.log('bar');
};

const p = new Rectangle(); // ReferenceError
class Rectangle {}
```
