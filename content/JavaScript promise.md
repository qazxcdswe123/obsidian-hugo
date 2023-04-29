---
aliases: []
date created: Aug 21st, 2022
date modified: Sep 6th, 2022
---

- [Promise - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)  
- [How to escape Promise Hell. Unlike Callback Hell, Promise Hell is… | by Ronald Chen | Medium](https://medium.com/@pyrolistical/how-to-get-out-of-promise-hell-8c20e0ab0513)  

A [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) is an [[JavaScript Object]] representing the eventual completion or failure of an [[asynchronous]] operation.

Promises are about making [[asynchronous]] code retain most of the lost properties of synchronous code such as flat indentation and one exception channel.

A promise is commonly defined as **a proxy for a value that will eventually become available**.  
![](https://img.ynchen.me/2022/09/45a744c38cf26022564ee5527535a188.png)


## Promise Executor
Set the state and return the value.

A Promise executor should call only one `resolve` or one `reject`. Once one state is changed `(pending => fulfilled or pending => rejected)`, that's all. Any further calls to `resolve` or `reject` will be ignored.

The executor runs automatically and attempts to perform a job. When it is finished with the attempt, it calls `resolve` if it was successful or `reject` if there was an error.

The `promise` object returned by the `new Promise` constructor has these internal properties:
- `state` — initially `"pending"`, then changes to either `"fulfilled"` when `resolve` is called or `"rejected"` when `reject` is called.
- `result` — initially `undefined`, then changes to `value` when `resolve(value)` is called or `error` when `reject(error)` is called.

## Promise Consumer
Deal with the value or value.

The constructor function takes a function as an argument. This function is called the `executor/consumer function`.

### .then
The first argument of `.then` is a function that runs when the promise is **resolved** and receives the result.  
The second argument of `.then` is a function that runs when the promise is **rejected** and receives the error.  
If we’re interested only in successful completions, then we can provide only one function argument to `.then`:

```js
let promise = new Promise(function(resolve, reject) {
  setTimeout(() => resolve("done!"), 1000);
});

// resolve runs the first function in .then
promise.then(
  result => alert(result), // shows "done!" after 1 second
  error => alert(error) // doesn't run because it was resolved
);
```

### .catch
If we’re interested only in errors, then we can use `null` as the first argument: `.then(null, errorHandlingFunction)`. Or we can use `.catch(errorHandlingFunction)`, which is exactly the same:

```js
let promise = new Promise((resolve, reject) => {
  setTimeout(() => reject(new Error("Whoops!")), 1000);
});

// .catch(f) is the same as promise.then(null, f)
promise.catch(alert); // shows "Error: Whoops!" after 1 second
```

The call `.catch(f)` is a complete analog of `.then(null, f)`, it’s just a shorthand.

### .finally
The idea of `finally` is to set up a handler for performing cleanup/finalizing after the previous operations are complete.

```js
new Promise((resolve, reject) => {
  /* do something that takes time, and then call resolve or maybe reject */
})
  // runs when the promise is settled, doesn't matter successfully or not
  .finally(() => stop loading indicator)
  // so the loading indicator is always stopped before we go on
  .then(result => show result, err => show error)
```

1. A `finally` handler has no arguments. In `finally` we don’t know whether the promise is successful or not. That’s all right, as our task is usually to perform “general” finalizing procedures.
2. A `finally` handler “passes through” the result or error to the next suitable handler.  
3. A `finally` handler also shouldn’t return anything. If it does, the returned value is silently ignored.  
The only exception to this rule is when a `finally` handler throws an error. Then this error goes to the next handler, instead of any previous outcome.

`finally` is not meant to process a promise result. As said, it’s a place to do generic cleanup, no matter what the outcome was.

## Promises Chaining
### Returning Promises

```js
new Promise(function (resolve, reject) {
  setTimeout(() => resolve(1), 1000);
})
  .then(function (result) {
    alert(result); // 1

    return new Promise((resolve, reject) => {
      setTimeout(() => resolve(result * 2), 1000);
    });
  })
  .then(function (result) {
    alert(result); // 2

    return new Promise((resolve, reject) => {
      setTimeout(() => resolve(result * 2), 1000);
    });
  })
  .then(function (result) {
    alert(result); // 4
  });
```

## Methods
### Promise.catch()
If we throw an Error like `new Error("Something wrong!")`  instead of calling the `reject` from the promise executor and handlers, it will still be treated as a rejection. It means that this will be caught by the `.catch` handler method.  

The **`catch()`** method returns a [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) and deals with rejected cases only. It behaves the same as calling [`Promise.prototype.then(undefined, onRejected)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then) (in fact, calling `obj.catch(onRejected)` internally calls `obj.then(undefined, onRejected)`). 
This means that you have to provide an `onRejected` function even if you want to fall back to an `undefined` result value - for example `obj.catch(() => {})`.

### Promise.prototype.finally()
The **`finally()`** method of a [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) schedules a function, the _callback function_, to be called when the promise is settled. Like `then()` and `catch()`, it immediately returns an equivalent [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) object, allowing you to chain calls to another promise method, an operation called _composition_.

```js
function checkMail() {
  return new Promise((resolve, reject) => {
    if (Math.random() > 0.5) {
      resolve('Mail has arrived');
    } else {
      reject(new Error('Failed to arrive'));
    }
  });
}

checkMail()
  .then((mail) => {
    console.log(mail);
  })
  .catch((err) => {
    console.error(err);
  })
  .finally(() => {
    console.log('Experiment completed');
  });
```

### Promise.resolve()
[Promise.resolve() - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve)  
The **`Promise.resolve()`** method "resolves" a given value to a [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise). If the value is a promise, that promise is returned; if the value is a [thenable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#thenables), `Promise.resolve()` will call the `then()` method with two callbacks it prepared; otherwise the returned promise will be fulfilled with the value.

### Promise.all()
[Promise.all() - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all)  
The **`Promise.all()`** method takes an iterable of promises as an input, and returns a single [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that resolves to an array of the results of the input promises. This returned promise will fulfil when all of the input's promises have fulfilled, or if the input iterable contains no promises. It rejects immediately upon any of the input promises rejecting or non-promises throwing an error, and will reject with this first rejection message / error.  
It is done when any one of the promises is settled.

- Example with promises array

```js
return getCurrentUser()
  .then((user) => {
    const foodPromise = attachFavouriteFood && getFood(user.favouriteFoodId);
    const schoolPromise = attachSchool && getSchool(user.schoolId);
    const facultyPromise = attachSchool && attachFaculty && schoolPromise
      .then((school) => getUsers(school.facultyIds));

    return Promise.all([foodPromise, schoolPromise, facultyPromise])
      .then(([food, school, faculty]) => {
        if (food) {
          user.food = food;
        }
        if (school) {
          user.school = school;
          if (faculty) {
            user.school.faculty = faculty;
          }
        }
        return user;
      });
  });
```

`Promise.all()` will just pass through non-promises, so using undefined is safe. This will scale better to any set of dependencies.

### Promise.allSettled()
The **`Promise.allSettled()`** method returns a promise that fulfills after all of the given promises have either fulfilled or rejected, with an array of objects that each describes the outcome of each promise.  
It is typically used when you have multiple [[asynchronous]] tasks that are not dependent on one another to complete successfully, or you'd always like to know the result of each promise.  
In comparison, the Promise returned by [`Promise.all()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all) may be more appropriate if the tasks are dependent on each other / if you'd like to immediately reject upon any of them rejecting.
