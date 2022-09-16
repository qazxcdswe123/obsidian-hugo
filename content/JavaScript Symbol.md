---
aliases: []
tags: []
date created: Sep 10th, 2022
date modified: Sep 13th, 2022
---
[Symbol - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)  
Starting with ECMAScript 2015, `symbol` is a primitive data type, just like `number` and `string`.  
`symbol` values are created by calling the `Symbol` constructor.

Symbols are immutable, and unique.

```ts
let sym2 = Symbol("key");
let sym3 = Symbol("key");
sym2 === sym3; // false, symbols are unique
```