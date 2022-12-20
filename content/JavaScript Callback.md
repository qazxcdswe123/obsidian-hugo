---
aliases: []
tags: []
date created: Aug 21st, 2022
date modified: Dec 17th, 2022
---

## Error-First Callback
[Error-First Callback in Node.js - GeeksforGeeks](https://www.geeksforgeeks.org/error-first-callback-in-node-js)  

**Error-First Callback** in Node.js is a function which either returns an error object or any successful data returned by the function.
1. The first argument of the `callback` is reserved for an **error** if it occurs. Then `callback(err)` is called.
2. The second argument (and the next ones if needed) are for the **successful result**. Then `callback(null, result1, result2…)` is called.

## Function Callback
[JavaScript Callbacks](https://www.w3schools.com/js/js_callback.asp)
- A callback is a function passed as an argument to another function
- A callback function can run **after** another function has finished  
The second argument is a function (usually anonymous) that runs when the action is completed.

## Example
```js
function myDisplayer(some) {
  document.getElementById("demo").innerHTML = some;
}

function myCalculator(num1, num2, myCallback) {
  let sum = num1 + num2;
  myCallback(sum);
}

myCalculator(5, 5, myDisplayer);
```

When you pass a function as an argument, remember not to use parenthesis.  
Right: `myCalculator(5, 5, myDisplayer);`  
Wrong: ~~myCalculator(5, 5, myDisplayer())~~;

## When to Use a Callback?
Where callbacks really shine are in asynchronous functions, where one function has to wait for another function (like waiting for a file to load).