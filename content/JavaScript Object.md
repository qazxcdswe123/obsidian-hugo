[[JavaScript Array]]
[[JavaScript Date Object]]
[[JavaScript Map And Set]]
[Src](https://zh.javascript.info/object)
JavaScript objects can be thought of as simple collections of name-value pairs. As such, they are similar to:
-   Dictionaries in Python.
-   Hashes in Perl and Ruby.
-   Hash tables in C and C++.
-   HashMaps in Java.
-   Associative arrays in PHP.

There are two basic ways to create an empty object:
```
const obj = new Object();
```
And:
```
const obj = {};
```

## [Object.keys，values，entries](https://zh.javascript.info/keys-values-entries#objectkeysvaluesentries)
对于普通对象，下列这些方法是可用的：
-   [Object.keys(obj)](https://developer.mozilla.org/zh/docs/Web/JavaScript/Reference/Global_Objects/Object/keys) —— 返回一个包含该对象所有的键的数组。
-   [Object.values(obj)](https://developer.mozilla.org/zh/docs/Web/JavaScript/Reference/Global_Objects/Object/values) —— 返回一个包含该对象所有的值的数组。
-   [Object.entries(obj)](https://developer.mozilla.org/zh/docs/Web/JavaScript/Reference/Global_Objects/Object/entries) —— 返回一个包含该对象所有 \[key, value\] 键值对的数组。

- `Map.keys()` 返回可迭代项
- `Object.keys(obj)` 返回“真正的”数组