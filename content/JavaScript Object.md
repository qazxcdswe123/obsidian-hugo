---
aliases: []
date created: May 8th, 2022
date modified: Sep 13th, 2022
---
[[JavaScript Array]]  
[[JavaScript Date Object]]  
[[JavaScript Map and Set]]  
[[JavaScript WeakMap]]
[Src](https://zh.javascript.info/object)

JavaScript objects can be thought of as simple collections of name-value pairs. As such, they are similar to:
- Dictionaries in Python.
- Hashes in Perl and Ruby.
- Hash tables in C and C++.
- HashMaps in Java.
- Associative arrays in PHP.

There are two basic ways to create an empty object:

```js
const obj = new Object();
const obj = {};
```

## [Object.keys，values，entries](https://zh.javascript.info/keys-values-entries#objectkeysvaluesentries)
对于普通对象，下列这些方法是可用的：
- [Object.keys(obj)](https://developer.mozilla.org/zh/docs/Web/JavaScript/Reference/Global_Objects/Object/keys) —— 返回一个包含该对象所有的键的数组。
- [Object.values(obj)](https://developer.mozilla.org/zh/docs/Web/JavaScript/Reference/Global_Objects/Object/values) —— 返回一个包含该对象所有的值的数组。
- [Object.entries(obj)](https://developer.mozilla.org/zh/docs/Web/JavaScript/Reference/Global_Objects/Object/entries) —— 返回一个包含该对象所有 \[key, value\] 键值对的数组。

- `Map.keys()` 返回可迭代项
- `Object.keys(obj)` 返回“真正的”数组

## Objects Vs Map
- The keys of an `Object` are [`Strings`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String) or [`Symbols`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol), where they can be of any value for a `Map`.
- You can get the `size` of a `Map` easily, while you have to manually keep track of size for an `Object`.
- The iteration of maps is in insertion order of the elements.
- An `Object` has a prototype, so there are default keys in the map. (This can be bypassed using `map = Object.create(null)`.)

___

- Use maps over objects when keys are unknown until run time, and when all keys are the same type and all values are the same type.
- Use maps if there is a need to store primitive values as keys because object treats each key as a string whether it's a number value, boolean value or any other primitive value.
- Use objects when there is logic that operates on individual elements.

## Objects Prototype
[Object prototypes - Learn web development | MDN](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes)  
Every object in JavaScript has a built-in property, which is called its **prototype**. The prototype is itself an object, so the prototype will have its own prototype, making what's called a **prototype chain**. The chain ends when we reach a prototype that has `null` for its own prototype.
