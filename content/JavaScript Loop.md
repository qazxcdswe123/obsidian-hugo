---
aliases: []
date created: Jul 8th, 2022
date modified: Sep 9th, 2022
---
[TypeScript: Documentation - Iterators and Generators](https://www.typescriptlang.org/docs/handbook/iterators-and-generators.html)

JavaScript's [`for` loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for) is the same as that in C and Java: it lets you provide the control information for your loop on a single line.

```js
for (let i = 0; i < 5; i++) {
  // Will execute 5 times
}
```

___
JavaScript also contains two other prominent for loops: [`for`...`of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of) and [`for`...`in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration#for...in_statement)

### For of

```js
for (let value of array) {
  // do something with value
}
```

[for of Must be iterable](https://zh.javascript.info/iterable#zong-jie)

### For in
The [`for...in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in) statement iterates a specified variable over all the enumerable properties of an object. For each distinct property, JavaScript executes the specified statements. A `for...in` statement looks as follows:

```
for (variable in object)
  statement
```
