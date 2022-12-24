## Convert `Set` to `Array`
```js
this.tagList = [...new Set(this.tagArrayFilter)];
```
The use of the spread syntax allows us to easily create a new array that only includes unique elements from the `this.tagArrayFilter` array.