---
aliases: []
date created: Sep 10th, 2022
date modified: Sep 13th, 2022
---
The main purpose of `Symbol` is to serve as a unique identifier for object properties
- Symbols are immutable, and unique.

```ts
let sym2 = Symbol("key");
let sym3 = Symbol("key");
sym2 === sym3; // false, symbols are unique
```

- [Symbol - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)  