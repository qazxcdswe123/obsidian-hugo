-  Filter
[Src](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)
The **`filter()`** method **creates a new array** with all elements that pass the test implemented by the provided function.

- From
[MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from)
[Src](https://zh.javascript.info/iterable#arrayfrom)
```js
let arr = Array.from(range, num => num * num); 
alert(arr); // 1,4,9,16,25

console.log(Array.from('foo'));
// expected output: Array ["f", "o", "o"]

console.log(Array.from([1, 2, 3], x => x + x));
// expected output: Array [2, 4, 6]
```