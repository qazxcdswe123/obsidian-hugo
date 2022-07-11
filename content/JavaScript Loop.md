JavaScript's [`for` loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for) is the same as that in C and Java: it lets you provide the control information for your loop on a single line.
```
for (let i = 0; i < 5; i++) {
  // Will execute 5 times
}
```
___
JavaScript also contains two other prominent for loops: [`for`...`of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
```
for (let value of array) {
  // do something with value
}
```
[for of Must be iterable](https://zh.javascript.info/iterable#zong-jie)