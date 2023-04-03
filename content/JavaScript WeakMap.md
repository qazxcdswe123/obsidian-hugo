---
aliases: []
date created: Sep 13th, 2022
date modified: Sep 13th, 2022
---
[WeakMap - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)
## What is WeakMap
A **`WeakMap`** is a collection of key/value pairs whose keys must be objects, with values of any arbitrary [JavaScript type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#javascript_types), and which does not create strong references to its keys.  
That is, an object's presence as a key in a `WeakMap` does not prevent the object from being garbage collected. Once an object used as a key has been collected, its corresponding values in any `WeakMap` become candidates for garbage collection as well — as long as they aren't strongly referred to elsewhere.

## Why use WeakMap
