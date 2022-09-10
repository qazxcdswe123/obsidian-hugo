---
aliases: []
tags: [] 
date created: May 5th, 2022
date modified: Sep 9th, 2022
---
[[JavaScript Template Literal]]
# Data
Let's start off by looking at the building blocks of any language: the types. JavaScript programs manipulate values, and those values all belong to a type. JavaScript's types are:
- [Number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#number_type)
	- 64 bit double
- [BigInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#bigint_type)
- [String](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#string_type)
	- [[JavaScript String]]
- [Boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#boolean_type)
	- `Boolean()`
- [Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#symbol_type) (new in ES2015)
	- [[JavaScript Symbol]]
- [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#objects)
    - [`Function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
    - [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
    - [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)
    - [`RegExp`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
- [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#null_type)
- [undefined](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#undefined_type)

## Variable
New variables in JavaScript are declared using one of three keywords: [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let), [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const), or [`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var).  

### Let
**`let`** allows you to declare block-level variables. The declared variable is available from the _block_ it is enclosed in.

```JavaScript 
let a;
let name = 'Simon';
```

The following is an example of scope with a variable declared with **`let`**:

```JavaScript 
// myLetVariable is *not* visible out here

for (let myLetVariable = 0; myLetVariable < 5; myLetVariable++) {
  // myLetVariable is only visible in here
}

// myLetVariable is *not* visible out here
```

### Const
**`const`** allows you to declare variables whose values are never intended to change. The variable is available from the _block_ it is declared in.

```JavaScript 
const Pi = 3.14; // variable Pi is set
Pi = 1; // will throw an error because you cannot change a constant variable.
```

### Var
**`var`** does not have the restrictions that the other two keywords have. This is because it was traditionally the only way to declare a variable in JavaScript. A variable declared with the **`var`** keyword is available from the _function_ it is declared in.

```JavaScript 
var a;
var name = 'Simon';
```

An example of scope with a variable declared with **`var`:**

```JavaScript 
// myVarVariable *is* visible out here

for (var myVarVariable = 0; myVarVariable < 5; myVarVariable++) {
  // myVarVariable is visible to the whole function
}

// myVarVariable *is* visible out here
```

If you declare a variable without assigning any value to it, its type is `undefined`.  
An important difference between JavaScript and other languages like Java is that in JavaScript, **blocks do not have scope; only functions have a scope.** So if a variable is defined using `var` in a compound statement (for example inside an `if` control structure), it will be visible to the **entire function**. However, starting with ECMAScript 2015, [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let) and [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const) declarations allow you to create block-scoped variables.

### Difference Between `let` and `var`
[javascript - What is the difference between "let" and "var"? - Stack Overflow](https://stackoverflow.com/questions/762011/what-is-the-difference-between-let-and-var)
- `let` is visible to the scope
- `var` is visible to the function, and it will create a property on the global object

## Hacks
- Use `+` prefix to convert something to number