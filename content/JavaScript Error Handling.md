---
aliases: []
date created: Sep 2nd, 2022
date modified: Sep 2nd, 2022
---
## Try Catch
- `try...catch` works synchronously
	- To catch an exception inside a scheduled function, `try...catch` must be inside that function:

```js
setTimeout(function() {
  try {
    noSuchVariable; // try...catch handles the error!
  } catch {
    alert( "error is caught here!" );
  }
}, 1000);
```

- `try...catch` only works for runtime errors
	- For `try...catch` to work, the code must be runnable. In other words, it should be valid JavaScript.

## Throw Operator
```javascript
throw <error object>
let error = new Error(message);
let error = new SyntaxError(message);
let error = new ReferenceError(message);
```

## Finally
The `finally` clause is a great place to finish the measurements no matter what.


Variables are local inside `try...catch...finally`
